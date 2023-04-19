"use strict";
/*  JavaScript 7th Edition
    Chapter 10
    Project 10-05

    Crossword Puzzle Code for Keyboard Actions
    
    Author: 
    Date:   

    Filename: project10-05.js

*/


// Event handler to for keydown events within the current document
document.onkeypress = selectLetter;

// Function to apply keyboard actions to select a letter or navigate the puzzle
function selectLetter(e) {
   
   event.preventDefault();
   
   // Reference the letter to the left of the current letter
   let leftLetter = document.getElementById(currentLetter.dataset.left);
   
   // Reference the letter above the current letter
   let upLetter = document.getElementById(currentLetter.dataset.up);
   
   // Reference the letter to the right of the current letter
   let rightLetter = document.getElementById(currentLetter.dataset.right); 
   
   // Reference the letter below the current letter
   let downLetter = document.getElementById(currentLetter.dataset.down); 
   
   // Get the key typed by the player
   let userKey = e.code;
 
   if (userKey === "ArrowLeft") { // Move left 
      formatPuzzle(leftLetter);  
      
   } else if (userKey === "ArrowUp") { // Move up
      formatPuzzle(upLetter);  
      
   } else if (userKey === "ArrowRight" || userKey === "Tab") { // Move right
      formatPuzzle(rightLetter);  
      
   } else if (userKey === "ArrowDown" || userKey === "Enter") { // Move down
      formatPuzzle(downLetter);  
      
   } else if (userKey === "Backspace" || userKey === "Delete") { // Delete the character
      currentLetter.textContent = ""; 
      
   } else if (userKey === "Space") { // Toggle the typing direction
      switchTypeDirection();  
      
   } else if (userKey >= "a" && userKey <= "z") { // Write the character
      currentLetter.textContent = userKey; 
      
      if (typeDirection === "right") {
         formatPuzzle(rightLetter);  // Move right after typing the letter
      } else {
         formatPuzzle(downLetter);  // Move down after typing the letter
      }
   }

}

