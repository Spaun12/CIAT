"use strict";
/*    JavaScript 7th Edition
      Chapter 7
      Project 07-02

      Project to deal cards from a shuffled poker deck
      Author: Michael D. Connell Jr.
      Date: 2023-05-02

      Filename: project07-02.js
*/

let deckStr = `Ace of Hearts, King of Hearts, Queeen of Hearts, Jack of Hearts,
               10 of Hearts, 9 of Hearts, 8 of Hearts, 7 of Hearts, 6 of Hearts,
               5 of Hearts, 4 of Hearts, 3 of Hearts, 2 of Hearts,
               Ace of Spades, King of Spades, Queeen of Spades, Jack of Spades,
               10 of Spades, 9 of Spades, 8 of Spades, 7 of Spades, 6 of Spades,
               5 of Spades, 4 of Spades, 3 of Spades, 2 of Spades,
               Ace of Diamonds, King of Diamonds, Queeen of Diamonds, Jack of Diamonds,
               10 of Diamonds, 9 of Diamonds, 8 of Diamonds, 7 of Diamonds, 6 of Diamonds,
               5 of Diamonds, 4 of Diamonds, 3 of Diamonds, 2 of Diamonds, 
               Ace of Clubs, King of Clubs, Queeen of Clubs, Jack of Clubs,
               10 of Clubs, 9 of Clubs, 8 of Clubs, 7 of Clubs, 6 of Clubs,
               5 of Clubs, 4 of Clubs, 3 of Clubs, 2 of Clubs`;

let cards = document.querySelectorAll("div#hand span"); 
let cardsLeft = document.getElementById("cardsLeft");
let deck = [];

newDeck(); // Call newDeck() initially to generate the deck of cards

document.getElementById("deal").onclick = function() {   
   // Step 5: Iterate through the contents of the cards node list
   for (let i = 0; i < cards.length; i++) {
      if (deck.length === 0) {
         newDeck();
      }
      cards[i].textContent = deck.pop();
      cardsLeft.textContent = deck.length;
   }
};

// Step 4: Create the newDeck() function
function newDeck() {
   // a. Split the contents of the deckStr variable
   deck = deckStr.split(", ");

   // b. Sort the contents of the deck array using the shuffle() function
   deck.sort(shuffle);

   // c. Create the shuffle() function
   function shuffle(a, b) {
      return 0.5 - Math.random();
   }
}