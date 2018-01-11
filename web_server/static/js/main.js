'use strict';
(function ($, http) {
    var apiBaseURL = window.location.origin + '/';
    var endoints = {
        EFFECT_BUNDLE: apiBaseURL + 'effect-bundle',
        MAKE_PHOTO: apiBaseURL + 'photo',
        GET_PHOTO: apiBaseURL + 'photo/'
    };
    var photoModalOptions = {};

    var $effectBtns;
    var $photoModal;
    var $makePhotoBtn;
    var $capturedPhoto;

    var onReady = function () {
        $effectBtns = $('.effect-btn');
        $photoModal = $('#photo-modal');
        $makePhotoBtn = $('#make-photo-btn');
        $capturedPhoto = $('#captured-photo');

        initEvents();
    };

    var effectBtnsOnClick = function () {
        var effectName = $(this).attr('data-effect-name');
        var data = {
            name: effectName
        };

        http.post(endoints.EFFECT_BUNDLE, data, function (data) {});
    };

    var onMakePhotoBtnClick = function () {
        // todo make promises
        http.get(endoints.MAKE_PHOTO, function(data) {
            if (data.name) {
                var photoName = data.name;
                http.get(endoints.GET_PHOTO + photoName, function (image) {
                    $capturedPhoto.attr('src', image);
                    $($photoModal).modal(photoModalOptions);
                }, 'image/jpg');
            }

            $($photoModal).modal(photoModalOptions);
        }, 'json');
    };

    var initEvents = function () {
        $effectBtns.click(effectBtnsOnClick);
        $makePhotoBtn.click(onMakePhotoBtnClick);
    };

    $(document).ready(onReady());

})(jQuery, http);
