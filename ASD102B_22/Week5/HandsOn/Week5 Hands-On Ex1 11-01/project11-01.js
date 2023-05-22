"use strict";
/*    JavaScript 7th Edition
      Chapter 11
      Project 11-01

      Project to retrieve the Astronomy Picture of the Day from NASA
      Author: Your Name
      Date: 2023-05-17

      Filename: project11-01.js
*/

let imageBox = document.getElementById("nasaImage");
let dateBox = document.getElementById("dateBox");

dateBox.onchange = function() {   
   // Step 3a: Retrieve the value of the dateBox element
   let dateStr = dateBox.value;

   // Step 3b: Fetch the data from the NASA APOD API
   fetch(`https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=${dateStr}`)
      .then(response => response.json()) // Step 3c: Parse the JSON response
      .then(json => showPicture(json)) // Step 3d: Call showPicture() with the JSON object
      .catch(error => console.log(error)); // Step 3e: Handle errors in the console
}

// Step 4: Define the showPicture function
function showPicture(json) {
   if (json.media_type === "video") {
      // Step 4a: If media_type is "video", display video HTML
      imageBox.innerHTML = `
         <iframe src="${json.url}"></iframe>
         <h1>${json.title}</h1>
         <p>${json.explanation}</p>
      `;
   } else if (json.media_type === "image") {
      // Step 4b: If media_type is "image", display image HTML
      imageBox.innerHTML = `
         <img src="${json.url}" />
         <h1>${json.title}</h1>
         <p>${json.explanation}</p>
      `;
   } else {
      // Step 4c: Otherwise, display "Image not Available"
      imageBox.innerHTML = "Image not Available";
   }
}