<?php
class Database {
    private static $host = 'localhost';
    private static $username = 'mgs_user';
    private static $password = 'pa55word';
    private static $database = 'my_guitar_shop2';
    private static $db;

    private function __construct() {}

    public static function getDB () {
        if (!isset(self::$db)) {
            try {
                self::$db = new mysqli(self::$host, 
                                       self::$username, 
                                       self::$password, 
                                       self::$database);                
            } catch (mysqli_sql_exception $e) {
                self::displayError($e->getMessage());
            }
        }
        return self::$db;
    }
    
    public static function displayError($error_message) {
        global $app_path;
        include 'errors/db_error.php';
        exit();
    }
}
?>