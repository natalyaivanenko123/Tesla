$(function() {


    // show-pass изменённый старый скрипт

    $('.hby-form .show-pass').on('click', function (e) {
      e.preventDefault();
      var type = $(this).closest('.hby-form-item').find('input').attr('type') == "text" ? "password" : 'text',
          text = $(this).attr('title') == "Скрыть пароль" ? "Показать пароль" : "Скрыть пароль";
      $(this).attr('title', text).toggleClass('show');
      $(this).closest('.hby-form-item').find('input').prop('type', type);
    });

    // показать поле с email для авторизации

    $('.other-user').on('click', function (e) {
      e.preventDefault();
      $(this).parent().css('display', 'none');
      $('.auth-email').css('display', 'block');
    });

    // select
    $('.fast-reg-select').selectric({
      arrowButtonMarkup: '<span class="select-icon icon-arrow-down"></span>',
      disableOnMobile: false,
      nativeOnMobile: false,
      labelBuilder: '{text}',
      optionsItemBuilder: '<p class="hby-text">{text}</p>',
    });
    var selectCheck = $('.selectric-fast-reg-select').find('li');
    $(selectCheck).click(function(e) {
      $(this).find("input[type='checkbox']").prop("checked", function(i, val) {
        return !val;
      })
    })
    $('.fast-reg-select').on('selectric-change', function(event, element, selectric) {
      let selectNumber = $('.selectric-items ul li.selected').index() - 1;
      $('.form-client-body .client').eq(selectNumber).addClass('selected').siblings().removeClass('selected');
    });
  });