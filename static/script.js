"use strict";
tns({
    container: '.slider',
    items: 1,
    slideBy: 'page',
    autoplay: true,
    mode: 'gallery',
    nav: false,
    controls: false,
    autoplayButtonOutput: false,
    autoplayTimeout: 1000 * 60,
    fixedWidth: window.innerWidth - 50,
});

const refresh = () => {
    console.log('Refreshing...')
    window.location.reload()
}

const interval = setInterval(refresh, 1000 * 60 * 10) // Hard refresh every 10 mins