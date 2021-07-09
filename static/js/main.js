'use strict';

(function () {
    if ($("#nav-toggle").length) {
        $("#nav-toggle")
            .on("click", function (e) {
                e.preventDefault();
                $("#db-wrapper").toggleClass("toggled");
            });
    }
    feather.replace()
})();