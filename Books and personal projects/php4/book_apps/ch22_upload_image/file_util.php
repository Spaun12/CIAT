<?php
function get_file_list($path) {
    $files = [];
    
    if (is_dir($path)) {
        $items = scandir($path);
        foreach ($items as $item) {
            $item_path = $path . DIRECTORY_SEPARATOR . $item;
            if (is_file($item_path)) {
                $files[] = $item;
            }
        }
    }
    return $files;
}
?>
