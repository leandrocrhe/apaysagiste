// Seleccionar el elemento submenu
var submenu = document.querySelector(".submenu");

// Añadir un evento click al elemento submenu
submenu.addEventListener("click", function(e) {
  
  // Evitar que el enlace se ejecute
  e.preventDefault();
  
  // Seleccionar el elemento ul dentro del submenu
  var ul = submenu.querySelector("ul");
  
  // Alternar la clase visible al elemento ul
  ul.classList.toggle("visible");
});