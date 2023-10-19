<?php
require_once('../../util/main.php');
require_once('../../util/tags.php');
require_once('../../model/database.php');
require_once('../../model/product_db.php');
require_once('../../model/category_db.php');
require_once('../../model/product.php');
require_once('../../model/category.php');

$action = filter_input(INPUT_POST, 'action');
if ($action == NULL) {
    $action = filter_input(INPUT_GET, 'action');
    if ($action == NULL) {
        $action = 'list_products';
    }
}

switch ($action) {
    case 'list_products':
        $category_id = filter_input(INPUT_GET, 'category_id', 
                FILTER_VALIDATE_INT);
        if ($category_id === FALSE || $category_id === NULL) {
            $category_id = 1;
        }                
        $current_category = CategoryDB::getCategory($category_id);
        $categories = CategoryDB::getCategories();
        $products = ProductDB::getProductsByCategory($category_id);
        include('product_list.php');
        break;
    case 'view_product':
        $categories = CategoryDB::getCategories();
        $product_id = filter_input(INPUT_GET, 'product_id', 
                FILTER_VALIDATE_INT);
        $product = ProductDB::getProduct($product_id);
        include('product_view.php');
        break;
    case 'delete_product':
        $product_id = filter_input(INPUT_POST, 'product_id', 
                FILTER_VALIDATE_INT);
        $category_id = filter_input(INPUT_POST, 'category_id', 
                FILTER_VALIDATE_INT);
        ProductDB::deleteProduct($product_id);
        
        // display product list for the current category
        header("Location: .?category_id=$category_id");
        break;
    case 'show_add_edit_form':
        $categories = CategoryDB::getCategories();
        $product_id = filter_input(INPUT_GET, 'product_id', 
                FILTER_VALIDATE_INT);
        if ($product_id == NULL) {
            $product_id = filter_input(INPUT_POST, 'product_id', 
                    FILTER_VALIDATE_INT);
        }
        if (isset($product_id)) {
            $product = ProductDB::getProduct($product_id);
        }
        include('product_add_edit.php');
        break;
    case 'add_product':        
        $category_id = filter_input(INPUT_POST, 'category_id', 
                FILTER_VALIDATE_INT);
        $code = filter_input(INPUT_POST, 'code');
        $name = filter_input(INPUT_POST, 'name');
        $description = filter_input(INPUT_POST, 'description');
        $price = filter_input(INPUT_POST, 'price', FILTER_VALIDATE_FLOAT);
        $discount_percent = filter_input(INPUT_POST, 'discount_percent',
                FILTER_VALIDATE_FLOAT);        

        if ($category_id === FALSE || 
                $code == NULL || $name == NULL || $description == NULL ||
                $price === FALSE || $discount_percent === FALSE) {            
            $error = 'Invalid product data.
                      Check all fields and try again.';
            include('../../errors/error.php');
        } else {
            $category = new Category($category_id, "");
            $product = new Product($category, $code, $name, $description,
                                   $price, $discount_percent);
            $product_id = ProductDB::addProduct($product);
            // display added product
            header("Location: .?action=view_product&product_id=$product_id");
        }
        break;
    case 'update_product':
        $product_id = filter_input(INPUT_POST, 'product_id', 
                FILTER_VALIDATE_INT);
        $category_id = filter_input(INPUT_POST, 'category_id', 
                FILTER_VALIDATE_INT);
        $code = filter_input(INPUT_POST, 'code');
        $name = filter_input(INPUT_POST, 'name');
        $description = filter_input(INPUT_POST, 'description');
        $price = filter_input(INPUT_POST, 'price', FILTER_VALIDATE_FLOAT);
        $discount_percent = filter_input(INPUT_POST, 'discount_percent');        

        if ($product_id === FALSE || $category_id === FALSE ||
                $code == NULL || $name == NULL || $description == NULL ||
                $price === FALSE || $discount_percent === FALSE) {            
            $error = 'Invalid product data.
                      Check all fields and try again.';
            include('../../errors/error.php');
        } else {
            $category = new Category($category_id, "");
            $product = new Product($category, $code, $name, $description,
                                   $price, $discount_percent);
            $product->setID($product_id);
            ProductDB::updateProduct($product);
            // display updated product
            header("Location: .?action=view_product&product_id=$product_id");
        }
        break;
}
?>