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

const cursor = document.querySelector(".cursor-inner");
const cursor2 = document.querySelector(".cursor-outer");
document.addEventListener("mousemove", e=>{
    cursor.style.top = e.clientY + "px";
    cursor.style.left = e.clientX + "px";

    cursor2.style.top = e.clientY + "px";
    cursor2.style.left = e.clientX + "px";
})
