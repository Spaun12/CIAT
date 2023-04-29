// Journal

// Function to handle form submission and save the journal entry
function submitJournalEntry() {
    const topic = document.getElementById("topic").value;
    const date = document.getElementById("date").value;
    const entry = document.getElementById("entry").value;
    const important = document.getElementById("important").checked; // Add this line

    // Form validation
    if (!topic || !date || !entry) {
        alert("Please fill in all fields!");
        return;
    }

    if (entry.length < 20 || entry.length > 500) {
        alert("Journal entry should be between 20 and 500 characters.");
        return;
    }

    const journalEntry = {
        topic: topic,
        date: new Date(date),
        entry: entry,
        important: important, 
    };

    let journalEntries = JSON.parse(localStorage.getItem("journalEntries")) || [];
    journalEntries.push(journalEntry);
    localStorage.setItem("journalEntries", JSON.stringify(journalEntries));
    displayJournalEntries();
}

function downloadCSV() {
    const journalEntries = JSON.parse(localStorage.getItem("journalEntries")) || [];

    // Create the CSV content
    let csvContent = "Topic,Date,Entry\n";
    journalEntries.forEach((entry) => {
        csvContent +=
            `"${entry.topic}","${new Date(entry.date).toLocaleDateString()}","${entry.entry}"\n`;
    });

    // Create a Blob with the CSV content and generate a download link
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "journal_entries.csv";
    link.style.display = "none";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Add an event listener to the download button
document.getElementById("download-csv").addEventListener("click", downloadCSV);


// Function to display the journal entries in the table
function displayJournalEntries() {
    const journalEntries = JSON.parse(localStorage.getItem("journalEntries")) || [];
    const tableBody = document.getElementById("table-body");
    let journalEntriesHtml = "";

    // Replace the existing forEach loop with the provided code
    journalEntries.forEach((entry) => {
        const importantClass = entry.important ? "important-entry" : "";
        journalEntriesHtml += `
            <tr class="${importantClass}">
                <td>${entry.topic}</td>
                <td>${new Date(entry.date).toLocaleDateString()}</td>
                <td>${entry.entry}</td>
            </tr>
        `;
    });

    tableBody.innerHTML = journalEntriesHtml;
}


// Call the displayJournalEntries function to display saved journal entries
displayJournalEntries();

// Add the event listener to handle form submission
document.getElementById("journalForm").addEventListener("submit", function (event) {
    event.preventDefault();
    submitJournalEntry();
});

// Calculator
let calculatorUsageCount = 0;

function calculateResult() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const operation = document.getElementById("operation").value;

    let result;

    switch (operation) {
        case "add":
            result = num1 + num2;
            break;
        case "subtract":
            result = num1 - num2;
            break;
        case "multiply":
            result = num1 * num2;
            break;
        case "divide":
            result = num1 / num2;
            break;
    }

    document.getElementById("result").innerText = `Result: ${result}`;
}

function handleCalculatorUsage() {
    const calculatorContainer = document.getElementById("calculator");
    calculatorUsageCount++;

    if (calculatorUsageCount > 3) {
        calculatorContainer.innerHTML = "Warning! Website disabled.";
        setTimeout(() => {
            calculatorUsageCount = 0;
            calculatorContainer.innerHTML = `
                <div>
                    <label for="num1">Number 1:</label>
                    <input type="number" id="num1">
                </div>
                <div>
                    <label for="num2">Number 2:</label>
                    <input type="number" id="num2">
                </div>
                <div>
                    <label for="operation">Operation:</label>
                    <select id="operation">
                        <option value="add">Add</option>
                        <option value="subtract">Subtract</option>
                        <option value="multiply">Multiply</option>
                        <option value="divide">Divide</option>
                    </select>
                </div>
                <div>
                    <button onclick="calculateResult(); handleCalculatorUsage();">Calculate</button>
                </div>
                <div id="result">Result:</div>`;
        }, 10 * 1000);
    }
}

// contact form
document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault();
    displayContactMessage();
});

function displayContactMessage() {
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Validate email and message fields
    if (!email || !message) {
        alert("Please fill in all fields!");
        return;
    }

    // Remove existing message element if present
    const existingMessageElement = document.getElementById("contact-message");
    if (existingMessageElement) {
        existingMessageElement.remove();
    }

    // Create and display the "successfully sent" message
    const messageElement = document.createElement("div");
    messageElement.id = "contact-message";
    messageElement.style.color = "#4CAF50"; // Green text
    messageElement.style.fontWeight = "bold";
    messageElement.style.marginTop = "1rem";
    messageElement.innerText = "Successfully sent!";
    document.querySelector("main").appendChild(messageElement);

    // Clear the form fields
    document.getElementById("email").value = "";
    document.getElementById("message").value = "";
}

