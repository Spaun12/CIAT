// Event listeners for convert and clear buttons
document.getElementById('convert').onclick = tempConvert;
document.getElementById('clear').onclick = clearForm;

// Function to convert temperatures
function tempConvert() {
    var fahrenheit = document.getElementById("fahrenheit").value;
    var celsius = document.getElementById("celsius").value;

    if (fahrenheit !== '') {
        celsius = (parseFloat(fahrenheit) - 32) / 1.8;
    } else if (celsius !== '') {
        fahrenheit = (parseFloat(celsius) * 1.8) + 32;
    }

    document.getElementById('fahrenheit').value = parseFloat(fahrenheit).toFixed(1);
    document.getElementById('celsius').value = parseFloat(celsius).toFixed(1);

    // Logic to convert Fahrenheit to Celsius and vice versa
    // Added logic to convert to Kelvin if needed
}

// Function to clear the form fields
function clearForm() {
    document.getElementById('fahrenheit').value = '';
    document.getElementById('celsius').value = '';
}

// Contributor note:
// Michael Connell
// For educational purposes - College project assignment
// Date: 2023-08-12




