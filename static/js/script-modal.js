$(function() {

    // modal
    var $modal = $('.hby-modal'),
      $modalButtonShowAuth = $('.hby-button-open-auth'),
      $modalButtonShowForget = $('.hby-button-open-forget'),
      $modalButtonShowReg = $('.hby-button-fast-reg'),
      $modalButtonShowRegSuccess = $('.hby-button-reg-success'),
      $modalBackground = $('.hby-modal .hby-modal-bg'),
      $modalButtonClose = $('.hby-modal .hby-modal-close');

    function closeModal() {
      $('body').removeClass('hby-modal-open');
      $modal.fadeOut();
      $modalBackground.fadeOut();
    }
    $modalButtonClose.click(function(e) {
      e.preventDefault();
      closeModal();
    });
    $modalBackground.click(function(e) {
      e.preventDefault();
      closeModal();
    });
    $modalButtonShowAuth.click(function(e) {
      e.preventDefault();
      $('body').addClass('hby-modal-open');
      $('.hby-modal.auth-modal').fadeIn();
      $modalBackground.fadeIn();
      $('.hby-modal.forget-modal').fadeOut();
      $('.hby-modal.fast-reg-modal').fadeOut();
    });
    $modalButtonShowForget.click(function(e) {
      e.preventDefault();
      $('body').addClass('hby-modal-open');
      $('.hby-modal.forget-modal').fadeIn();
      $modalBackground.fadeIn();
      $('.hby-modal.auth-modal').fadeOut();
    });
    $modalButtonShowReg.click(function(e) {
      e.preventDefault();
      $('body').addClass('hby-modal-open');
      $('.hby-modal.fast-reg-modal').fadeIn();
      $modalBackground.fadeIn();
      $('.hby-modal.auth-modal').fadeOut();
    });
    $modalButtonShowRegSuccess.click(function(e) {
      e.preventDefault();
      $('body').addClass('hby-modal-open');
      $('.hby-modal.success-modal').fadeIn();
      $modalBackground.fadeIn();
      $('.hby-modal.fast-reg-modal').fadeOut();
    });
  });