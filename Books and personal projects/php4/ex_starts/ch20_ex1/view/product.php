<h1><?php echo $product->getName(); ?></h1>
<div id="left_column">
    <p><img src="<?php echo $product->getImagePath($app_path); ?>"
            alt="<?php echo $product->getImageAltText(); ?>" /></p>
</div>

<div id="right_column">
    <p><b>List Price:</b>
        <?php echo '$' . $product->getPrice(); ?></p>
    <p><b>Discount:</b>
        <?php echo $product->getDiscountPercentFormatted() . '%'; ?></p>
    <p><b>Your Price:</b>
        <?php echo '$' . $product->getDiscountPriceFormatted(); ?>
        (You save <?php echo '$' . $product->getDiscountAmountFormatted(); ?>)</p>
    <form action="<?php echo $app_path . 'cart' ?>" method="post">
        <input type="hidden" name="action" value="add">
        <input type="hidden" name="product_id"
               value="<?php echo $product->getID(); ?>">
        <b>Quantity:</b>
        <input type="text" name="quantity" value="1" size="2">
        <input type="submit" value="Add to Cart">
    </form>
    <h2 class="no_bottom_margin">Description</h2>
    <?php echo add_tags($product->getDescription()); ?>
</div>
