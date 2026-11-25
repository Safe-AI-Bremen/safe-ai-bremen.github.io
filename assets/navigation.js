const menu = document.querySelector('.mobile-menu');
const menuButton = menu.querySelector('summary');

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menu.open) {
    menu.open = false;
    menuButton.focus();
  }
});

document.addEventListener('click', (event) => {
  if (menu.open && !menu.contains(event.target)) menu.open = false;
});

menu.addEventListener('focusout', (event) => {
  if (event.relatedTarget && !menu.contains(event.relatedTarget)) menu.open = false;
});

window.matchMedia('(min-width: 821px)').addEventListener('change', (event) => {
  if (event.matches) menu.open = false;
});
