document.getElementById("Oxfam").style.display = "none";
document.getElementById("Cancer").style.display = "none";
document.getElementById("Direct").style.display = "none";
document.getElementById("British").style.display = "none";
document.getElementById("Save").style.display = "none";



function secondCharity() {
    var s = document.getElementById("Cancer");
    var x = document.getElementById("Oxfam");
    var a = document.getElementById("Direct");
    var d = document.getElementById("British");
    var n = document.getElementById("Save");

    if (s.style.display === "none") {
        s.style.display = "block";
        x.style.display = "none";
        n.style.display = "none";
        a.style.display = "none";
        d.style.display = "none";
    } else {
        s.style.display = "none";
    }
}

function firstcharity() {
    var x = document.getElementById("Oxfam");
    var s = document.getElementById("Cancer");
    var a = document.getElementById("Direct");
    var d = document.getElementById("British");
    var n = document.getElementById("Save");
    if (x.style.display === "none") {
        x.style.display = "block";
        s.style.display = "none";
        a.style.display = "none";
        n.style.display = "none";
        d.style.display = "none";
    } else {
        x.style.display = "none";
    }
}

function thirdcharity() {
    var a = document.getElementById("Direct");
    var x = document.getElementById("Oxfam");
    var s = document.getElementById("Cancer");
    var d = document.getElementById("British");
    var n = document.getElementById("Save");
    if (a.style.display === "none") {
        a.style.display = "block";
        x.style.display = "none";
        s.style.display = "none";
        d.style.display = "none";
        n.style.display = "none";
    } else {
        a.style.display = "none";
    }
}

function fourthcharity() {
    var d = document.getElementById("British");
    var a = document.getElementById("Direct");
    var x = document.getElementById("Oxfam");
    var s = document.getElementById("Cancer");
    var n = document.getElementById("Save");
    if (d.style.display === "none") {
        d.style.display = "block";
        a.style.display = "none";
        s.style.display = "none";
        x.style.display = "none";
        n.style.display = "none";
    } else {
        d.style.display = "none";
    }
}

function fifthcharity() {
    var n = document.getElementById("Save");
    var a = document.getElementById("Direct");
    var x = document.getElementById("Oxfam");
    var s = document.getElementById("Cancer");
    var d = document.getElementById("British");
    if (n.style.display === "none") {
        n.style.display = "block";
        a.style.display = "none";
        s.style.display = "none";
        x.style.display = "none";
        d.style.display = "none";
    } else {
        n.style.display = "none";
    }
}