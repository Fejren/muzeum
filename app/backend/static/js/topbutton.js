mybutton = document.getElementById("myBtn");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  document.body.scrollTop > 20 || document.documentElement.scrollTop > 20 ?
    mybutton.style.display = "block" :
    mybutton.style.display = "none";
}

function topFunction() {
  document.body.scrollTop = 0; // Safari
  document.documentElement.scrollTop = 0; // Chrome, Firefox, IE and Opera
}