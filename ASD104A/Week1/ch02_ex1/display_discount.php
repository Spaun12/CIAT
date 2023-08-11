<!--Student: Michael Connell
    Date: 2023-08-02
    Project: Week 1 - Hands On Chapter 2 Exercise 2-1
    File: display_discount.php -->

<!DOCTYPE html>
<html>
<head>
    <title>Product Discount Calculator</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <main>
        <h1>Product Discount Calculator</h1> <!-- Fixed the heading as per step 11 -->

        <?php 
            // Step 5: using $_POST to get the data from the form
            // I hope I am getting this right
            $product_description = $_POST['product_description']; 
            $list_price = filter_input(INPUT_POST, 'list_price', FILTER_VALIDATE_FLOAT); // Step 6: Changing $_POST with filter_input for validation and security
            $discount_percent = filter_input(INPUT_POST, 'discount_percent', FILTER_VALIDATE_FLOAT); // Step 6: Changing $_POST with filter_input for validation and security

            // Step 7: Calculating the discount amount and discount price
            $discount_amount = $list_price * $discount_percent * .01; // discount amount calculation
            $discount_price = $list_price - $discount_amount; // discount price calculation
        ?>

        <label>Product Description:</label>
        <!-- Step 10: Adding htmlspecialchars to avoid HTML rendering -->
        <span><?php echo htmlspecialchars($product_description); ?></span><br>

        <label>List Price:</label>
        <!-- Step 8: Formatting the number as currency -->
        <span><?php echo '$'.number_format($list_price, 2); ?></span><br>

        <label>Discount Percent:</label>
        <!-- Step 8: Formatting the number as a percentage -->
        <span><?php echo number_format($discount_percent, 2).'%'; ?></span><br>

        <label>Discount Amount:</label>
        <!-- Step 8: Formatting the number as currency -->
        <span><?php echo '$'.number_format($discount_amount, 2); ?></span><br>

        <label>Discount Price:</label>
        <!-- Step 8: Formatting the number as currency -->
        <span><?php echo '$'.number_format($discount_price, 2); ?></span><br>
    </main>
</body>
</html>