$(document).ready(function () {
    $('input.add-person').on('click', function () {
        var person = $('input.attendee').val()
        $('input.attendee').val("")
        $('.addmeeting-form .form-container ul').append("<li><span><i class='fa fa-trash-o' aria-hidden='true'></i></span> " + person + '</li>')
    })

    $('.addmeeting-form .form-container ul').on('click', 'span', function (event) {
        $(this).parent().fadeOut(500, function () {
            $(this).remove()
        })
        event.stopPropagation();
    });


});

$(document).on('keyup keypress', 'form input[type="text"]', function (e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        return false;
    }
});