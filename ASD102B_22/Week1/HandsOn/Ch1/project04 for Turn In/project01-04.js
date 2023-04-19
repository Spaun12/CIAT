/*  JavaScript 7th Edition
    Chapter 1
    Hands-On Project 1-4

    Author: Michael D. Connell Jr.
    Date: 2023-04-18

    Filename: project01-04.js
*/

// Step 2: Define variables for home and work addresses
var homeStreet = "1 Main St.";
var homeCity = "Sicilia";
var homeState = "MA";
var homeCode = "02103";
var workStreet = "15 Oak Ln.";
var workCity = "Central City";
var workState = "MA";
var workCode = "02104";

// Function to display home and work addresses
function displayAddresses() {
  document.getElementById('homeAddressDetails').innerHTML = homeStreet + "<br>" + homeCity + ", " + homeState + " " + homeCode;
  document.getElementById('workAddressDetails').innerHTML = workStreet + "<br>" + workCity + ", " + workState + " " + workCode;
}

// Step 7a-d: Function to set home address input values
function setHomeAddress() {
  document.getElementById('street').value = homeStreet;
  document.getElementById('city').value = homeCity;
  document.getElementById('state').value = homeState;
  document.getElementById('code').value = homeCode;
}

// Step 8a-d: Function to set work address input values
function setWorkAddress() {
  document.getElementById('street').value = workStreet;
  document.getElementById('city').value = workCity;
  document.getElementById('state').value = workState;
  document.getElementById('code').value = workCode;
}