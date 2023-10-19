<?php include 'view/header.php'; ?>
<?php include 'view/sidebar.php'; ?>
<section>
    <h1>Featured products</h1>
    <p>My Guitar Shop has a great selection of
        musical instruments including guitars, basses, and drums. And we're
        constantly adding more to give you the best selection possible!
    </p>
    <table>
    <?php foreach ($products as $product) : ?>
        <tr>
            <td class="product_image_cell">
                <img src="images/<?php echo $product->getCode(); ?>_s.png"
                     alt="&nbsp;">
            </td>
            <td class="product_info_cell">
                <p>
                    <a href="catalog?action=view_product&amp;product_id=<?php 
                              echo $product->getCode(); ?>">
                        <?php echo $product->getName(); ?>
                    </a>
                </p>
                <p>
                    <b>Your price:</b>
                    $<?php echo $product->getDiscountPriceFormatted(); ?>
                </p>
                <p>
                    <?php echo get_first_paragraph($product->getDescription()); ?>
                </p>
            </td>
        </tr>
    <?php endforeach; ?>
    </table>
</section>
<?php include 'view/footer.php'; ?>