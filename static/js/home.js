(function($) {
    "use strict";

    //---------------------------------------------
    //Nivo slider
    //---------------------------------------------
    $('#ensign-nivoslider').nivoSlider({
        effect: 'random',
        slices: 15,
        boxCols: 8,
        boxRows: 4,
        animSpeed: 500,
        pauseTime: 6000,
        startSlide: 0,
        directionNav: true,
        controlNavThumbs: false,
        pauseOnHover: false,
        controlNav: false,
        prevText: '<i class="sp-angle-left"></i>',
        nextText: '<i class="sp-angle-right"></i>'
    });

})(jQuery);
(function($) {

    "use strict";

    //Hide Loading Box (Preloader)
    function handlePreloader() {
        if ($('.loader-wrap').length) {
            $('.loader-wrap').delay(1000).fadeOut(500);
        }
        TweenMax.to($(".loader-wrap .overlay"), 1.2, {
            force3D: true,
            left: "100%",
            ease: Expo.easeInOut,
        });
    }

    if ($(".preloader-close").length) {
        $(".preloader-close").on("click", function() {
            $('.loader-wrap').delay(200).fadeOut(500);
        })
    }
})