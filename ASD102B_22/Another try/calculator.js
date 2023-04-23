let usageCount = 0;
//this has both the calculator and the if else task part of number 3
function calculate(operation) {
  if (usageCount >= 3) {
    // Show warning, hide calculator, and reset usageCount after 2 seconds
    document.getElementById("warning").style.display = "block";
    document.getElementById("calculator").style.display = "none";
    setTimeout(() => {
      document.getElementById("warning").style.display = "none";
      document.getElementById("jk").style.display = "block";
      setTimeout(() => {
        document.getElementById("jk").style.display = "none";
        document.getElementById("calculator").style.display = "block";
        usageCount = 0;
      }, 2000);
    }, 2000);
    return;
  }

  const number1 = parseFloat(document.getElementById("number1").value);
  const number2 = parseFloat(document.getElementById("number2").value);
  let result;

  switch (operation) {
    case "add":
      result = number1 + number2;
      break;
    case "subtract":
      result = number1 - number2;
      break;
    case "multiply":
      result = number1 * number2;
      break;
    case "divide":
      result = number1 / number2;
      break;
    default:
      result = "Invalid operation";
  }

  document.getElementById("result").innerHTML = result;
  usageCount++;
}