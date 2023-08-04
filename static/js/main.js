const navToggle = document.querySelector(".nav_toggle");
const navMenu = document.querySelector(".nav_menu");
const btnFloat = document.querySelector(".btn_top");

window.addEventListener('scroll', () => {
  const services = document.querySelector('h1');
  const mapServ = services.getBoundingClientRect();
  if (mapServ.top >= -10) {
    btnFloat.classList.add("btn_top-disabled");
  } else {
    btnFloat.classList.remove("btn_top-disabled"); 
  }
});

navToggle.addEventListener("click", function() {
  navMenu.classList.toggle("nav_menu-visible");
});

/*
document.addEventListener('DOMContentLoaded', function(){
  navFixed();
});

function navFixed() {

  const navBar = document.querySelector('.nav_sm');

  // Registrar Intersection Observer
  const observer = new IntersectionObserver( function(entries) {
    if(entries[0].isIntersecting) {
      navBar.classList.remove('nav_sm-fixed');
    } else {
      navBar.classList.add('nav_sm-fixed');      
    };
  });
  // Elemento a obserbar
  observer.observe(document.querySelector('.observe'))
}
*/