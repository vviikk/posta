

const $ = document.querySelectorAll.bind(document);

if (showHeading) {
    $('#heading')[0].classList.remove('hidden')
}

const fader = (images, timer = 60000, current = 0) => {
    const total = images.length;
    for (let i = 0; i < total; i++) {
        images[i].style.opacity = 0;
        images[i].style.transform = 'translate3d(-50%, 0, 0)'
    }
    images[current].style.opacity = 1;
    images[current].style.transform = 'translate3d(0, 0, 0)';

    const next = (current !== total - 1) ? current + 1 : 0;

    images[next].style.transform = 'translate3d(25%, 0, 0)';


    setTimeout(fader, timer, images, timer, next);
};

fader($('ul.slider li'))