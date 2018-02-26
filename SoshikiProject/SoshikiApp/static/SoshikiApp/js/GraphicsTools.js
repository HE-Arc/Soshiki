$(document).ready(function(){
    $('#lm').on('click', function(evt){
        evt.preventDefault();
        var target = $(this).attr('href');
        $('html, body').stop().animate({scrollTop: $(target).offset().top}, 1000 );
    });
    $('.tables').click(function () {
        window.location = $(this).find("a").attr("href");
        return false;
    })
});