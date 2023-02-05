function searchTable(event) {
    if (event) {
        event.preventDefault();
    }

    const searchTerm = document.getElementById("searchTerm").value.trim().toLowerCase();

    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set("searchTerm", searchTerm);
    window.history.replaceState({}, "", `${window.location.pathname}?${urlParams}`);

    const tableRows = document.querySelectorAll("table tbody tr");
    const similarWords = {
        "windows": ["win-", "winserver"],
        "windows 7": ["win-7"],
        "windows 10": ["win-10"],
        "cisco": ["vios"]
        // Add more search terms and their similar words here
    };

    tableRows.forEach(row => {
        const rowCells = row.querySelectorAll("td");

        let hideRow = true;
        rowCells.forEach(cell => {
            if (cell.cellIndex === 1) {
                return;
            }

            const cellText = cell.textContent.trim().toLowerCase();
            const words = [searchTerm, ...(similarWords[searchTerm] || [])];

            words.forEach(word => {
                if (cellText.indexOf(word) !== -1) {
                    hideRow = false;
                }
            });
        });

        row.style.display = hideRow ? "none" : "table-row";
    });
}


const urlParams = new URLSearchParams(window.location.search);
const searchTerm = urlParams.get("searchTerm");
if (searchTerm) {
    document.getElementById("searchTerm").value = searchTerm;
    searchTable();
}

const visibleRows = document.querySelectorAll("table tbody tr:not([style='display: none;'])");
console.log(visibleRows.length);
if (visibleRows.length === 0) {
    const table = document.querySelector("table");
    const noResultsRow = document.createElement("tr");
    const noResultsCell = document.createElement("td");
    noResultsCell.colSpan = "4";
    noResultsCell.textContent = "No results found";
    noResultsCell.style.textAlign = "center";
    noResultsRow.appendChild(noResultsCell);
    table.querySelector("tbody").appendChild(noResultsRow);
}
