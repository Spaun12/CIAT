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
