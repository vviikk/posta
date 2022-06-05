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