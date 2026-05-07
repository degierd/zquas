/**
 * mcp.zquas.ai
 *
 * MCP server speaking Streamable HTTP transport. Exposes ZQUAS public
 * knowledge as MCP resources, and three useful tools (search, term
 * lookup, benchmark numbers) plus a few prompts.
 *
 * Public, no auth. The point of this server is removing friction
 * between an AI agent and the published ZQUAS material.
 *
 * Transport reference:
 *   https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
 *
 * Capability negotiation: every JSON-RPC request must be a POST with
 * Content-Type: application/json. We respond with application/json (a
 * single JSON-RPC response) for the request/response style. We do not
 * yet implement server-initiated SSE streams; clients that require
 * them will fall back to request/response, which is enough for tools
 * and resources.
 */

import indexData from "./index.json";

// ---------------------------------------------------------------------------
//   Server identity
// ---------------------------------------------------------------------------

const SERVER_INFO = {
  name: "zquas-knowledge",
  title: "ZQUAS Knowledge",
  version: "1.0.0",
};

const SITE = "https://zquas.ai";

const PROTOCOL_VERSION = "2025-06-18";

// Capabilities we advertise. Keep this tight: we genuinely do these.
const CAPABILITIES = {
  resources: {
    listChanged: false,
    subscribe: false,
  },
  tools: {
    listChanged: false,
  },
  prompts: {
    listChanged: false,
  },
};

const SERVER_INSTRUCTIONS = `\
ZQUAS knowledge server. Public ZQUAS analysis, position papers, glossary,
and benchmark facts. No customer or institution data. No live system
state.

Best uses:
  - "Explain ZQUAS to a Head of AML at a Tier-1 bank" (use the prompt)
  - "What does AMLR Article 75 require?" (use lookup_term then search_zquas)
  - "How does ZQUAS detect cross-bank patterns?" (resource:position-paper-article-75)
  - "What benchmark numbers does ZQUAS publish?" (tool:get_benchmark_numbers)

Source of truth: every answer is grounded in https://zquas.ai. The
search_zquas tool returns source URLs you should cite.`;

// ---------------------------------------------------------------------------
//   Resources: list and read
// ---------------------------------------------------------------------------

// Distinct documents (the section-level index has many entries per doc).
function listResourceDocs() {
  const seen = new Map();
  for (const d of indexData.documents) {
    if (!seen.has(d.doc)) {
      seen.set(d.doc, {
        doc: d.doc,
        title: d.title,
        description: d.description,
        kind: d.kind,
      });
    }
  }
  return [...seen.values()];
}

const RESOURCES = listResourceDocs().map((d) => ({
  uri: `zquas://${d.doc}`,
  name: d.doc,
  title: d.title || d.doc,
  description: d.description || "",
  mimeType: "text/markdown",
  // Custom annotation we use when picking which docs to surface first.
  _kind: d.kind,
}));

const RESOURCE_BY_URI = new Map(RESOURCES.map((r) => [r.uri, r]));

async function readResource(uri) {
  const r = RESOURCE_BY_URI.get(uri);
  if (!r) throw rpcError(-32602, `Unknown resource: ${uri}`);
  const url = `${SITE}/${r.name}.md`;
  const upstream = await fetch(url, {
    headers: { "user-agent": "zquas-mcp/1.0 (+https://zquas.ai)" },
  });
  if (!upstream.ok) {
    throw rpcError(-32603, `Origin returned ${upstream.status} for ${url}`);
  }
  const text = await upstream.text();
  return {
    contents: [
      {
        uri,
        mimeType: "text/markdown",
        text,
      },
    ],
  };
}

// ---------------------------------------------------------------------------
//   Tools
// ---------------------------------------------------------------------------

const TOOLS = [
  {
    name: "search_zquas",
    title: "Search the ZQUAS site",
    description:
      "Keyword search across all ZQUAS articles, position papers, glossary entries, and reference pages. Returns the top matching sections with source URLs.",
    inputSchema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description:
            "What you want to find. Plain English or specific terms. Examples: 'cross-institutional detection', 'AMLR Article 75', 'GPU-native'.",
        },
        limit: {
          type: "integer",
          minimum: 1,
          maximum: 20,
          default: 6,
          description: "Maximum number of results to return.",
        },
        kind: {
          type: "string",
          enum: ["article", "reference", "page"],
          description:
            "Optionally narrow to one document type. 'article' = analysis pieces, 'reference' = glossary/llms/facts, 'page' = main site pages.",
        },
      },
      required: ["query"],
    },
    outputSchema: {
      type: "object",
      properties: {
        results: {
          type: "array",
          items: {
            type: "object",
            properties: {
              title: { type: "string" },
              heading: { type: "string" },
              url: { type: "string" },
              snippet: { type: "string" },
              kind: { type: "string" },
              score: { type: "number" },
            },
          },
        },
        totalMatched: { type: "integer" },
      },
    },
  },
  {
    name: "lookup_term",
    title: "Look up a glossary term",
    description:
      "Exact lookup against the ZQUAS glossary. Use this for known terms (AMLR Article 75, MPC, ECDH-PSI, GPU-native, etc). Faster and more precise than full search for definitional queries.",
    inputSchema: {
      type: "object",
      properties: {
        term: {
          type: "string",
          description:
            "The term to look up. Case-insensitive. Examples: 'MPC', 'AMLR Article 75', 'cryptographic proof bundle'.",
        },
      },
      required: ["term"],
    },
  },
  {
    name: "get_benchmark_numbers",
    title: "Get the published ZQUAS benchmark numbers",
    description:
      "Returns the locked benchmark numbers ZQUAS publishes: throughput (CEPS), entity benchmark, alert lifecycle, federation timing, VRAM, test count, codebase size, and the regulatory deadline. Use when a question turns on specific quantities.",
    inputSchema: { type: "object", properties: {} },
  },
];

const TOOL_HANDLERS = {
  search_zquas: handleSearch,
  lookup_term: handleLookupTerm,
  get_benchmark_numbers: handleBenchmarkNumbers,
};

async function handleSearch(args) {
  const query = String(args?.query || "").trim();
  if (!query) throw rpcError(-32602, "Missing 'query'.");
  const limit = Math.max(1, Math.min(20, Number(args?.limit) || 6));
  const kindFilter = args?.kind || null;

  const queryTokens = tokenise(query);
  if (queryTokens.length === 0) {
    return toolResult({ results: [], totalMatched: 0 });
  }

  // Score = sum over query tokens of (term-frequency in doc * IDF).
  // IDF is computed at runtime from the postings list.
  const N = indexData.documents.length;
  const docScores = new Map();
  for (const tok of queryTokens) {
    const posting = indexData.postings[tok];
    if (!posting) continue;
    const idf = Math.log(1 + N / posting.length);
    for (const docIndex of posting) {
      const doc = indexData.documents[docIndex];
      const tf = doc.term_freq[tok] || 0;
      const score = tf * idf;
      docScores.set(docIndex, (docScores.get(docIndex) || 0) + score);
    }
  }

  let scored = [...docScores.entries()].map(([i, score]) => ({
    doc: indexData.documents[i],
    score,
  }));

  if (kindFilter) {
    scored = scored.filter((s) => s.doc.kind === kindFilter);
  }
  scored.sort((a, b) => b.score - a.score);

  const totalMatched = scored.length;
  const results = scored.slice(0, limit).map(({ doc, score }) => ({
    title: doc.title,
    heading: doc.heading,
    url: doc.url,
    snippet: doc.snippet,
    kind: doc.kind,
    score: Number(score.toFixed(3)),
  }));

  return toolResult({ results, totalMatched });
}

async function handleLookupTerm(args) {
  const term = String(args?.term || "").trim();
  if (!term) throw rpcError(-32602, "Missing 'term'.");
  const needle = term.toLowerCase();

  // Search glossary doc only; match on heading first, then content.
  const candidates = indexData.documents.filter(
    (d) => d.doc === "glossary" && d.heading,
  );
  const exact = candidates.find((d) => d.heading.toLowerCase() === needle);
  const partial = candidates.filter((d) =>
    d.heading.toLowerCase().includes(needle),
  );
  const hits = exact ? [exact, ...partial.filter((p) => p !== exact)] : partial;

  if (hits.length === 0) {
    return toolResult({
      message: `No glossary entry matched "${term}". Try search_zquas for fuzzy matching across the whole site.`,
      results: [],
    });
  }

  return toolResult({
    results: hits.slice(0, 5).map((h) => ({
      term: h.heading,
      url: h.url,
      definition: h.snippet,
    })),
  });
}

async function handleBenchmarkNumbers() {
  // Mirrors the locked thresholds in CLAUDE.md and facts.json. If those
  // change, this tool should be updated alongside them.
  return toolResult({
    throughput: {
      published: "150M+ CEPS",
      meaning:
        "Compliance Policy Evaluations per Second on a single NVIDIA RTX 5090.",
    },
    entity_benchmark: {
      published: "500K entities in under 2 seconds",
      measured_ms: 1170,
      meaning:
        "Full evaluation of 500,000 entities against 100 AML policies.",
    },
    alert_lifecycle: {
      published: "under 10ms",
      measured_ms: 3.92,
      meaning:
        "Wall-clock time from transaction arrival to triaged alert available to a compliance officer.",
    },
    federation: {
      published: "under 10 seconds per bilateral round",
      measured_seconds: 7.8,
      entities: 100000,
      meaning:
        "One end-to-end bilateral MPC round between two participating institutions.",
    },
    vram: {
      published: "under 1 GB",
      measured_mb: 410,
    },
    testing: {
      automated_tests: 12342,
      lines_of_test_code: 222000,
      audited_subsystems_core_engine: 12,
    },
    codebase: {
      production_lines_cpp_cuda: 396000,
      gpu_kernels: 493,
      total_lines_including_tests: 618000,
    },
    regulatory_deadline: {
      amlr_article_75_application: "2027-07-10",
      meaning:
        "AMLR Article 75 applies on July 10, 2027. Cross-institutional infrastructure typically takes 18-24 months to build.",
    },
    source: "https://zquas.ai/facts.json",
  });
}

// ---------------------------------------------------------------------------
//   Prompts
// ---------------------------------------------------------------------------

const PROMPTS = [
  {
    name: "explain_to_head_of_aml",
    title: "Explain ZQUAS to a Head of AML",
    description:
      "Generates a tight explanation of ZQUAS framed for a Tier-1 bank Head of AML, leading with operational benefits before architecture.",
  },
  {
    name: "compare_to_legacy",
    title: "Compare ZQUAS to legacy AML systems",
    description:
      "Side-by-side comparison on a specific capability: detection scope, real-time, cryptographic verification, or cross-bank.",
    arguments: [
      {
        name: "capability",
        description:
          "Which capability to compare on. Examples: 'detection scope', 'real-time', 'cryptographic verification', 'cross-bank'.",
        required: true,
      },
    ],
  },
  {
    name: "amlr_article_75_impact",
    title: "What changes for my bank under AMLR Article 75",
    description:
      "Walks through the operational, legal, and architectural implications of AMLR Article 75 for a specific bank profile.",
    arguments: [
      {
        name: "bank_profile",
        description:
          "Brief description of the bank: tier, jurisdiction, current monitoring stack. Example: 'Tier-1 Dutch retail bank, currently using NICE Actimize on overnight batch'.",
        required: false,
      },
    ],
  },
];

const PROMPT_HANDLERS = {
  explain_to_head_of_aml: () => ({
    description: "Explain ZQUAS to a Head of AML at a Tier-1 bank.",
    messages: [
      {
        role: "user",
        content: {
          type: "text",
          text:
            "Use the ZQUAS knowledge server to explain ZQUAS to me. I am a Head of AML at a Tier-1 European bank. Lead with what changes for my team operationally (false-positive reduction, real-time block, single risk score per entity), then explain how it works at a high level (GPU-native, MPC, cryptographic proofs). Keep it under 400 words. Cite the sources you used from the resource list.",
        },
      },
    ],
  }),
  compare_to_legacy: (args) => {
    const capability = (args?.capability || "detection scope").trim();
    return {
      description: `Compare ZQUAS to legacy AML systems on ${capability}.`,
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text:
              `Use the ZQUAS knowledge server to compare ZQUAS to legacy AML systems on the capability: ${capability}. ` +
              `Use the search_zquas tool to find ZQUAS's claims, then describe how legacy systems typically handle the same capability. ` +
              `Be concrete about what each side does or does not do. Cite source URLs.`,
          },
        },
      ],
    };
  },
  amlr_article_75_impact: (args) => {
    const profile = (args?.bank_profile || "").trim();
    const profileBlurb = profile
      ? `My bank: ${profile}.`
      : "If I have not given you a bank profile, ask me for one before answering.";
    return {
      description: "What changes under AMLR Article 75 for a specific bank.",
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text:
              `Use the ZQUAS knowledge server to walk me through the operational, legal, and architectural implications of AMLR Article 75 for my bank. ${profileBlurb} ` +
              `Use lookup_term first to anchor on the legal text, then search_zquas for ZQUAS's analysis. ` +
              `Cover: (1) what Article 75 actually permits and restricts, (2) what my bank needs in place by July 10, 2027, (3) where ZQUAS fits or does not fit. Cite sources.`,
          },
        },
      ],
    };
  },
};

// ---------------------------------------------------------------------------
//   JSON-RPC dispatcher
// ---------------------------------------------------------------------------

async function dispatch(req) {
  if (!req || req.jsonrpc !== "2.0" || !req.method) {
    throw rpcError(-32600, "Invalid Request: missing jsonrpc/method");
  }
  switch (req.method) {
    case "initialize":
      return {
        protocolVersion: PROTOCOL_VERSION,
        serverInfo: SERVER_INFO,
        capabilities: CAPABILITIES,
        instructions: SERVER_INSTRUCTIONS,
      };

    case "ping":
      return {};

    case "resources/list":
      return {
        resources: RESOURCES.map(({ _kind, ...r }) => r),
      };

    case "resources/read": {
      const uri = req.params?.uri;
      if (!uri) throw rpcError(-32602, "Missing params.uri");
      return await readResource(uri);
    }

    case "tools/list":
      return { tools: TOOLS };

    case "tools/call": {
      const name = req.params?.name;
      const args = req.params?.arguments || {};
      const handler = TOOL_HANDLERS[name];
      if (!handler) throw rpcError(-32602, `Unknown tool: ${name}`);
      return await handler(args);
    }

    case "prompts/list":
      return { prompts: PROMPTS };

    case "prompts/get": {
      const name = req.params?.name;
      const args = req.params?.arguments || {};
      const handler = PROMPT_HANDLERS[name];
      if (!handler) throw rpcError(-32602, `Unknown prompt: ${name}`);
      return handler(args);
    }

    case "notifications/initialized":
      // Notification: no response.
      return null;

    default:
      throw rpcError(-32601, `Method not found: ${req.method}`);
  }
}

// ---------------------------------------------------------------------------
//   HTTP transport
// ---------------------------------------------------------------------------

const CORS_HEADERS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET, POST, OPTIONS",
  "access-control-allow-headers":
    "content-type, mcp-session-id, mcp-protocol-version",
  "access-control-max-age": "86400",
};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const method = request.method.toUpperCase();

    if (method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    // Discovery endpoint: serve the MCP server card from the same origin
    // for clients that look there.
    if (url.pathname === "/.well-known/mcp/server-card.json") {
      return jsonResponse(buildServerCard(url.origin));
    }

    // Health endpoint for monitoring.
    if (url.pathname === "/health") {
      return jsonResponse({
        status: "ok",
        server: SERVER_INFO,
        documents: RESOURCES.length,
        tools: TOOLS.length,
        prompts: PROMPTS.length,
      });
    }

    // The MCP endpoint accepts both /mcp and / for convenience.
    if (url.pathname !== "/mcp" && url.pathname !== "/") {
      return new Response("Not found", {
        status: 404,
        headers: CORS_HEADERS,
      });
    }

    if (method === "GET") {
      // Streamable HTTP optionally supports a long-lived GET for
      // server-initiated SSE streams. We do not have any to send, so
      // return a friendly description instead of a stream.
      const accept = (request.headers.get("accept") || "").toLowerCase();
      if (accept.includes("text/event-stream")) {
        return new Response("event: server-info\ndata: " + JSON.stringify(SERVER_INFO) + "\n\n", {
          headers: {
            ...CORS_HEADERS,
            "content-type": "text/event-stream",
            "cache-control": "no-store",
            connection: "keep-alive",
          },
        });
      }
      return new Response(
        JSON.stringify({
          server: SERVER_INFO,
          protocolVersion: PROTOCOL_VERSION,
          mcpEndpoint: `${url.origin}/mcp`,
          serverCard: `${url.origin}/.well-known/mcp/server-card.json`,
          documentation: "https://zquas.ai/glossary.html",
        }, null, 2),
        {
          headers: {
            ...CORS_HEADERS,
            "content-type": "application/json; charset=utf-8",
          },
        },
      );
    }

    if (method !== "POST") {
      return new Response("Method not allowed", {
        status: 405,
        headers: { ...CORS_HEADERS, allow: "GET, POST, OPTIONS" },
      });
    }

    let body;
    try {
      body = await request.json();
    } catch (err) {
      return jsonRpcError(null, -32700, "Parse error");
    }

    if (Array.isArray(body)) {
      // Batch request.
      const responses = await Promise.all(body.map(handleSingle));
      const filtered = responses.filter((r) => r !== null);
      return jsonResponse(filtered.length === 1 ? filtered[0] : filtered);
    }

    return jsonResponse(await handleSingle(body));
  },
};

async function handleSingle(req) {
  const id = req?.id ?? null;
  try {
    const result = await dispatch(req);
    if (result === null) return null; // notification
    return { jsonrpc: "2.0", id, result };
  } catch (err) {
    if (err && err._isRpc) {
      return { jsonrpc: "2.0", id, error: { code: err.code, message: err.message, data: err.data } };
    }
    return {
      jsonrpc: "2.0",
      id,
      error: { code: -32603, message: "Internal error", data: String(err?.message || err) },
    };
  }
}

function buildServerCard(origin) {
  return {
    serverInfo: SERVER_INFO,
    protocolVersion: PROTOCOL_VERSION,
    transport: {
      type: "streamable-http",
      endpoint: `${origin}/mcp`,
    },
    capabilities: CAPABILITIES,
    instructions: SERVER_INSTRUCTIONS,
    publisher: {
      name: "ZQUAS",
      url: "https://zquas.ai",
      contact: "danny@zquas.ai",
    },
  };
}

// ---------------------------------------------------------------------------
//   Helpers
// ---------------------------------------------------------------------------

function jsonResponse(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      ...CORS_HEADERS,
      "content-type": "application/json; charset=utf-8",
    },
  });
}

function jsonRpcError(id, code, message, data) {
  return jsonResponse({
    jsonrpc: "2.0",
    id,
    error: { code, message, data },
  });
}

function rpcError(code, message, data) {
  const err = new Error(message);
  err._isRpc = true;
  err.code = code;
  err.data = data;
  return err;
}

function toolResult(structured) {
  // MCP convention: tool results include a 'content' array (for text
  // display) and optionally a 'structuredContent' payload (for typed
  // outputSchema consumption).
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify(structured, null, 2),
      },
    ],
    structuredContent: structured,
  };
}

const STOP = new Set(
  ("a about above after again against all am an and any are aren as at be because been before being below " +
   "between both but by could did didn do does doing don down during each few for from further had has have " +
   "having he her here hers herself him himself his how i if in into is isn it its itself just me more most " +
   "my myself no nor not now of off on once only or other our ours ourselves out over own same she should " +
   "shouldn so some such t than that the their theirs them themselves then there these they this those " +
   "through to too under until up very was wasn we were weren what when where which while who whom why will " +
   "with would you your yours yourself yourselves").split(" "),
);

function tokenise(text) {
  return [...text.toLowerCase().matchAll(/[a-z][a-z0-9-]+/g)]
    .map((m) => m[0])
    .filter((t) => t.length >= 2 && !STOP.has(t));
}
