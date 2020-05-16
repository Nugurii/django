$(function() {

    $("#date").on('input propertychange', function() {
        let pattern = /^[0-9]{4}[\-][0-9]{2}[\-][0-9]{2}$/;
        let date = $(this).val();
        if (date == '') {
            $(this).removeClass("is-autocheck-errored");
            $(this).removeClass("is-autocheck-successed");
            return;
        }
        if (pattern.test(date) == false) {
            $(this).addClass("is-autocheck-errored");
            $(this).removeClass("is-autocheck-successed");
        } else {
            $(this).removeClass("is-autocheck-errored");
            $(this).addClass("is-autocheck-successed");
        }
    })

})
