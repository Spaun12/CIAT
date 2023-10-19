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
$cat_id = 2;

// Get the products
$products = ProductDB::getProductsByCategory($cat_id);

/***************************************
 * Delete a product
 ****************************************/

// Sample data
$product_name = 'Fender Telecaster';

// Delete the product and display an appropriate messge
$delete_message = "No rows were deleted.";

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

// Insert the data and display an appropriate message
$insert_message = "No rows were inserted.";

include 'home.php';
?>