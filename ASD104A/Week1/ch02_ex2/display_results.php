<!--Student: Michael Connell
    Date: 2023-08-02
    Project: Week 1 - Hands On Chapter 2 Exercise 2-1
    File: display_results.php -->

<?php
    // (4)Review the code: This section retrieves data from the form.
    $investment = filter_input(INPUT_POST, 'investment', FILTER_VALIDATE_FLOAT);
    $interest_rate = filter_input(INPUT_POST, 'interest_rate', FILTER_VALIDATE_FLOAT);
    $years = filter_input(INPUT_POST, 'years', FILTER_VALIDATE_INT);

    // (4): A default error message is set up here.
    $error_message = '';
    
    // (4): This section validates the investment input.
    if ($investment === FALSE ) {
        $error_message .= 'Investment must be a valid number.<br>'; 
    } else if ( $investment <= 0 ) {
        $error_message .= 'Investment must be greater than zero.<br>'; 
    } 
    
    // (4): This section validates the interest rate input.
    // (5) Enhance the validity checking: Added an additional validation to ensure interest rate is <= 15.
    if ( $interest_rate === FALSE )  {
        $error_message .= 'Interest rate must be a valid number.<br>'; 
    } else if ( $interest_rate <= 0 ) {
        $error_message .= 'Interest rate must be greater than zero.<br>'; 
    } else if ( $interest_rate > 15 ) {
        $error_message .= 'Interest rate must be less than or equal to 15.<br>'; 
    }
    
    // (4): This section validates the years input.
    if ( $years === FALSE ) {
        $error_message .= 'Years must be a valid whole number.<br>';
    } else if ( $years <= 0 ) {
        $error_message .= 'Years must be greater than zero.<br>';
    } else if ( $years > 30 ) {
        $error_message .= 'Years must be less than 31.<br>';
    } 

    // (4): If any validation failed, this section redirects back to the form.
    if ($error_message != '') {
        include('index.php');
        exit();
    }

    // (4): This section calculates the future value of the investment.
    $future_value = $investment;
    for ($i = 1; $i <= $years; $i++) {
        $future_value += $future_value * $interest_rate * .01; 
    }

    // (4): This section formats the investment, interest rate, and future value for output.
    $investment_f = '$'.number_format($investment, 2);
    $yearly_rate_f = $interest_rate.'%';
    $future_value_f = '$'.number_format($future_value, 2);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Future Value Calculator</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <main>
        <h1>Future Value Calculator</h1>

        <!-- (4): This section displays the investment amount. -->
        <label>Investment Amount:</label>
        <span><?php echo $investment_f; ?></span><br>

        <!-- (4): This section displays the interest rate. -->
        <label>Yearly Interest Rate:</label>
        <span><?php echo $yearly_rate_f; ?></span><br>

        <!-- (4): This section displays the number of years. -->
        <label>Number of Years:</label>
        <span><?php echo $years; ?></span><br>

        <!-- (4): This section displays the calculated future value. -->
        <label>Future Value:</label>
        <span><?php echo $future_value_f; ?></span><br>

        <!-- (6): This new section displays the current date. -->
        <label>Calculation Date:</label>
        <span><?php echo date('m/d/Y'); ?></span><br> <!-- Display the current date using PHP's date function -->
    </main>
</body>
</html>
