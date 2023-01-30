$(document).ready(function () {
  var docHeight = $(window).height();
  var footerHeight = $('#footer').height();
  var footerTop = $('#footer').position().top + footerHeight;
  if (footerTop < docHeight) {
    $('#footer').css('margin-top', (docHeight - footerTop) + 'px');
  }
});

setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();

}, 3000);

function autoType(element, delay) {
  var p = document.querySelector(element);
  var i = 0;
  var text = p.textContent;
  p.textContent = "";

  function type() {
    if (i < text.length) {
      p.textContent += text.charAt(i);
      i++;
      setTimeout(type, delay);
    }
  }

  setTimeout(type, delay);
}

autoType('.type-script', 100);