function searchTable(event) {
    if (event) {
        event.preventDefault();
    }
    const searchTerm = document.getElementById("searchTerm").value.toLowerCase();


    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set("searchTerm", searchTerm);
    window.history.replaceState({}, "", `${window.location.pathname}?${urlParams.toString()}`);

    const tableRows = document.querySelectorAll("table tbody tr");
    for (let i = 0; i < tableRows.length; i++) {
        const row = tableRows[i];
        const rowCells = row.querySelectorAll("td");

        let hideRow = true;
        for (let j = 0; j < rowCells.length; j++) {
            const cell = rowCells[j];
            if (j === 1) {
                continue;
            }

            const similarWords = {
                "windows": ["win-", "win-7", "winserver"],
                // Add more search terms and their similar words here
            };
            const words = similarWords[searchTerm.toLowerCase()] || [];
            words.push(searchTerm.toLowerCase());

            const cellText = cell.textContent.toLowerCase();
            for (let k = 0; k < words.length; k++) {
                if (cellText.indexOf(words[k]) !== -1) {
                    hideRow = false;
                    break;
                }
            }

            if (cell.textContent.toLowerCase().indexOf(searchTerm) !== -1) {
                hideRow = false;
                break;
            }
        }

        if (hideRow) {
            row.style.display = "none";
        } else {
            row.style.display = "table-row";
        }
    }
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
