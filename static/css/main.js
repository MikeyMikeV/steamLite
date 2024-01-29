$(document).ready(function () {
    $('.sliders').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: ".sliders-two",
        responsive: [

        ]
    }) 

    $('.sliders-two').slick({
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        arrows: false,
        centerMode: true,
        centerPadding: '60px',
        LeftPadding: '0',
        focusOnSelect: true,
        asNavFor: ".sliders",
        autoplay: true,
        autoplaySpeed: 2000,
        
    
    })

});



        // prevArrow: '<button class="btn slider-btn slider-prev"><img src="img/arrow-left-solid.svg" alt=""></button>',
        // nextArrow: '<button class="btn slider-btn slider-next"><img src="img/arrow-right-solid.svg" alt=""></button>',

// $(document).ready(function  () {
//     $('.sliders').slick()
// });