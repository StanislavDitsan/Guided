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