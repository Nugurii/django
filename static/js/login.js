window.onload = function() {
    let username = document.getElementById("username")
    let password = document.getElementById("password")
    let submit = document.getElementById("signin")

    document.onkeydown = function(event) {
        if (event.keyCode === 13) {
            submit.click();
            // submit.disabled = "true";
            // submit.value = "Signing in...";
            // username.disabled = "true";
            // password.disabled = "true";
            return false;
        }
        return true;
    }
}