<?php
require_once('util/main.php');
require_once('util/tags.php');
require_once('model/database.php');
require_once('model/product_db.php');
require_once('model/category_db.php');
require_once('model/product.php');
require_once('model/category.php');

// Get all categories
$categories = CategoryDB::getCategories();

// Set the featured product IDs in an array
$product_ids = [1, 7, 9];
// Note: You could also store a list of featured products in the database

// Get an array of featured products from the database
$products = [];
foreach ($product_ids as $product_id) {
    $product = ProductDB::getProduct($product_id);
    $products[] = $product;   // add product to array
}

// Display the home page
include('home_view.php');
?>