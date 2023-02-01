const year = document.getElementById("year");
year.textContent = new Date().getFullYear();


document.addEventListener('keydown', (event) => {
    if (event.key === 'k' && (event.ctrlKey || event.metaKey)) {
        event.preventDefault();
        document.querySelector('.form-inline.my-2.my-lg-3 input[type="search"]').focus();
    }
});
const searchInput = document.querySelector('.form-inline.my-2.my-lg-3 input[type="search"]');
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && document.activeElement === searchInput) {
        event.preventDefault();
        searchInput.blur();
    }
});