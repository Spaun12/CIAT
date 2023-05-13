// Calculator
let calculatorUsageCount = 0;

function calculateResult() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const operation = document.getElementById("operation").value;

    let result;

    switch (operation) {
        case "add":
            result = num1 + num2;
            break;
        case "subtract":
            result = num1 - num2;
            break;
        case "multiply":
            result = num1 * num2;
            break;
        case "divide":
            result = num1 / num2;
            break;
    }

    document.getElementById("result").innerText = `Result: ${result}`;
}

function handleCalculatorUsage() {
    const calculatorContainer = document.getElementById("calculator");
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
                    <label for="operation">Operation:</label>
                    <select id="operation">
                        <option value="add">Add</option>
                        <option value="subtract">Subtract</option>
                        <option value="multiply">Multiply</option>
                        <option value="divide">Divide</option>
                    </select>
                </div>
                <div>
                    <button onclick="calculateResult(); handleCalculatorUsage();">Calculate</button>
                </div>
                <div id="result">Result:</div>`;
        }, 10 * 1000);
    }
}