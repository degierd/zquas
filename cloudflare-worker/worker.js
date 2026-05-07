/**
 * zquas.ai edge worker
 *
 * Adds:
 *   1. RFC 8288 Link response headers on every HTML response, advertising
 *      llms.txt, facts.json, sitemap, feed, agent-skills, api-catalog.
 *   2. Markdown for Agents content negotiation: when a request to an
 *      .html page sends `Accept: text/markdown`, return the .md twin
 *      with `Content-Type: text/markdown`.
 *
 * Routes (configure in Cloudflare): zquas.ai/*
 *
 * Behaviour:
 *   - Static origin remains GitHub Pages. Worker fetches from origin and
 *     mutates the response headers.
 *   - Pre-existing response headers are preserved; we only add and (for
 *     markdown) replace where appropriate.
 *
 * Deployment:
 *   1. Cloudflare dashboard -> Workers & Pages -> Create -> "Hello world"
 *      template -> paste this file's contents -> Deploy.
 *   2. Add a route: zone zquas.ai, route `*zquas.ai/*`.
 *   3. Confirm via:
 *        curl -I https://zquas.ai/                      (Link header present)
 *        curl -H "Accept: text/markdown" -I https://zquas.ai/article-75.html
 *          (Content-Type: text/markdown)
 */

const LINK_HEADER = [
  '</llms.txt>; rel="describedby"; type="text/plain"',
  '</llms-full.txt>; rel="describedby"; type="text/plain"',
  '</facts.json>; rel="describedby"; type="application/json"',
  '</.well-known/agent-skills/index.json>; rel="agent-skills"',
  '</.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json"',
  '</sitemap.xml>; rel="sitemap"; type="application/xml"',
  '</feed.xml>; rel="alternate"; type="application/rss+xml"; title="ZQUAS Articles"',
  '</atom.xml>; rel="alternate"; type="application/atom+xml"; title="ZQUAS Articles"',
  '</glossary.html>; rel="glossary"',
  '</.well-known/security.txt>; rel="security-policy"',
].join(', ');

export default {
  /**
   * @param {Request} request
   * @param {object} env
   * @param {ExecutionContext} ctx
   */
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const accept = request.headers.get('accept') || '';

    // 1. Markdown content negotiation.
    //    If the client wants markdown and the request is for an HTML
    //    page (or the bare site root), serve the .md twin.
    const wantsMarkdown = accept.toLowerCase().includes('text/markdown');
    if (wantsMarkdown) {
      const mdPath = htmlPathToMarkdown(url.pathname);
      if (mdPath) {
        const mdUrl = new URL(mdPath, url);
        const mdResponse = await fetch(mdUrl.toString(), {
          headers: { 'user-agent': request.headers.get('user-agent') || 'zquas-edge' },
        });
        if (mdResponse.ok) {
          const headers = new Headers(mdResponse.headers);
          headers.set('content-type', 'text/markdown; charset=utf-8');
          headers.set('vary', 'accept');
          headers.set('link', LINK_HEADER);
          return new Response(mdResponse.body, {
            status: mdResponse.status,
            statusText: mdResponse.statusText,
            headers,
          });
        }
        // If the .md twin is missing for some reason, fall through to HTML.
      }
    }

    // 2. Default flow: fetch origin, fix MIME types where GitHub Pages
    //    is wrong, add Link header on HTML, set Vary so caches do not
    //    mix Markdown and HTML responses.
    const originResponse = await fetch(request);
    const contentType = originResponse.headers.get('content-type') || '';
    const isHtml = contentType.toLowerCase().includes('text/html');

    const headers = new Headers(originResponse.headers);

    // MIME type overrides. GitHub Pages serves these as text/plain or
    // application/octet-stream; the right type matters for clients.
    const mimeOverride = mimeForPath(url.pathname);
    if (mimeOverride) {
      headers.set('content-type', mimeOverride);
    }

    if (isHtml) {
      headers.set('link', LINK_HEADER);
      // Tell caches that response varies with Accept (markdown negotiation)
      const existingVary = headers.get('vary');
      if (!existingVary) {
        headers.set('vary', 'accept');
      } else if (!/(^|,\s*)accept(\s*,|$)/i.test(existingVary)) {
        headers.set('vary', `${existingVary}, accept`);
      }
    }

    return new Response(originResponse.body, {
      status: originResponse.status,
      statusText: originResponse.statusText,
      headers,
    });
  },
};

/**
 * Override Content-Type for paths where GitHub Pages defaults are wrong.
 * Returns the correct type, or null to leave the origin's value alone.
 */
function mimeForPath(pathname) {
  if (pathname === '/.well-known/api-catalog') {
    return 'application/linkset+json; charset=utf-8';
  }
  if (pathname === '/feed.xml') {
    return 'application/rss+xml; charset=utf-8';
  }
  if (pathname === '/atom.xml') {
    return 'application/atom+xml; charset=utf-8';
  }
  if (pathname.endsWith('.md')) {
    return 'text/markdown; charset=utf-8';
  }
  return null;
}

/**
 * Map an HTML request path to its Markdown twin path.
 * Returns null if no twin should be served.
 *   /                  -> /index.md
 *   /article-75.html   -> /article-75.md
 *   /article-75        -> /article-75.md (extensionless)
 *   /assets/x.png      -> null (not HTML)
 */
function htmlPathToMarkdown(pathname) {
  if (pathname === '/' || pathname === '') return '/index.md';
  if (pathname.endsWith('.html')) return pathname.slice(0, -5) + '.md';
  // Static assets we never want to MD-negotiate
  if (/\.(png|jpe?g|webp|svg|ico|css|js|json|xml|txt|pdf|woff2?|webmanifest)$/i.test(pathname)) {
    return null;
  }
  // Bare extensionless path: try to map to .md
  if (!pathname.includes('.')) return pathname + '.md';
  return null;
}
