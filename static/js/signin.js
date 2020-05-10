$(function () {

    $("#signin").click(function () {
        let form_data = new FormData();
        form_data.append('username', $("#username").val());
        form_data.append('password', $("#password").val());
        $.ajax({
            url: '/user/signin/',
            type: 'POST',
            headers: {"X-CSRFToken": $.cookie("csrftoken")},
            data: form_data,
            dataType: 'JSON',
            processData: false,
            contentType: false,
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
                    $("#username").removeAttr("disabled");
                    $("#password").val(""); // password清空
                }
            }
        });
        // $("#signin").blur();
        $("#signin").val("Signing in...");
        $("#signin").attr("disabled", true);
        $("#username").attr("disabled", true);
        $("#password").attr("disabled", true);
    })

    // $("#signin").mousedown(function() {
    //     console.log("2333", $(this).hasClass("signin-btn"));
    //     $("#signin").blur();
    // })

    $("#del-message").click(function () {
        $("#flash-error").hide();
    })

    $(document).keydown(function (event) {
        if (event.keyCode == 13) {
            $("#signin").click();
            return false;
        }
        return true;
    });
})