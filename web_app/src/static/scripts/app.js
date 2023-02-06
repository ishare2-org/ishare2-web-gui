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

let headerCells = document.querySelectorAll('th');
headerCells.forEach(cell => {
    cell.addEventListener('click', function () {
        sortTable(cell.cellIndex);
    });
});

function sortTable(columnIndex) {
    let table = document.querySelector('table');
    let rows = Array.from(table.rows).slice(1);

    // Sort the rows based on the content of the selected column
    rows.sort(function (a, b) {
        let valueA = a.cells[columnIndex].textContent;
        let valueB = b.cells[columnIndex].textContent;

        // Check if the values are numbers
        valueA = isNaN(parseFloat(valueA)) ? valueA.toLowerCase() : parseFloat(valueA);
        valueB = isNaN(parseFloat(valueB)) ? valueB.toLowerCase() : parseFloat(valueB);

        if (valueA < valueB) {
            return -1;
        }
        if (valueA > valueB) {
            return 1;
        }
        return 0;
    });

    // Remove the current rows from the table
    rows.forEach(row => {
        table.deleteRow(row.rowIndex);
    });

    // Re-add the sorted rows to the table
    rows.forEach(row => {
        table.appendChild(row);
    });
    updateTableStyles();
}


function updateTableStyles() {
    let table = document.querySelector('table');
    let rows = Array.from(table.rows).slice(1);

    // Remove the existing styles from the table rows
    rows.forEach(row => {
        row.classList.remove('table-active');
        row.classList.remove('table-secondary');
    });

    // Add the new styles to the table rows
    rows.forEach((row, index) => {
        if (index % 2 === 0) {
            row.classList.add('table-active');
        } else {
            row.classList.add('table-secondary');
        }
    });
}
