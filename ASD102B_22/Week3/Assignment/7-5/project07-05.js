"use strict";
/*    JavaScript 7th Edition
      Chapter 7
      Project 07-05

      Project to compare the distribution of word lengths between two authors
      Author: Michael D. Connell Jr. 
      Date: 2023-05-03  

      Filename: project07-05.js
*/

// Onchange event handler to load an external file for author 1
document.getElementById("button1").onchange = function() {
   // Fixed: Changed 'this.file[0]' to 'this.files[0]'
   let file = this.files[0];
   let doc = document.getElementById("document1");
   let count = document.getElementById("count1");
   
   // Generate the word frequency table for author 1
   generateWordFreq(file, doc, count);
};

// Onchange event handler to load an external file for author 2
document.getElementById("button2").onchange = function() {
   // Fixed: Changed 'this.file[0]' to 'this.files[0]'
   let file = this.files[0];
   let doc = document.getElementById("document2");
   let count = document.getElementById("count2");
   
   // Generate the word frequency table for author 2
   generateWordFreq(file, doc, count);
};

// Function that generates a table of frequencies for words
// of 1 to 15 characters in length
function generateWordFreq(inputFile, outputDoc, outputCount) {
   // Fixed: Changed 'Reader()' to 'FileReader()'
   let fr = new FileReader();
   // Fixed: Changed 'fr.read(inputFile)' to 'fr.readAsText(inputFile)'
   fr.readAsText(inputFile);

   // Once the file has finished loading, display the document in the page
   fr.onload = function() {
      outputDoc.innerHTML = fr.result;

      // Fixed: Changed 'outputDoc.innerHTML' to 'outputDoc.textContent'
      let sourceText = outputDoc.textContent;

      // Fixed: Changed '/[^a-zA-Z\s]/g' to /[^\sa-zA-Z]/g (removed quotes and fixed regex)
      let alphaRegx = /[^\sa-zA-Z]/g;
      sourceText = sourceText.replace(alphaRegx, "");

      // Fixed: Changed 'sourceText.split(/\s+/);' to 'sourceText.split(/\s+/g);'
      let words = sourceText.split(/\s+/g);

      // Initial frequency array for words of 1 to 15 characters in length
      // Setting their initial counts to 0.
      let freqs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

      // Fixed: Changed 'for (let i = 0; i <= words.length; i++)' to 'for (let i = 0; i < words.length; i++)'
      for (let i = 0; i < words.length; i++) {
         if (words[i].length >= 15) {
            freqs[15]++;
         } else {
            freqs[words[i].length]++;
         }
      }

      let totalWords = words.length;

      let outputPara = outputCount.getElementsByTagName("p");
      for (let i = 1; i <= 15; i++) {
         // Fixed: Changed '(totalWords/freqs[i]*100)' to '(freqs[i]/totalWords*100)'
         let percent = (freqs[i] / totalWords * 100).toFixed(1) + "%";
         outputPara[i - 1].textContent = percent;
      }
   };
}
