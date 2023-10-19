<?php
namespace cart {
    // Add an item to the cart
    function add_item(string $key, int $quantity, array $product) {
        if ($quantity > 0) {
            // If item already exists in cart, update quantity
            if (isset($_SESSION['cart13'][$key])) {
                $quantity += $_SESSION['cart13'][$key]['qty'];
                update_item($key, $quantity);
            } else { 
                // Add item
                $item = [
                    'name' => $product['name'],
                    'cost' => $product['cost'],
                    'qty'  => $quantity,
                    'total' => $product['cost'] * $quantity,
                ];
                $_SESSION['cart13'][$key] = $item;
            }
        }
    }

    // Update an item in the cart
    function update_item(string $key, int $quantity) {
        if (isset($_SESSION['cart13'][$key])) {
            if ($quantity <= 0) {
                unset($_SESSION['cart13'][$key]);
            } else {
                $_SESSION['cart13'][$key]['qty'] = $quantity;
                $total = $_SESSION['cart13'][$key]['cost'] *
                         $_SESSION['cart13'][$key]['qty'];
                $_SESSION['cart13'][$key]['total'] = $total;
            }
        }
    }

    // Get cart subtotal
    function get_subtotal() {
        $subtotal = 0;
        foreach ($_SESSION['cart13'] as $item) {
            $subtotal += $item['total'];
        }
        $subtotal_f = number_format($subtotal, 2);
        return $subtotal_f;
    }
    
    // get a function for  sorting the cart on the specified key
    function compare_factory(string $sort_key) {
        return fn($left, $right) => $left[$sort_key] <=> $right[$sort_key];
    }

    // Sort the cart on the specified key
    function sort(string $sort_key) {
        $sort_function = compare_factory($sort_key);
        uasort($_SESSION['cart13'], $sort_function);
    }
}
?>