// window.onload = function () {
//     // hightlighting the selected
//     var container = document.getElementById("btnContainer");
//     var btns = document.getElementsByClassName("btn");
//     for (var i = 0; i < btns.length; i++) {
//         btns[i].addEventListener("click", function () {
//             var current = document.getElementsByClassName("active");
//             current[0].className = current[0].className.replace(" active", "");
//             this.className += " active";
//         });
//     }
// }

// // Get the elements with class="column"
// var elements = document.getElementsByClassName("card");

// // Declare a loop variable
// var i;

// // List View
// function listView() {

// }

// // Grid View
// function gridView() {
//     for (i = 0; i < elements.length; i++) {
//         elements[i].style.width = "25%";
//     }
// }

$(document).ready(function () {
    $('#list').click(function (event) {
        event.preventDefault();
        $('.item').addClass('list-group-item');
    });
    $('#grid').click(function (event) {
        event.preventDefault();
        $('.item').removeClass('list-group-item');
        $('.item').addClass('grid-group-item');
    });
});