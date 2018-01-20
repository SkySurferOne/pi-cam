'use strict';
var http = (function ($) {

    var post = function (url, data, callback, onError) {
        $.ajax({
          type: 'POST',
          url: url,
          data: JSON.stringify(data),
          success: callback,
          contentType: "application/json; charset=utf-8",
          dataType: 'json',
          error: function (jqXHR, textStatus, errorThrown) {
            onError();
          }
        });
    };

    var getBlob = function (url, callback, dataType) {
        var request = new XMLHttpRequest();
        request.open("GET", url);
        request.responseType = "blob";

        request.onload = function () {
            var objectURL = URL.createObjectURL(this.response);
            callback(objectURL);
        };
        request.send();
    };

    var get = function(url, callback, dataType, onError) {
        dataType = dataType || 'json';

        if(dataType.indexOf('image') !== -1) {
            getBlob(url, callback, dataType);
        } else {
            $.ajax({
              type: 'GET',
              url: url,
              success: callback,
              dataType: dataType,
              error: function (jqXHR, textStatus, errorThrown) {
                onError();
              }
            });
        }
    };

    return {
        post: post,
        get: get
    }

})(jQuery);