document.addEventListener("DOMContentLoaded", function () {
  var nightModeEnabled = localStorage.getItem('nightModeEnabled');

  if (nightModeEnabled === 'true') {
    document.body.classList.add('night-mode');
  }

  document.querySelector('.theme__icon').addEventListener('click', function () {
    document.body.classList.toggle('night-mode');

    var isNightModeEnabled = document.body.classList.contains('night-mode');
    localStorage.setItem('nightModeEnabled', isNightModeEnabled.toString());
  });
});