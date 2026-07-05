/* ZQUAS site configuration.
 *
 * VIGIL_ENABLED controls whether the airspace-security (VIGIL) tenant is shown.
 *   false  -> site shows the financial-crime tenant only, exactly as before.
 *             VIGIL homepage section, Solutions dropdown, investor card are hidden,
 *             and /vigil.html redirects to the home page.
 *   true   -> VIGIL content is revealed everywhere and /vigil.html is reachable.
 *
 * Flip this single flag to turn the whole VIGIL surface on or off.
 */
window.ZQUAS_CONFIG = {
    VIGIL_ENABLED: true
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
