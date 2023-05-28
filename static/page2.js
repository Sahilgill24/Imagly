var swiper = new Swiper(".blog-slider", {
    loop: true,
    slidesPerView: "1",
    speed: 500,
    effect: "coverflow",
    coverflowEffect: {
        slideShadows: false,
    },
    mousewheel: {
        invert: false,
    },
    autoplay: {
        delay: 3000,
    },
    breakpoints: {
        0: {
            effect: "slide",
            centeredSlides: false,
        },
        768: {
            slidesPerView: "2",
            centeredSlides: true,
        },
        1200: {
            slidesPerView: "3",
            centeredSlides: true,
        }
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "fraction"
    },

});

