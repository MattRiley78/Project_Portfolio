// import the data from data.js
const tableData = data;
// Reference the HTML table using D3
var tbody = d3.select("tbody");
// Create function to build table.
function buildTable(data) {
    // Clear existing data
    tbody.html("");
    // build forEach loop
    data.forEach((dataRow) => {
        // Append a row to the table body
        let row = tbody.append("tr");
        // Loop through each field in the dataRow
        Object.values(dataRow).forEach((val) => {
            // add each value as a table cell
            let cell = row.append("td");
            cell.text(val);
        });
    });
};
// New function to handle filter.
function handleClick() {
    // Grab the datetime value from the filter
    let date = d3.select("#datetime").property("value");
    // Set default filter
    let filteredData = tableData;
    // Check to see if a date was entered and filter that data using that date.
    if (date) {
        // Apply `filter` to the table data
        // Only keep rows where the `datatime` value matches the filter value
        filteredData = filteredData.filter(row => row.datetime === date);
};
    // Rebuild the table using the filtered data
    buildTable(filteredData);
};
// Attach an event to listen for the form button
d3.selectAll("#filter-btn").on("click", handleClick);

// Build the table where the page loads
buildTable(tableData);
