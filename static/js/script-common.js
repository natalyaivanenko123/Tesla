$(function() {

var header = $('.hby-header'), 
   body = $('body'),
   mainMenu = $('.hby-header-center'),
   mainMenuItem = $('.hby-header-center .menu-item'),
   dropDownMenu = $('.hby-header-main-sections'),
   dropDownMenuItem = $('.hby-header-main-sections .main-section-block'),
   headerBg = $('.header-bg'),
   mobileButton = $('.menu-mobile'),
   profileButton = $('.hby-header-right-item .login-icon.open-profile'),
   tooltipButton = $('.tooltip-btn'),
   tooltipInner = $('.tooltip-item');
   cartButton = $('.cart-icon');
   cartInner = $('.cart-wrapper');

// close all header elements
   function closeAll() {
      header.removeClass('open');
      mainMenu.removeClass('open');
      mainMenuItem.removeClass('active');
      dropDownMenu.removeClass('open');
      dropDownMenuItem.removeClass('active');
      profileButton.removeClass('active');
      mobileButton.parent().removeClass('active');
      body.removeClass('hby-header-open');
      body.removeClass('mobile-menu-open');
   }


// main menu
   mainMenuItem.click(function(e) {
      e.preventDefault();
      let index = $(this).index();
      if(!$(this).hasClass('active') && $(this).siblings().hasClass('active') || $('.login-icon.open-profile').hasClass('active')) {

      } else {
         mainMenu.toggleClass('open');
         dropDownMenu.toggleClass('open');
         header.toggleClass('open');
         // mobileButton.parent().toggleClass('active');
         body.toggleClass('hby-header-open');
         console.log('error 1');
         
      }
      $(this).toggleClass('active').siblings().removeClass('active');
      dropDownMenuItem.eq(index).toggleClass('active').siblings().removeClass('active');
      profileButton.removeClass('active');
      
      // close cart
      cartButton.removeClass('open');
      cartInner.removeClass('open');
   });

   $('.section-items .item-toggler').click(function(e) {
      e.preventDefault();
      $(this).addClass('active');
      $(this).parents('.section-items').find('.item-toggler').not(this).removeClass('active');
      $(this).parents('.section-items').find('.item').removeClass('chosen');
      $(this).siblings('.item').addClass('chosen');
   });

// profile
   profileButton.click(function(e) {
      e.preventDefault();
      if(!$(this).hasClass('active') && $('.hby-header-center .menu-item').hasClass('active')) {

      } else {
         mainMenu.toggleClass('open');
         header.toggleClass('open');
         dropDownMenu.toggleClass('open');
         body.toggleClass('hby-header-open');
         
      }

      if(!$(body).hasClass('mobile-menu-open')) {
         mobileButton.parent().toggleClass('active');
      }

      $(this).toggleClass('active');
      $('.hby-header-main-sections .main-section-block:last-child').toggleClass('active').siblings().removeClass('active');
      mainMenuItem.removeClass('active');
   });

// cart

cartButton.click(function(e) {
      e.preventDefault();
      $(cartInner).toggleClass('open');
      $(this).toggleClass('open');
   });
   

// header-bg
   headerBg.on('click', function() {
      closeAll();
   });

// menu-mobile
   mobileButton.on('click', function() {
      if($(this).parent().hasClass('active')) {
         $(this).parent().removeClass('active');
         closeAll();
      } else {
         $(this).parent().addClass('active');
         body.addClass('mobile-menu-open');
      }
   });

// mobile-arrow 
   $('.arrow-back').on('click', function() {
      $(this).parents('.main-section-block').removeClass('active');
      dropDownMenu.removeClass('open');
      mainMenuItem.removeClass('active');
      header.removeClass('open');
      body.removeClass('hby-header-open');

   });

// tooltip
   tooltipButton.click(function(e) {
      console.log('correct');
      e.stopPropagation()

      if ( $(this).hasClass('open') ) {
         $(this).removeClass('open');
         tooltipInner.removeClass('open');
      
   } else {
         tooltipButton.not(this).removeClass('open');
         $(this).addClass('open');
         tooltipInner.removeClass('open');
         $(this).siblings('.tooltip-item').toggleClass('open');
   }
   });
   
   $(document).click(function (e) {
      if ( !tooltipButton.is(e.target) && !tooltipInner.is(e.target) && tooltipInner.has(e.target).length === 0) {
         tooltipInner.removeClass('open');
         tooltipButton.removeClass('open');
      };
   });
   
   let div = document.querySelector("span[title='33']");
        console.log(div);
        let parent =  div.closest('div.product-price');
        console.log(parent);
        parent.querySelector()

});

