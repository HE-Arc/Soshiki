$(document).ready(function(){
    //Smooth the slide when you press on the learn more link
    $('#lm').on('click', function(evt){
        evt.preventDefault();
        var target = $(this).attr('href');
        $('html, body').stop().animate({scrollTop: $(target).offset().top}, 1000 );
    });
    //Make the Tables cards clickable
    $('.tables').click(function () {
        window.location = $(this).parentElement().attr("href");
        return false;
    })
    //Make the add task clickable
    $('.add_task').click(function () {
        window.location = $(this).parentElement().attr("href");
        return false;
    })
});