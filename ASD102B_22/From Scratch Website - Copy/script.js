// Michael D. Connell Jr. Beginner Website creation project 2023 CIAT WebDevelopment

// Journal Creation and Function

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


  
