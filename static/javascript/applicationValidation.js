document.getElementById("error1").style.color = "red";
document.getElementById("error2").style.color = "red";
document.getElementById("error1").style.visibility = "hidden";
document.getElementById("error2").style.visibility = "hidden";

function validateForm() {
    var terms = document.getElementById("termsBox").checked;
    var confirm = document.getElementById("confirmBox").checked;
    if (terms == true && confirm == true) {
        document.getElementById("error1").style.visibility = "hidden";
        document.getElementById("error2").style.visibility = "hidden";
        return true
    } else if (terms == false) {
        document.getElementById("error1").style.visibility = "visible";
        document.getElementById("error2").style.visibility = "hidden";
        return false
    } else if (confirm == false) {
        document.getElementById("error1").style.visibility = "hidden";
        document.getElementById("error2").style.visibility = "visible";
        return false
    } else {
        document.getElementById("error1").style.visibility = "visible";
        document.getElementById("error2").style.visibility = "hidden";
        return false
    }
}