// script.js
document.addEventListener("DOMContentLoaded", function() {
    const searchBar = document.getElementById("search-bar");
    searchBar.addEventListener("input", function() {
        const query = searchBar.value.toLowerCase();
        const content = document.querySelectorAll("h1, h2, h3, h4, h5, h6, p, li");

        content.forEach(function(element) {
            const text = element.textContent.toLowerCase();
            if (text.includes(query)) {
                element.style.display = "block";
            } else {
                element.style.display = "none";
            }
        });
    });
});
