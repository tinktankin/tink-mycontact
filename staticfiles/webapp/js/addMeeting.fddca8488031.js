var attendeeList = []

$(document).ready(function () {
    $('input.add-person').on('click', function () {
        var person = $('input.attendee').val()
        attendeeList.push(person) //appending attendees to attendeeList
        $('input.attendee').val("")
        $('.addmeeting-form .form-container ul').append("<li><span><i class='fa fa-trash-o' aria-hidden='true'></i></span>" + person + '</li>')
    })

    $('.addmeeting-form .form-container ul').on('click', 'span', function (event) {
        attendeeList.splice($.inArray($(this).parent().text(), attendeeList), 1) // removing attendee from attendeeList
        $(this).parent().fadeOut(500, function () {
            $(this).remove()
        })
        event.stopPropagation();
    });

    $("input.scheudle").click(function () {
        // Code for getting current working directory -->
        // var scripts = document.querySelectorAll('script[src]');
        // var currentScript = scripts[scripts.length - 1].src;
        // var currentScriptChunks = currentScript.split('/');
        // var currentScriptFile = currentScriptChunks[currentScriptChunks.length - 1];
        // console.log(currentScript.replace(currentScriptFile, ''));

        // Code to save the file -->
        //var textToSave = attendeeList;
        //var hiddenElement = document.createElement('a');

        //hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
        //hiddenElement.target = '_blank';
        //hiddenElement.download = 'Attendees.txt';
        //hiddenElement.click();
    })
});

$(document).on('keyup keypress', 'form input[type="text"]', function (e) {
    if (e.keyCode == 13) {
        e.preventDefault();
        return false;
    }
});