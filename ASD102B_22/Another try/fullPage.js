document.addEventListener('DOMContentLoaded', function () {
    new fullpage('#fullpage', {
        anchors: ['home', 'portfolio', 'calculator', 'contact'],
        navigation: true,
        paddingTop: '3em',
        paddingBottom: '10px',
        fixedElements: '#header, .footer',
        scrollingSpeed: 1000, // Adjust this value to control the scrolling speed (milliseconds)
        touchSensitivity: 25, // Adjust this value to control the touch sensitivity (higher values require more swipe)
    });

    const menuItems = document.querySelectorAll('nav ul li a');
    menuItems.forEach((item) => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetSection = e.target.getAttribute('href').substring(1);
            fullpage_api.moveTo(targetSection);
        });
    });
});

// Calculator code
let usageCount = 0;

function calculate(operation) {
    if (usageCount >= 3) {
        document.getElementById("warning").style.display = "block";
        document.getElementById("calculator-wrapper").style.display = "none";
        setTimeout(() => {
            document.getElementById("warning").style.display = "none";
            document.getElementById("jk").style.display = "block";
            setTimeout(() => {
                document.getElementById("jk").style.display = "none";
                document.getElementById("calculator-wrapper").style.display = "block";
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
        case "percentage":
            result = (number1 / 100) * number2;
            break;
        default:
            result = "Invalid operation";
    }

    document.getElementById("result").innerHTML = result;
    usageCount++;
}
