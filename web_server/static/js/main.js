'use strict';
(function ($, http) {
    var apiBaseURL = window.location.origin + '/';
    var endoints = {
        EFFECT_BUNDLE: apiBaseURL + 'effect-bundle',
        MAKE_PHOTO: apiBaseURL + 'photo',
        GET_PHOTO: apiBaseURL + 'photo/',
        SEND_PHOTO_TO_MAIL: apiBaseURL + 'mail/photo/'
    };
    var photoModalOptions = {};

    var $effectBtns;
    var $photoModal;
    var $makePhotoBtn;
    var $capturedPhoto;
    var $sendPhotoBtn;
    var currentPhotoName;
    var $alerts;
    var $successAlert;
    var $errorAlert;
    var $warningAlert;

    var onReady = function () {
        $effectBtns = $('.effect-btn');
        $photoModal = $('#photo-modal');
        $makePhotoBtn = $('#make-photo-btn');
        $capturedPhoto = $('#captured-photo');
        $sendPhotoBtn = $('#send-photo-btn');
        $alerts = $('.alert');
        $successAlert = $('#success-alert');
        $errorAlert = $('#error-alert');
        $warningAlert = $('#warning-alert');

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
        $alerts.hide();

        // todo make promises
        http.get(endoints.MAKE_PHOTO, function(data) {
            if (data.name) {
                var photoName = data.name;
                http.get(endoints.GET_PHOTO + photoName, function (image) {
                    $capturedPhoto.attr('src', image);
                    $($photoModal).modal(photoModalOptions);
                    currentPhotoName = photoName;
                }, 'image/jpg');
            }

            $($photoModal).modal(photoModalOptions);
        }, 'json');
    };

    var onSendPhotoBtnClick = function () {
        var email = $('#email').val();

        if (email !== '') {
            var data = {
                email: email
            };

            if (currentPhotoName) {
                http.post(endoints.SEND_PHOTO_TO_MAIL + currentPhotoName, data, function (data) {
                    $alerts.hide();
                    $successAlert.show();
                }, function () {
                    $alerts.hide();
                    $errorAlert.show();
                });
            } else {
                console.error('currentPhotoName is null');
            }
        } else {
            console.log('You have to write email');
            $alerts.hide();
            $warningAlert.show();
        }
    };

    var initEvents = function () {
        $effectBtns.click(effectBtnsOnClick);
        $makePhotoBtn.click(onMakePhotoBtnClick);
        $sendPhotoBtn.click(onSendPhotoBtnClick);
    };

    $(document).ready(onReady());

})(jQuery, http);
