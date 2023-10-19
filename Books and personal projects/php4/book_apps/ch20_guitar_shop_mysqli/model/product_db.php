<?php
class ProductDB {    
    public static function getProductsByCategory($category_id) {
        $db = Database::getDB();
        $category = CategoryDB::getCategory($category_id);
        
        $query = 'SELECT categoryID, productID, productCode, productName, 
                     description, listPrice, discountPercent 
                  FROM products
                  WHERE categoryID = ?
                  ORDER BY productID';

        try {
            $statement = $db->prepare($query);
            $statement->bind_param("i", $category_id);
            $statement->bind_result($category_id, $product_id, $code, $name, 
                $description, $price, $discount_percent);
            $statement->execute();
            
            $products = [];
            while($statement->fetch()) {
                $products[] = self::loadProduct($category, $product_id, $code, 
                        $name, $description, $price, $discount_percent);
            }
            $statement->close();
            return $products;
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }
    
    private static function loadProduct($category, $product_id, $code, $name, 
            $description, $price, $discount_percent) {
        $product = new Product($category, $code, $name, $description, 
                $price, $discount_percent);
        $product->setID($product_id);
        return $product;
    }
    
    public static function getProducts() {
        $db = Database::getDB();
        $query = 'SELECT c.categoryID, categoryName, productID, 
                     productCode, productName, 
                     description, listPrice, discountPercent 
                  FROM products AS p
                  JOIN categories AS c 
                  ON p.categoryID = c.CategoryID
                  ORDER BY productID';

        try {
            $statement = $db->prepare($query);
            $statement->bind_result($category_id, $category_name, $product_id, 
                $code, $name, $description, $price, $discount_percent);
            $statement->execute();
            
            $products = [];
            while($statement->fetch()) {
                $category = new Category($category_id, $category_name);
                $products[] = self::loadProduct($category, $product_id, $code, 
                        $name, $description, $price, $discount_percent);
            }
            $statement->close();
            
            return $products;
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }

    public static function getProduct($product_id) {
        $db = Database::getDB();
        $query = 'SELECT categoryID, productID, productCode, productName, 
                    description, listPrice, discountPercent 
                  FROM products 
                  WHERE productID = ?';

        try {
            $statement = $db->prepare($query);
            $statement->bind_param("i", $product_id);
            $statement->bind_result($category_id, $product_id, $code, $name, 
                $description, $price, $discount_percent);
            $statement->execute();
            
            $statement->fetch();
            $statement->close();
            $category = CategoryDB::getCategory($category_id);
            return self::loadProduct($category, $product_id, $code, 
                    $name, $description, $price, $discount_percent);
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }
    
    public static function addProduct($product) {
        $db = Database::getDB();
        $query = 'INSERT INTO products
                    (categoryID, productCode, productName, description,
                     listPrice, discountPercent, dateAdded)
                  VALUES
                    (?, ?, ?, ?, ?, ?, NOW())';

        try {
            $statement = $db->prepare($query);
            $category_id = $product->getCategory()->getID();
            $code = $product->getCode();
            $name = $product->getName();
            $desc = $product->getDescription();
            $price = $product->getPrice();
            $percent = $product->getDiscountPercent();
            $statement->bind_param("isssdd", $category_id, $code, $name, $desc,
                                   $price, $percent);
            $statement->execute();
            $statement->close();
            return $db->insert_id;
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }
    
    public static function updateProduct($product) {
        $db = Database::getDB();
        $query = 'UPDATE Products
                  SET categoryID = ?, productCode = ?, productName = ?,
                      description = ?, listPrice = ?, discountPercent = ?
                  WHERE productID = ?';

        try {
            $statement = $db->prepare($query);
            $category_id = $product->getCategory()->getID();
            $product_id = $product->getID();
            $code = $product->getCode();
            $name = $product->getName();
            $desc = $product->getDescription();
            $price = $product->getPrice();
            $percent = $product->getDiscountPercent();
            $statement->bind_param("isssddi", $category_id, $code, $name, 
                $desc, $price, $percent, $product_id);
            
            $statement->execute();
            $statement->close();
            return $db->affected_rows;
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }
    
    public static function deleteProduct($product_id) {
        $db = Database::getDB();
        $query = 'DELETE FROM products
                  WHERE productID = ?';

        try {
            $statement = $db->prepare($query);
            $statement->bind_param("i", $product_id);
            $statement->execute();
            $statement->close();
            return $db->affected_rows;
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }
}
?>