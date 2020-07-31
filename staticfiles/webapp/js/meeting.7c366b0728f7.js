$(document).on('click', '.remove', function () {
    $(this).closest(".card-view").fadeOut(800, function () {
        $(this).remove();
    });
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