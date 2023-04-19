/*    JavaScript 7th Edition
      Chapter 2
      Project 02-05

      Application to create an online calculator
      Author: Michael D. Connell Jr.
      Date: 2023-04-18

      Filename: project02-05.js
*/

// Function to display characters in the calculator window based on what is clicked
function display(val) {
   document.getElementById("calcWindow").value += val;
}

// Function to calculate the result of the expression in the calculator window
function calculate() {
   try {
      document.getElementById("calcWindow").value = eval(document.getElementById("calcWindow").value);
   } catch (e) {
      document.getElementById("calcWindow").value = "Error";
   }
}

// Function to clear the calculator window
function clearCalc() {
   document.getElementById("calcWindow").value = "";
}

// Assign onclick event handlers to each calculator button
window.onload = function() {
   var buttons = document.getElementsByClassName("calcButton");
   for (var i = 0; i < buttons.length; i++) {
      buttons[i].onclick = function() {
         if (this.value === "enter") {
            calculate();
         } else if (this.value === "C") {
            clearCalc();
         } else {
            display(this.value);
         }
      }
   }
}

