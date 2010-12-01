function showProgress(){
    $("#success-message").hide();
    $("#error-message").hide();
    $("#progress-message").show("fast");
    setTimeout('showError()',1500);
};

function showError(){
    $("#progress-message").hide();
    $("#success-message").hide();
    $("#error-message").show();
    setTimeout('showSuccess()',1500);
};

function showSuccess(){
    $("#progress-message").hide();
    $("#error-message").hide();
    $("#success-message").show();
    setTimeout('$("#success-message").hide("fast")',1500);
};
