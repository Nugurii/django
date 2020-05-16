$(function() {

    $("[data-toggle='tooltip']").tooltip();

    // 解决bootstrap下拉菜单第一次点击无反应问题
    $("[data-toggle='dropdown']").dropdown();

    console.log(window.location.pathname);
    let toggle = window.location.pathname;
    if (toggle == '/user/signin/')
        $("#test1").addClass("active");
    else if (toggle == '/user/signup/')
        $("#test2").addClass("active");

})
