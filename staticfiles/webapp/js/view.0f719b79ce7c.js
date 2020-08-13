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