"use strict";
/*    JavaScript 7th Edition
      Chapter 8
      Project 08-01

      Project to create a timer object
      Author: Michael D. Connell Jr. 
      Date: 2023-05-02   

      Filename: project08-01.js
*/

/*--------------- Object Code --------------------*/

// Step 3: Add constructor function for the timer object
function timer(min, sec) {
   this.minutes = min;
   this.seconds = sec;
   this.timeID = null;
}

// Step 4: Add the runPause() method to the timer object class prototype
timer.prototype.runPause = function(timer, minBox, secBox) {
   // Step 5: Add tasks to runPause() method
   if (timer.timeID) {
      window.clearInterval(timer.timeID);
      timer.timeID = null;
   } else {
      timer.timeID = window.setInterval(countdown, 1000);
   }

   // Step 6: Add countdown() function
   function countdown() {
      if (timer.seconds > 0) {
         timer.seconds--;
      } else if (timer.minutes > 0) {
         timer.minutes--;
         timer.seconds = 59;
      } else {
         window.clearInterval(timer.timeID);
         timer.timeID = null;
      }
      minBox.value = timer.minutes;
      secBox.value = timer.seconds;
   }
};

/*---------------Interface Code -----------------*/

/* Interface Objects */
let minBox = document.getElementById("minutesBox");
let secBox = document.getElementById("secondsBox");
let runPauseTimer = document.getElementById("runPauseButton");

// Step 7: Declare an instance of the timer object
let myTimer = new timer(minBox.value, secBox.value);

// Step 8: Create onchange event handlers for minBox and secBox
minBox.onchange = function() {
   myTimer.minutes = minBox.value;
};
secBox.onchange = function() {
   myTimer.seconds = secBox.value;
};

// Step 9: Create an onclick event handler for the runPauseTimer button
runPauseTimer.onclick = function() {
   myTimer.runPause(myTimer, minBox, secBox);
};