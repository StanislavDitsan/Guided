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


setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();

}, 3000);