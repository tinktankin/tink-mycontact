$(document).on('click', '.remove', function () {
    $(this).closest(".card-view").fadeOut(800, function () {
        $(this).remove();
    });

    // var card = $(this).closest(".card-view").fadeOut(800, function () {
    //     card.remove();
    // });   

    // var car = $(this).closest('.card-view').css({
    //     display: 'none'
    // })
});

$(document).on('click', '.checkmark', function () {
    $(this).closest(".card-view").toggleClass('meeting-done');
});

$(document).ready(function () {
    $('#list').click(function (event) {
        event.preventDefault();
        $('.item').addClass('list-group-item');
        $('.view-group').css({
            padding: '0 0'
        });
    });
    $('#grid').click(function (event) {
        event.preventDefault();
        $('.item').removeClass('list-group-item');
        $('.item').addClass('grid-group-item');
        $('.view-group').css({
            padding: '0 50px'
        });
    });
});

// window.onload = function () {
//     var checked = document.getElementsByClassName("checkmark")

//     checked.addEventListener("click", function () {
//         console.log("clicked")
//     })
// }


// window.onload = function () {

//     var checked = document.querySelector(".checkmark")
//     var title = document.querySelector(".card-view")
//     var done = document.querySelector(".remove")

//     checked.addEventListener('click', function () {
//         title.classList.toggle("meeting-done")
//     })

//     // done.addEventListener('click', function () {
//     //     title.classList.toggle('my-animation')
//     // })
// }


// $(document).ready(function () {
//     $('.card-view').on('click', '.checkmark', function (event) {
//         $('.card-view').toggleClass('meeting-done');
//         event.stopPropagation();
//     });


// $('.card-view').on('click', '.remove', function (event) {
//     console.log("clicked")
//     $(this).fadeOut(500, function () {
//         $(this).remove()
//     })
//     event.stopPropagation();
// });

// })

// $(document).ready(function () {
// $('.meeting-title').on('click', function () {
//     // (this).toggleClass('meeting-done')
//     console.log("clciked")
// })
// })