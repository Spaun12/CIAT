"use strict";
/*    JavaScript 7th Edition
      Chapter 5
      Project 05-03

      Project to create a table of headings from an article
      Author: Michael D. Connell Jr.
      Date: 2023-04-26   

      Filename: project05-03.js
*/

// Declare variables
const sourceDoc = document.getElementById("source_doc");
const toc = document.getElementById("toc");
let headingCount = 1;
const heading = "H2";

// Loop through all child elements of sourceDoc
for (let n = sourceDoc.firstElementChild; n !== null; n = n.nextElementSibling) {
  // Check if the current node is an H2 element
  if (n.nodeName === heading) {
    // Create anchor element and set its name attribute
    const anchor = document.createElement("a");
    anchor.name = "doclink" + headingCount;
    
    // Insert anchor before the first child of the H2 element
    n.insertBefore(anchor, n.firstChild);

    // Create li and a elements, and append the link to the listItem
    const listItem = document.createElement("li");
    const link = document.createElement("a");
    listItem.appendChild(link);

    // Set the link text and href attributes
    link.textContent = n.textContent;
    link.href = "#doclink" + headingCount;

    // Append listItem to the toc object
    toc.appendChild(listItem);

    // Increment headingCount
    headingCount++;
  }
}