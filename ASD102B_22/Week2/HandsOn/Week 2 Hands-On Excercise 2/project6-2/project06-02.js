"use strict";

/*    JavaScript 7th Edition
      Chapter 6
      Project 06-02

      Project to turn a selection list into a selection of hypertext links
      Author: Michael D. Connell Jr. 
      Date: 2023-04-26  

      Filename: project06-02.js
*/

// Step 3: Add an event listener that runs an anonymous function when the page loads
document.addEventListener("DOMContentLoaded", function () {

      // Step 4: Create a node list of all elements matching the CSS selector form#govLinks select
    let allSelect = document.querySelectorAll("form#govLinks select");

    // Step 5: Iterate through all the contents of the allSelect node list
    for (let i = 0; i < allSelect.length; i++) {

      // Step 5a: Apply the onchange event handler to run an anonymous function when the selection list option is changed
        allSelect[i].addEventListener("change", function (evt) {

            // Step 5b: Retrieve the value property of evt.target and store it in the linkURL variable
            let linkURL = evt.target.value;

            // Step 5c: Use the window.open() method to open a new browser window with linkURL as the URL
            let newWin = window.open(linkURL);
        });
    }
});