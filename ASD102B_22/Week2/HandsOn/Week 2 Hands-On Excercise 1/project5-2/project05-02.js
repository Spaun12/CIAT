"use strict";
/*    JavaScript 7th Edition
      Chapter 5
      Project 05-02

      Project to move images between a photo bucket and photo list.
      Author: Michael D. Connell Jr.
      Date: 2023-04-26  

      Filename: project05-02.js
*/

// Declare the required variables
let images = document.getElementsByTagName("img");
let photoBucket = document.getElementById("photo_bucket");
let photoList = document.getElementById("photo_list");

// Iterate through all items in the images collection
for (let i = 0; i < images.length; i++) {
   // Add onclick event handler for each image
   images[i].onclick = function () {
      // Determine if the image should be moved to the photo list or back to the photo bucket
      if (this.parentElement.id === "photo_bucket") {
         // Move image from photo bucket to photo list
         let newItem = document.createElement("li");
         photoList.appendChild(newItem);
         newItem.appendChild(this);
      } else {
         // Move image from photo list back to photo bucket
         let oldItem = this.parentElement;
         photoBucket.appendChild(this);
         oldItem.parentElement.removeChild(oldItem);
      }
   };
}