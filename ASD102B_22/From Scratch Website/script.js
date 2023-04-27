// Journal form validation
function validateJournalForm() {
  const topic = document.getElementById("topic");
  const date = document.getElementById("date");
  const entry = document.getElementById("entry");
  const agree = document.getElementById("agree");

  if (!topic.value.trim()) {
      alert("Please enter a topic.");
      topic.focus();
      return false;
  }

  if (!date.value) {
      alert("Please select a date.");
      date.focus();
      return false;
  }

  if (!entry.value.trim()) {
      alert("Please enter your journal entry.");
      entry.focus();
      return false;
  }

  if (!agree.checked) {
      alert("Please agree to the terms and conditions.");
      agree.focus();
      return false;
  }

  alert("Your journal entry has been submitted.");
  return true;
}

// Calculator
let calculatorUsageCount = 0;
const calculatorContainer = document.getElementById("calculator");

function calculateSum() {
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);
  const sum = num1 + num2;
  document.getElementById("result").innerText = `Result: ${sum}`;
}

function handleCalculatorUsage() {
  calculatorUsageCount++;

  if (calculatorUsageCount > 3) {
      calculatorContainer.innerHTML = "Warning! Website disabled.";
      setTimeout(() => {
          calculatorUsageCount = 0;
          calculatorContainer.innerHTML = `
              <div>
                  <label for="num1">Number 1:</label>
                  <input type="number" id="num1">
              </div>
              <div>
                  <label for="num2">Number 2:</label>
                  <input type="number" id="num2">
              </div>
              <div>
                  <button onclick="calculateSum(); handleCalculatorUsage();">Add Numbers</button>
              </div>
              <div id="result">Result:</div>`;
      }, 2 * 60 * 1000);
  }
}