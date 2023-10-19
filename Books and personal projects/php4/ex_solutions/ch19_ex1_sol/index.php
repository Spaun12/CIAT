<?php
require_once('util/main.php');

require_once('model/database.php');
require_once('model/product_db.php');
require_once('model/category_db.php');
require_once('model/product.php');
require_once('model/category.php');

/*********************************************
 * Select some products
 **********************************************/

// Sample data
$cat_id = 1;

// Get the products
$products = ProductDB::getProductsByCategory($cat_id);

/***************************************
 * Delete a product
 ****************************************/

// Sample data
$product_name = 'Fender Telecaster';

// Delete the product and display an appropriate messge
$product = ProductDB::getProductByName($product_name);
if ($product) {
    $product_id = $product->getID();
    $row_count = ProductDB::deleteProduct($product_id);
    if ($row_count > 0) {
        $delete_message = "$row_count row was deleted.";
    } else {
        $delete_message = "No rows were deleted.";
    }
} else {
    $delete_message = "There is no product with that name.";
}

/***************************************
 * Insert a product
 ****************************************/

// Sample data
$category_id = 1;
$code = 'tele';
$name = 'Fender Telecaster';
$description = 'NA';
$price = '949.99';
$discount_percent = '10';

// Insert the data
$category = CategoryDB::getCategory($category_id);
$product = new Product($category, $code, $name, $description, $price, $discount_percent);
$product_id = ProductDB::addProduct($product);

// Display an appropriate message
if ($product_id > 0) {
    $insert_message = "1 row was inserted with this ID: $product_id";
} else {
    $insert_message = "No rows were inserted.";
}

include 'home.php';
?>