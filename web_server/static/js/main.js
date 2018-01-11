'use strict';
(function ($, http) {
    var apiBaseURL = window.location.origin + '/';
    var endoints = {
        EFFECT_BUNDLE: apiBaseURL + 'effect-bundle'
    };
    var $effectBtns;

    var onReady = function () {
        console.log('Heloo!');

        $effectBtns = $('.effect-btn');

        initEvents();
    };

    var effectBtnsOnClick = function (e) {
        var effectName = $(this).attr('data-effect-name');
        var data = {
            name: effectName
        };

        http.post(endoints.EFFECT_BUNDLE, data, function (data) {
              console.log(data);
        });
    };

    var initEvents = function () {
        $effectBtns.click(effectBtnsOnClick);
    };

    $(document).ready(onReady());

})(jQuery, http);
