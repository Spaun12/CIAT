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
        $action = 'list_categories';
    }
}

switch ($action) {
    case 'list_categories':
        $categories = CategoryDB::getCategories();
        include('category_list.php');
        break;
    case 'add_category':
        $name = filter_input(INPUT_POST, 'name');

        // Validate inputs
        if ($name == NULL) {
            $error = "Invalid category name. Check name and try again.";
            include('errors/error.php');
        } else {
            CategoryDB::addCategory($name);
            // display the Category List page
            header('Location: .?action=list_categories');  
        }
        break;
    case 'delete_category':
        $category_id = filter_input(INPUT_POST, 'category_id', 
                FILTER_VALIDATE_INT);

        $product_count = CategoryDB::getProductCount($category_id);
        if ($product_count > 0) {
            $error = "This category can't be deleted because it contains products.";
            include('errors/error.php');
        } else {
            CategoryDB::deleteCategory($category_id);
            // display the Category List page
            header('Location: .?action=list_categories');      
        }
        break;
}
?>