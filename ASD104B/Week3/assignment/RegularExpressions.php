<?php
//Michael Connell
//Week 3 Assignment Regular Expressions
// Initialize variables to store messages
$emailMessage = "";
$nameMessage = "";
$phoneMessage = "";

// Function to validate email address format
function validate_email($email) {
    $pattern = '/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/';
    return preg_match($pattern, $email);
}

// Function to validate member's name
function validate_member_name($name) {
    $pattern = "/^[a-zA-Z\s']+$/";
    return preg_match($pattern, $name);
}

// Function to validate phone number
function validate_member_phone($phone) {
    $pattern = '/^[\d\s\-\(\)]+$/';
    return preg_match($pattern, $phone);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $name = $_POST['name'];
    $phone = $_POST['phone'];

    // Validate email and set message
    if (validate_email($email)) {
        $emailMessage = "<span class='success'>Valid email.</span>";
    } else {
        $emailMessage = "<span class='error'>Invalid email. Please use format username@example.com.</span>";
    }

    // Validate name and set message
    if (validate_member_name($name)) {
        $nameMessage = "<span class='success'>Valid name.</span>";
    } else {
        $nameMessage = "<span class='error'>Invalid name. Only letters, spaces, and apostrophes are allowed.</span>";
    }

    // Validate phone and set message
    if (validate_member_phone($phone)) {
        $phoneMessage = "<span class='success'>Valid phone.</span>";
    } else {
        $phoneMessage = "<span class='error'>Invalid phone. Only digits, parentheses, dashes, and spaces are allowed.</span>";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Member Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        .container {
            margin: auto;
            width: 40%;
            border: 2px solid #333;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #333;
            color: white;
            padding: 14px 20px;
            border: none;
            cursor: pointer;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Member Information</h2>

    <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
      Name: <input type="text" name="name">
      <?php echo $nameMessage; ?><br>

      Email: <input type="text" name="email">
      <?php echo $emailMessage; ?><br>

      Phone: <input type="text" name="phone">
      <?php echo $phoneMessage; ?><br>

      <input type="submit">
    </form>
</div>

</body>
</html>

