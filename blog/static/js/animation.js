var lastScrollTop = 0;
var delta = 5; // 동작의 구현이 시작되는 위치
var headerHeight = $('header').outerHeight(); // 영향을 받을 요소를 선택
var didScroll;

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();

    if(Math.abs(lastScrollTop - st) <= delta)
        return;

    if (st > lastScrollTop && st > headerHeight){
        // Scroll Down
        $('header').removeClass('header-down').addClass('header-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('header').removeClass('header-up').addClass('header-down');
        }
    }

    lastScrollTop = st;
}