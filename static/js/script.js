const data = new Date().getFullYear()
const para = document.getElementById("year")
para.innerHTML = data

document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const navbarBurger = document.getElementById('navbarBurger');
  const navbarMenu = document.getElementById('navbarMenu');

  // Check if there are any navbar burgers
  if (navbarBurger) {
    // Add a click event on the navbar burger icon
    navbarBurger.addEventListener('click', () => {
      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      navbarBurger.classList.toggle('is-active');
      navbarMenu.classList.toggle('is-active');
    });
  }
});
