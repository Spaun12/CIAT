"use strict";
/*    JavaScript 7th Edition
      Chapter 12
      Project 12-05

      Project to validate a user form
      Author: Michael D. Connell Jr.
      Date: 2023-05-17  

      Filename: project12-05.js
*/

$("#userform")  // Changed selector from 'form.userform' to '#userform'
.attr("novalidate", "")
.submit( e => {  
   let isValid = true;
   
   let username = $("#username");  // Changed selector from 'input#username' to '#username'
   if (username.val() === "") {  // Added parentheses to val method: val === "" to val() === ""
      isValid = false;
      username.next()
      .hide()
      .text("* You must supply a username")
      .show(500);
   } else {
      username.next().text("");
   }
   
   let email = $("#email");  // Corrected the selector, $(input#email) to $("#email")
   let mailRE = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;  // Converted string to RegExp
	let validMail = mailRE.test(email.val()); 
   
   if (!validMail) {  // Simplified the condition, validMail !== true to !validMail
      isValid = false;
      email.next()
      .hide()
      .text("* Not a valid e-mail address")
      .show(500);      
   } else {
      email.next().text("");
   }
   
   let pwd = $("#pwd");  // Changed selector from 'input#pwd' to '#pwd'
	let pwdRE = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
	let validPwd = pwdRE.test(pwd.val());
   
   if (!validPwd) {  // Simplified the condition, validPwd !== true to !validPwd
      isValid = false;
      pwd.next()
      .hide()
      .text("* Invalid password")
      .show(500);  // Removed unnecessary semicolon after hide() and next()      
   } else {
      pwd.next().text("");
   }
   
   let pwd2 = $("#pwd2");  // Removed extra semicolon after selector
   
   if (pwd.val() !== pwd2.val()) {
      isValid = false;
      pwd2.next()
      .hide()
      .text("* Passwords must match")
      .show(500);  // Changed interval from 0.5 to 500      
   }  else {
      pwd2.next().text("");
   } 
   
   if (isValid === false) {  // Corrected the condition from 'isValid = false' to 'isValid === false'
      e.preventDefault();
   }
});
