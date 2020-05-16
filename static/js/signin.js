$(function () {

    $("#signin").click(function () {
        // let form_data = new FormData();
        // form_data.append('username', $("#username").val());
        // form_data.append('password', $("#password").val());
        let form_data = {
            'username': $("#username").val(),
            'password': $("#password").val()
        }
        $.ajax({
            url: '/user/signin/',
            type: 'POST',
            headers: {"X-CSRFToken": $.cookie("csrftoken")},
            // data: form_data,
            data: JSON.stringify(form_data),
            dataType: 'JSON',
            processData: false,
            // contentType: false,
            contentType: 'application/json; charset=utf-8',
            success: function (args) {
                console.log(args.status, args.msg)
                if (args.status) {
                    window.location.href = '/'
                }
                else {
                    $("#flash-error").show();
                    // $(this).val("Sign in"); // 不起作用
                    // $(this).removeAttr("disabled"); //不起作用
                    $("#signin").val("Sign in");
                    $("#signin").removeAttr("disabled");
                    $("#password").val(""); // password清空
                }
            }
        });
        $(this).val("Signing in...");
        $(this).attr("disabled", true);
    })

    $("#del-message").click(function () {
        $("#flash-error").hide();
    })

    $(document).keydown(function (event) {
        if (event.keyCode == 13) {
            if ($("#username").is(":focus") || $("#password").is(":focus") || $("#signin").is(":focus")){
                $("#signin").click();
                return false;
            }
        }
        return true;
    });
})