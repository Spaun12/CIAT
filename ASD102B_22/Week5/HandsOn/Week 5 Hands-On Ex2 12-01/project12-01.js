"use strict";
/*    JavaScript 7th Edition
      Chapter 12
      Project 12-01

      Project to display a dropdown menu
      Author: Michael D. Connell Jr.
      Date: 2023-05-17

      Filename: project12-01.js
*/

// Step 3: Run code when the page is loaded and ready
$(document).ready(function() {
   // Step 4: Show dropdown menu on mouseover
   $("li.submenu").mouseover(function(e) {
      $(e.currentTarget).children("ul").show();
   });

   // Step 5: Hide dropdown menu on mouseout
   $("li.submenu").mouseout(function(e) {
      $(e.currentTarget).children("ul").hide();
   });
});                                               