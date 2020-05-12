$(function () {

    let is_username_valid = false;
    let is_password_valid = false;
    
    $("#username").on('input propertychange', function () {
        let pattern = /^[a-zA-Z0-9]+$/;
        let username = $(this).val();
        let message = $("#username-message");
        message.hide();
        // console.log(username, username.length, pattern.test(username));
        $(this).removeClass("is-autocheck-errored");
        $(this).removeClass("is-autocheck-successed");
        $(this).addClass("is-autocheck-loading");
        if (username == '') {
            $(this).removeClass("is-autocheck-loading");
            $(this).removeClass("is-autocheck-errored");
            $(this).removeClass("is-autocheck-successed");
            is_username_valid = false;
            return;
        }
        if (pattern.test(username) == false) {
            $(this).removeClass("is-autocheck-loading");
            $(this).addClass("is-autocheck-errored");
            $(this).removeClass("is-autocheck-successed");
            message.html("Username is not available.");
            message.show();
            is_username_valid = false;
            return;
        }
        if (username.length < 5 || username.length > 39) {
            $(this).removeClass("is-autocheck-loading");
            $(this).addClass("is-autocheck-errored");
            $(this).removeClass("is-autocheck-successed");
            message.html("Username is not available.");
            message.show();
            is_username_valid = false;
            return;
        }
        let form_data = new FormData();
        form_data.append('type', 0);
        form_data.append('username', username);
        that = this;
        $.ajax({
            url: '/user/signup/',
            type: 'POST',
            headers: {"X-CSRFToken": $.cookie("csrftoken")},
            data: form_data,
            dataType: 'JSON',
            processData: false,
            contentType: false,
            success: function (args) {
                console.log(args.status, args.msg)
                if (args.status) {
                    $(that).removeClass("is-autocheck-loading");
                    $(that).removeClass("is-autocheck-errored");
                    $(that).addClass("is-autocheck-successed");
                    is_username_valid = true;
                    if (is_username_valid && is_password_valid)
                        $("#signup").removeAttr("disabled");
                }
                else {
                    $(that).removeClass("is-autocheck-loading");
                    $(that).addClass("is-autocheck-errored");
                    $(that).removeClass("is-autocheck-successed");
                    message.html("Username has been taken.");
                    message.show();
                    is_username_valid = false;
                }
            }
        });
    })

    $("#password").on('input propertychange', function () {
        let password = $(this).val();
        let message = $("#password-message");
        message.hide();
        if (password == '') {
            return;
        }
        if (password.length < 8 || password.length > 128) {
            message.html("Password is not available.");
            message.show();
            is_password_valid = false;
            return;
        }
        is_password_valid = true;
        if (is_username_valid && is_password_valid)
            $("#signup").removeAttr("disabled");
    })

    // $("#signup").click(function () {
    //     let form_data = new FormData();
    //     form_data.append('type', 1);
    //     form_data.append('username', $("#username").val());
    //     form_data.append('password', $("#password").val());
    //     $.ajax({
    //         url: '/user/signup/',
    //         type: 'POST',
    //         headers: {"X-CSRFToken": $.cookie("csrftoken")},
    //         data: form_data,
    //         dataType: 'JSON',
    //         processData: false,
    //         contentType: false,
    //         success: function (args) {
    //             let flash = $("#flash-box");
    //             if (args.status) {
    //                 // flash.show();
    //                 // $("#signup").val("Sign up");
    //                 // $("#password").val("");
    //                 alert("Sign up successfully! now it's going to sign in.");
    //                 window.location.href = '/user/signin/'
    //             }
    //             else {
    //                 // flash.removeClass("signup-flash-success");
    //                 // flash.addClass("signup-flash-error");
    //                 // flash.show();
    //             }
    //         }
    //     });
    //     $(this).attr("disabled", true);
    //     $(this).val("Signing up...")
    // })

    $("#del-flash-message").click(function () {
        $("#flash-box").hide();
    })

    $(document).keydown(function (event) {
        if (event.keyCode == 13) {
            if ($("#username").is(":focus") || $("#password").is(":focus") || $("#signup").is(":focus")){
                $("#signup").click();
                return false;
            }
        }
        return true;
    });
})