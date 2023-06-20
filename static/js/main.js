const navToggle = document.querySelector(".nav_toggle");
const navMenu = document.querySelector(".nav_menu");

navToggle.addEventListener("click", function() {
  navMenu.classList.toggle("nav_menu-visible");
});
