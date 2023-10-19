<?php
class CategoryDB {
    public static function getCategories() {
        $db = Database::getDB();
        $query = 'SELECT categoryID, categoryName 
                  FROM categories 
                  ORDER BY categoryID';
        
        try {
            $result = $db->query($query);            
            $categories = [];
            for ($i = 0; $i < $result->num_rows; $i++) {
                $row = $result->fetch_assoc();
                $categories[] = new Category($row['categoryID'],
                                             $row['categoryName']);
            }
            $result->free();
            return $categories;
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }

    public static function getCategory($category_id) {
        $db = Database::getDB();
        $query = 'SELECT categoryID, categoryName 
                  FROM categories 
                  WHERE categoryID = ?';

        try {
            $statement = $db->prepare($query);
            $statement->bind_param("i", $category_id);
            $statement->bind_result($id, $name);
            $statement->execute();
            $statement->fetch();
            $statement->close();
            return new Category($id, $name);
        } catch (mysqli_sql_exception $e) {
            Database::displayError($e->getMessage());
        }
    }
}
?>