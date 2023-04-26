/*    JavaScript 7th Edition
      Chapter 4
      Project 04-03

      Application to count the number of characters in a review comment
      Author: Michael D. Connell Jr.
      Date: 2023-04-26  

      Filename: project04-03.js
*/

// Step 3: Insert a statement directing that the code be interpreted under strict standards
"use strict";

// Maximum Length of Review
const MAX_REVIEW = 1000;
document.getElementById("limit").innerHTML = MAX_REVIEW;

// Reference to elements in the web page
let wordCountBox = document.getElementById("countValue");
let warningBox = document.getElementById("warningBox");

// Step 6: Fix the syntax error in the event listener
// Event listener for typing into the comment box
document.getElementById("comment").addEventListener("keyup", updateCount);

// Function to update the count with each keyup event
function updateCount() {
   // Set the warning box to an empty text string 
   warningBox.innerHTML = "";
   
   // Count the number of characters in the comment box
   let commentText = document.getElementById("comment").value;
   let charCount = countCharacters(commentText);
   
   // Step 4: Insert a try catch finally statement
   try {
      // Test if the charCount variable is greater than the value of the MAX_REVIEW constant
      if (charCount > MAX_REVIEW) {
         throw new Error("You have exceeded the character count limit");
      }
   } catch (error) {
      // Display the error message within the innerHTML of the warningBox object
      warningBox.innerHTML = error.message;
   } finally {
      // Change the innerHTML of the wordCountBox object to the value of the charCount variable
      wordCountBox.innerHTML = charCount;
   }
}

/*=================================================================*/
// Function to count the number of characters in a text string
function countCharacters(textStr) {
   var commentregx = /\s/g;
   var chars = textStr.replace(commentregx, "");
   return chars.length;
}
