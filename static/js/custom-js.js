let prevScrollpos = window.pageYOffset;
const navbar = document.getElementById("mainNav");

window.onscroll = function() {
  const currentScrollPos = window.pageYOffset;

  if (prevScrollpos > currentScrollPos) {
    navbar.style.top = "0";
  } else {
    navbar.style.top = `-${navbar.offsetHeight}px`;
  }

  prevScrollpos = currentScrollPos;
}
