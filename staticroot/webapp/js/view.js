$(document).ready(function () {
    var zindex = 10;

    $("div.card").click(function (e) {
        e.preventDefault();

        var isShowing = false;

        if ($(this).hasClass("show-info")) {
            isShowing = true
        }

        if ($("div.dashboard-cards").hasClass("showing")) {
            $("div.card.show-info")
                .removeClass("show-info");

            if (isShowing) {
                $("div.dashboard-cards")
                    .removeClass("showing");
            } else {
                $(this)
                    .css({
                        zIndex: zindex
                    })
                    .addClass("show-info");

            }

            zindex++;

        } else {
            $("div.dashboard-cards")
                .addClass("showing");
            $(this)
                .css({
                    zIndex: zindex
                })
                .addClass("show-info");

            zindex++;
        }

    });
});

// window.onload = function () {
//     var card = document.getElementsByClassName("card")

//     for (var i = 0; i < card.length; i++) {
//         card[i].addEventListener("click", function () {
//             console.log("clicked")
//             var content = this.nextElementSibling;
//             if (content.style.display === "block") {
//                 content.style.display = "none";
//             } else {
//                 content.style.display = "block";
//             }
//         });
//     }
// }