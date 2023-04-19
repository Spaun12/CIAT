/* JavaScript 7th Edition
   Chapter 2
   Project 02-04

   Application to calculate the cost of a restaurant order plus tax
   Author: Michael D. Connell Jr.
   Date: 2023-04-18

   Filename: project02-04.js
*/

// Step1 Constants
const CHICKEN_PRICE = 10.95;
const HALIBUT_PRICE = 13.95;
const BURGER_PRICE = 9.95;
const SALMON_PRICE = 18.95;
const SALAD_PRICE = 7.95;
const SALES_TAX = 0.07;

// Step4 Function to display a numeric value as a text string in the format $##.##
function formatCurrency(value) {
  return "$" + value.toFixed(2);
}

// Step 5 calcTotal function
document.getElementById("chicken").onclick = calcTotal;
document.getElementById("halibut").onclick = calcTotal;
document.getElementById("burger").onclick = calcTotal;
document.getElementById("salmon").onclick = calcTotal;
document.getElementById("salad").onclick = calcTotal;

function calcTotal() {
  // Step 4a
  let cost = 0;

  // Step 4b
  let buyChicken = document.getElementById("chicken").checked;
  let buyHalibut = document.getElementById("halibut").checked;
  let buyBurger = document.getElementById("burger").checked;
  let buySalmon = document.getElementById("salmon").checked;
  let buySalad = document.getElementById("salad").checked;

  // Step 4c
  cost += buyChicken ? CHICKEN_PRICE : 0;
  cost += buyHalibut ? HALIBUT_PRICE : 0;
  cost += buyBurger ? BURGER_PRICE : 0;
  cost += buySalmon ? SALMON_PRICE : 0;
  cost += buySalad ? SALAD_PRICE : 0;

  // Step 4d
  document.getElementById("foodTotal").innerHTML = formatCurrency(cost);

  // Step 4e
  let tax = cost * SALES_TAX;

  // Step 4f
  document.getElementById("foodTax").innerHTML = formatCurrency(tax);

  // Step 4g
  let totalCost = cost + tax;

  // Step 4h
  document.getElementById("totalBill").innerHTML = formatCurrency(totalCost);
}

// Initialize the cost, tax, and total values
calcTotal();


