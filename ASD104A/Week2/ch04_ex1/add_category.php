<?php
// Get the category name
$name = filter_input(INPUT_POST, 'name');

// Validate input
if ($name == NULL) {
    $error = "Invalid category name. Check the field and try again.";
    include('error.php');
} else {
    require_once('database.php');

    // Step 8: Add the category to the database
    $query = 'INSERT INTO categories (categoryName)
              VALUES (:name)';
    $statement = $db->prepare($query);
    $statement->bindValue(':name', $name);
    $statement->execute();
    $statement->closeCursor();

    // Display the Category List page
    include('category_list.php');
}
?>
