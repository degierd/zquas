/* ZQUAS site configuration.
 *
 * VIGIL_ENABLED controls whether the airspace-security (VIGIL) tenant is shown.
 *   false  -> site shows the financial-crime tenant only, exactly as before.
 *             VIGIL homepage section, Solutions dropdown, investor card are hidden,
 *             and /vigil.html redirects to the home page.
 *   true   -> VIGIL content is revealed everywhere and /vigil.html is reachable.
 *
 * THIS FILE IS NOT A GATE. It runs in the browser. A crawler that does not
 * execute JavaScript reads the hidden markup anyway, and previously fetched
 * /vigil.html with a 200. The authoritative gate is VIGIL_ENABLED in
 * cloudflare-worker/wrangler.toml, which removes [data-vigil] elements at the
 * edge and redirects /vigil.html. What remains here is a rendering fallback so
 * the page does not flash gated content before the worker-stripped HTML lands.
 *
 * To turn the tenant on: set VIGIL_ENABLED = true here, set it to "true" in
 * wrangler.toml, then redeploy the worker. Both, or the surface stays hidden.
 */
window.ZQUAS_CONFIG = {
    VIGIL_ENABLED: false
};

(function () {
    var enabled = !!(window.ZQUAS_CONFIG && window.ZQUAS_CONFIG.VIGIL_ENABLED);
    var root = document.documentElement;

    // Gate the standalone VIGIL page: if this is /vigil.html and VIGIL is off,
    // send the visitor to the home page before anything renders.
    if (root.getAttribute('data-vigil-page') === 'true' && !enabled) {
        window.location.replace('/');
        return;
    }

    // Reveal or hide VIGIL-tagged elements once the DOM is ready.
    function apply() {
        var els = document.querySelectorAll('[data-vigil]');
        for (var i = 0; i < els.length; i++) {
            if (enabled) {
                els[i].removeAttribute('hidden');
            } else {
                els[i].setAttribute('hidden', '');
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', apply);
    } else {
        apply();
    }
})();
