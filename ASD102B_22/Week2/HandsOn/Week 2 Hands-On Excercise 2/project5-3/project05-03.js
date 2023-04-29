"use strict";
/*    JavaScript 7th Edition
      Chapter 5
      Project 05-03

      Project to create a table of headings from an article
      Author: Jared Rodriguez
      Date: April 28, 2023 
      Filename: project05-03.js
*/

// Declare variables
const heading = "H2";
let headingCount = 1;
const sourceDoc = document.getElementById("source_doc");
const toc = document.getElementById("toc");

// Loop through child elements of sourceDoc
for (let n = sourceDoc.firstElementChild; n != null; n = n.nextElementSibling) {

  // Check if child element is a heading
  if (n.nodeName === heading) {

    // Create anchor element for the TOC
    const anchor = document.createElement("a");
    anchor.setAttribute("name", "doclink" + headingCount);
    n.parentNode.insertBefore(anchor, n);

    // Create list item and link elements for the TOC
    const listItem = document.createElement("li");
    const link = document.createElement("a");
    link.textContent = n.textContent;

    // Add click event listener to smoothly scroll to the target anchor
    link.addEventListener("click", function(event) {
      event.preventDefault();
      const targetAnchor = document.querySelector(`[name=doclink${headingCount}]`);
      targetAnchor.scrollIntoView({ behavior: "smooth" });
    });

    // Append the link element to the list item element
    listItem.appendChild(link);

    // Set href attribute for the link element
    link.setAttribute("href", "#doclink" + headingCount);

    // Append the list item element to the TOC
    toc.appendChild(listItem);

    // Increment the heading count
    headingCount++;
  }
}

// Move event listener to the end to avoid the closure issue
toc.querySelectorAll("a").forEach((link, index) => {
  link.addEventListener("click", function(event) {
    event.preventDefault();
    const targetAnchor = document.querySelector(`[name=doclink${index + 1}]`);
    targetAnchor.scrollIntoView({ behavior: "smooth" });
  });
});