document.addEventListener("DOMContentLoaded", function () {
    const menuLink = document.getElementById("menu-link");
    const submenu = document.getElementById("submenu");

    menuLink.addEventListener("click", function (event) {
        event.preventDefault();
        submenu.classList.toggle("show");
    });
});
