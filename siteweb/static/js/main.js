const navToggle = document.querySelector(".nav_toggle");
const navMenu = document.querySelector(".nav_menu");
const btnFloat = document.querySelector(".btn_top");

document.addEventListener('DOMContentLoaded', () => {
  const url = window.location.href;
  const links = document.querySelectorAll('.nav_link a');

  links.forEach(link => link.classList.toggle('active', link.href === url));
});

window.addEventListener('scroll', () => {
  const services = document.querySelector('h1');
  const mapServ = services.getBoundingClientRect();
  btnFloat.classList.toggle("btn_top-disabled", mapServ.top > -10);
});

navToggle.addEventListener("click", () => {
  navMenu.classList.toggle("nav_menu-visible");
});

ScrollReveal().reveal('.nav', {
  duration: 3000,
  origin: 'bottom',
  distance: '-68px' 
});
ScrollReveal().reveal('.banner_text', {
  duration: 3000,
  origin: 'bottom',
  distance: '68px' 
});
ScrollReveal().reveal('.section_titles', {
  duration: 3000,
  origin: 'bottom',
  distance: '50px' 
});
ScrollReveal().reveal('.section_container-warranty', {
  // delay: 500,
  duration: 3000,
});
ScrollReveal().reveal('.scroll_card_left', {
  delay: 500,
  duration: 3000,
  origin: 'right',
  distance: '100px' 
});
ScrollReveal().reveal('.scroll_card_right', {
  delay: 500,
  duration: 3000,
  origin: 'right',
  distance: '100px' 
});
ScrollReveal().reveal('.services_galery', {
  delay: 500,
  duration: 2000,  
  origin: 'bottom',
  distance: '100px' 
});
ScrollReveal().reveal('.testimonials_container', {
  delay: 100,
  duration: 3000,
  origin: 'bottom',
  distance: '50px' 
});
ScrollReveal().reveal('.section_about', {
  duration: 2000,
  origin: 'bottom',
  distance: '100px' 
});
ScrollReveal().reveal('.service_texts', {
  delay: 500,  
  origin: 'right',
  distance: '100px'
});
ScrollReveal().reveal('.service_picture', {
  delay: 500,  
  origin: 'left',
  distance: '100px'
});
// ScrollReveal().reveal('.gallery', {
//   delay: 500, 
//   duration: 2000, 
//   origin: 'bottom',
//   distance: '100px'
// });
ScrollReveal().reveal('.flex1', {
  delay: 100,
  duration: 3000,
  origin: 'left',
  distance: '100px' 
});
ScrollReveal().reveal('.flex2', {
  delay: 100,
  duration: 3000,
  origin: 'rigth',
  distance: '100px' 
});

ScrollReveal().reveal('.contact-container', {delay: 500});


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