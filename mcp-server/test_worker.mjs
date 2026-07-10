/**
 * Smoke-test the MCP worker handlers without spinning up wrangler dev.
 *
 *   node test_worker.mjs
 *
 * Loads the worker module, calls `dispatch()` (re-exported via the
 * default fetch handler) by faking Request objects, and prints the
 * JSON-RPC responses for the protocol's main methods. If anything
 * throws, you'll see it.
 *
 * Exits 0 when every check passes, 1 otherwise, so this can gate CI.
 * A case that passes `expectErrorCode` inverts the check: a JSON-RPC
 * error with that code is the pass condition, and a result is a failure.
 */

import { readFileSync } from "node:fs";

// We can't easily import the Cloudflare Worker module here because it
// imports JSON via the Cloudflare bundler. Re-implement the handler
// invocation by reading worker.js as a string and patching imports.

const workerSource = readFileSync(new URL("./src/worker.js", import.meta.url), "utf8");
const indexJson = readFileSync(new URL("./src/index.json", import.meta.url), "utf8");

// Replace the JSON import with an inline literal.
const patched = workerSource.replace(
  /import indexData from "\.\/index\.json";/,
  `const indexData = ${indexJson};`,
);

const moduleUrl = "data:text/javascript;base64," + Buffer.from(patched).toString("base64");
const mod = await import(moduleUrl);
const handler = mod.default;

let failures = 0;

async function call(method, params, label = method, { expectErrorCode = null } = {}) {
  const req = new Request("http://test.local/mcp", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, params }),
  });
  const res = await handler.fetch(req);
  const body = await res.json();
  console.log(`\n=== ${label} (status ${res.status}) ===`);

  if (expectErrorCode !== null) {
    if (!body.error) {
      failures++;
      console.log(`FAIL: expected JSON-RPC error ${expectErrorCode}, got a result`);
    } else if (body.error.code !== expectErrorCode) {
      failures++;
      console.log(`FAIL: expected error code ${expectErrorCode}, got ${body.error.code}`, body.error);
    } else {
      console.log("OK: got the expected error:", body.error);
    }
    return body;
  }

  if (body.error) {
    failures++;
    console.log("FAIL:", body.error);
  } else {
    const text = JSON.stringify(body.result, null, 2);
    console.log(text.length > 1500 ? text.slice(0, 1500) + "\n... [truncated]" : text);
  }
  return body;
}

await call("initialize", { protocolVersion: "2025-06-18" });
await call("resources/list", {}, "resources/list (preview)");
await call("tools/list", {}, "tools/list (preview)");
await call("tools/call", {
  name: "search_zquas",
  arguments: { query: "AMLR Article 75 cross-institutional", limit: 3 },
}, "tools/call search_zquas");
await call("tools/call", {
  name: "lookup_term",
  arguments: { term: "AMLR Article 75" },
}, "tools/call lookup_term");
await call("tools/call", {
  name: "get_benchmark_numbers",
  arguments: {},
}, "tools/call get_benchmark_numbers");
await call("prompts/list", {}, "prompts/list");
await call("prompts/get", {
  name: "explain_to_head_of_aml",
  arguments: {},
}, "prompts/get explain_to_head_of_aml");

// Probe an unknown method to confirm the error path. -32601 is JSON-RPC
// "Method not found". This is a passing case, not a failure.
await call("does_not_exist", {}, "unknown method (expected error)", {
  expectErrorCode: -32601,
});

console.log("\n=== summary ===");
if (failures > 0) {
  console.log(`${failures} check(s) failed.`);
  process.exitCode = 1;
} else {
  console.log("All checks passed.");
}
