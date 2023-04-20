/*    JavaScript 7th Edition
      Chapter 3
      Project 03-01

      Application to calculate total order cost
      Author: Michael D. Connell Jr.
      Date: 2023-04-19

      Filename: project03-01.js
*/

// 3. Declare a variable named menuItems
let menuItems = document.getElementsByClassName("menuItem");

// 4. Create a for loop that loops through the contents of the menuItems collection
for (let i = 0; i < menuItems.length; i++) {
    menuItems[i].addEventListener("click", calcTotal);
}

// 5. Create the calcTotal() function
function calcTotal() {
    let orderTotal = 0; // 5a. Declare the orderTotal variable

    // 5b. Create a for loop that loops through the contents of the menuItems collection
    for (let i = 0; i < menuItems.length; i++) {
        if (menuItems[i].checked) {
            orderTotal += Number(menuItems[i].value);
        }
    }

    // 5c. Change the innerHTML property of the element with the id "billTotal"
    document.getElementById("billTotal").innerHTML = formatCurrency(orderTotal);
}

// Function to display a numeric value as a text string in the format $##.##
function formatCurrency(value) {
    return "$" + value.toFixed(2);
}
