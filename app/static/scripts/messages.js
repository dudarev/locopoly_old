function postTweet(){
    var message = $('#message').text();
    showProgress();
    $.post("/twitter/statuses/update", {
              message: message
              },
              function (data) {
                if( data.match(/Success/) ){
                    showSuccess();
                } else {
                    showError();
                }
              }
          );
};

function showProgress(){
    $("#success-message").hide();
    $("#error-message").hide();
    $("#progress-message").show();
};

function showError(){
    $("#progress-message").hide();
    $("#success-message").hide();
    $("#error-message").show();
    setTimeout('$("#error-message").hide("fast")',2000);
};

function showSuccess(){
    $("#progress-message").hide();
    $("#error-message").hide();
    $("#success-message").show();
    setTimeout('$("#success-message").hide("fast")',2000);
};
