# Deploy mcp.zquas.ai

This is the MCP knowledge server. Hosts ZQUAS content as MCP resources,
tools, and prompts. Public, no auth.

## Three steps

### 1. Add a DNS record for mcp.zquas.ai

Cloudflare dashboard -> zquas.ai -> DNS -> Records -> Add record.

- Type: **AAAA**
- Name: **mcp**
- IPv6 address: **100::** (any address; the Worker route takes precedence)
- Proxy status: **Proxied** (orange cloud)
- TTL: Auto

Save. The DNS record is needed because Cloudflare will not bind a Worker
route to a hostname that has no DNS entry.

(Alternative: the Worker's `*.workers.dev` URL works without DNS, but the
custom domain looks more professional and matches the server card.)

### 2. Deploy the Worker

```
cd mcp-server
npm install
npx wrangler deploy
```

Wrangler reads `wrangler.toml`, bundles `src/worker.js` and the search
index, uploads it, and binds `mcp.zquas.ai/*`. Output ends with
`Current Version ID: <uuid>`.

### 3. Verify

```
# Health check
curl https://mcp.zquas.ai/health

# Server card from the MCP origin
curl https://mcp.zquas.ai/.well-known/mcp/server-card.json | head -20

# Server card from the main site (already deployed)
curl https://zquas.ai/.well-known/mcp/server-card.json | head -20

# MCP initialize
curl -X POST https://mcp.zquas.ai/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18"}}'

# List resources
curl -X POST https://mcp.zquas.ai/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":2,"method":"resources/list"}'

# List tools
curl -X POST https://mcp.zquas.ai/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/list"}'

# Call the search tool
curl -X POST https://mcp.zquas.ai/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"search_zquas","arguments":{"query":"AMLR Article 75"}}}'

# Call the benchmark tool
curl -X POST https://mcp.zquas.ai/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"get_benchmark_numbers"}}'
```

You should get well-formed JSON-RPC responses for each.

## Connecting from Claude Desktop

1. Claude Desktop -> Settings -> Developer -> Edit Config.
2. Open the `claude_desktop_config.json` that opens in your editor.
3. Add this entry under `mcpServers`:

```json
{
  "mcpServers": {
    "zquas-knowledge": {
      "url": "https://mcp.zquas.ai/mcp"
    }
  }
}
```

4. Save the file. Restart Claude Desktop.
5. In a new conversation, look for the MCP indicator (paperclip or
   plug icon) -> ZQUAS Knowledge should appear with the resources,
   tools, and prompts listed.
6. Ask something like "What does AMLR Article 75 require?" - Claude
   will use the `lookup_term` and `search_zquas` tools and cite
   ZQUAS sources.

## Updating

When site content changes:

```
python rebuild_artifacts.py     # rebuilds the .md twins
python mcp-server/build_index.py # rebuilds the search index
cd mcp-server && npx wrangler deploy
```

`rebuild_artifacts.py` runs `build_index.py` automatically as part of
its sequence, so the manual second command is redundant if you ran the
first.

## Costs

Cloudflare Workers free tier: 100,000 requests per day, 10ms CPU per
request. The server stays well inside both limits even with steady MCP
traffic. Free.

## Tail logs

```
cd mcp-server
npx wrangler tail
```

Streams every request with status, latency, and any console output.

## What it does NOT do

- Live system telemetry. The server returns published facts and content
  only. It cannot tell anyone how many transactions ZQUAS is processing
  right now, who its customers are, or anything that is not already
  public on https://zquas.ai.
- Authentication. There are no protected resources. Adding auth was
  considered and explicitly skipped: the goal is removing friction
  between an AI agent and the public ZQUAS material.
- Vector search. Keyword search over the section-level corpus is fast,
  deterministic, and free per query. Embeddings can be added later if
  the search quality stops being good enough.
