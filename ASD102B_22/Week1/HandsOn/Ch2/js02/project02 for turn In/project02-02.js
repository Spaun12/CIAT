/*    JavaScript 7th Edition
      Chapter 2
      Project 02-02

      Application to test for completed form
      Author: Your Name
      Date: 2023-04-18   

      Filename: project02-02.js
 */

// Step 3: Created a function named verifyForm() with no parameters
function verifyForm() {
      // a. Declare the name variable equal to the value of the input control with the id “name”
      let name = document.getElementById("name").value;
  
      // b. Declare the email variable equal to the value of the input control with the id “email”
      let email = document.getElementById("email").value;
  
      // c. Declare the phone variable equal to the value of the input control with the id “phone”
      let phone = document.getElementById("phone").value;
  
      // d. Insert a conditional operator that tests the truthy or falsy value of name and email and phone
      (name && email && phone) ? window.alert("Thank you!") : window.alert("Please fill in all fields");
        // If true, display the message “Thank you!”
        // Otherwise, display the message “Please fill in all fields”
  }
  // Step 4: Attach an event listener to the page element with the id “submit”
  document.getElementById("submit").addEventListener("click", verifyForm);  