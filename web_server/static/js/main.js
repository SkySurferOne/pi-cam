'use strict';
(function ($, http) {
    var apiBaseURL = window.location.origin + '/';
    var endoints = {
        EFFECT_BUNDLE: apiBaseURL + 'effect-bundle'
    };
    var photoModalOptions = {};

    var $effectBtns;
    var $photoModal;
    var $makePhotoBtn;

    var onReady = function () {
        $effectBtns = $('.effect-btn');
        $photoModal = $('#photo-modal');
        $makePhotoBtn = $('#make-photo-btn');

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

    var onMakePhotoBtnClick = function () {
      $($photoModal).modal(photoModalOptions);
    };

    var initEvents = function () {
        $effectBtns.click(effectBtnsOnClick);
        $makePhotoBtn.click(onMakePhotoBtnClick);
    };

    $(document).ready(onReady());

})(jQuery, http);
