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