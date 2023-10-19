<?php include '../../view/header.php'; ?>
<?php include '../../view/sidebar_admin.php'; ?>
<?php

if (isset($product)) {
    $heading_text = 'Edit Product';
    $action = 'update_product';
    $category_id = $product->getCategory()->getID();
    $code = htmlspecialchars($product->getCode());
    $name = htmlspecialchars($product->getName());
    $price = $product->getPrice();
    $discount = $product->getDiscountPercent();
    $description = htmlspecialchars($product->getDescription());
} else {
    $heading_text = 'Add Product';
    $action = 'add_product';
    $category_id = '';
    $code = '';
    $name = '';
    $price = '';
    $discount = '';
    $description = '';
}
?>
<section>
    <h1>Product Manager - <?php echo $heading_text; ?></h1>
    <form action="index.php" method="post" id="add_edit_product_form">
        <input type="hidden" name="action" 
               value="<?php echo $action; ?>" />
        <input type="hidden" name="category_id" 
               value="<?php echo $category_id; ?>" />
        <input type="hidden" name="product_id"
               value="<?php echo $product_id; ?>" />

        <label>Category:</label>
        <select name="category_id">
        <?php foreach ($categories as $category) : 
            $selected = '';
            if ($category->getID() == $category_id) {
                $selected = 'selected';
            }
        ?>
            <option value="<?php echo $category->getID(); ?>" 
                <?php echo $selected; ?>><?php echo $category->getName(); ?>
            </option>
        <?php endforeach; ?>
        </select><br>

        <label>Code:</label>
        <input type="text" name="code" value="<?php echo $code; ?>"><br>

        <label>Name:</label>
        <input type="text" name="name" value="<?php echo $name; ?>"><br>

        <label>List Price:</label>
        <input type="text" name="price" value="<?php echo $price; ?>"><br>

        <label>Discount Percent:</label>
        <input type="text" name="discount_percent" 
               value="<?php echo $discount; ?>"><br>

        <label>Description:</label>
        <textarea name="description" rows="10">
                      <?php echo $description; ?></textarea><br>

        <label>&nbsp;</label>
        <input type="submit" value="Submit">
    </form>
    
    <div id="formatting_directions">
        <h2>How to format the Description entry</h2>
        <ul>
            <li>Use two returns to start a new paragraph.</li>
            <li>Use an asterisk to mark items in a bulleted list.</li>
            <li>Use one return between items in a bulleted list.</li>
            <li>Use standard HMTL tags for bold and italics.</li>
        </ul>
    </div>
</section>
<?php include '../../view/footer.php'; ?>