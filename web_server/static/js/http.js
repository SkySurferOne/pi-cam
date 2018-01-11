'use strict';
var http = (function ($) {

    var post = function (url, data, callback) {
        $.ajax({
          type: 'POST',
          url: url,
          data: JSON.stringify(data),
          success: callback,
          contentType: "application/json; charset=utf-8",
          dataType: 'json'
        });
    };

    return {
        post: post
    }
})(jQuery);