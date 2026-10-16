// =========================================================
// NIVAD GYM - Mobile navigation
// =========================================================

const menuButton = document.getElementById("menuBtn");
const mainNav = document.getElementById("mainNav");

if (menuButton && mainNav) {
    // Open / close the mobile navigation.
    menuButton.addEventListener("click", () => {
        mainNav.classList.toggle("open");
    });

    // Close the menu after selecting a navigation item.
    mainNav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            mainNav.classList.remove("open");
        });
    });
}
