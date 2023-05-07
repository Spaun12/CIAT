// Michael D. Connell Jr. Beginner Website creation project 2023 CIAT WebDevelopment


// enable FeedbackManager to be imported as a module
import FeedbackManager from "./FeedbackManager.js";

// contact form
document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault();
    displayContactMessage();
});

const feedbackManager = new FeedbackManager();

// Handle checkbox changes for feedback form
document.querySelectorAll('input[type=checkbox]').forEach((checkbox) => {
    checkbox.addEventListener('change', (event) => {
        if (event.target.checked) {
            feedbackManager.addOption(event.target.value);
        } else {
            feedbackManager.removeOption(event.target.value);
        }
    });
});

function displayContactMessage() {
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Validate email and message fields
    if (!email || !message) {
        alert("Please fill in all fields!");
        return;
    }

    // Validate if at least one reason is selected _ Had to be added to make checks operate correctly
    if (feedbackManager.isEmpty()) {
        alert("Please select at least one reason for contacting us!");
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

    // Remove the "successfully sent" message after a timeout (5 seconds)
    setTimeout(() => {
        messageElement.remove();
    }, 5000); // (5 seconds)
}