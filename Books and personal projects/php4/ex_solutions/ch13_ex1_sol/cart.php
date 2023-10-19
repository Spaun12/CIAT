<?php

namespace murach\cart {

    // Add an item to the cart
    function add_item(array &$cart, string $key, int $quantity, array $product) {
        if ($quantity > 0) {
            // If item already exists in cart, update quantity
            if (isset($cart[$key])) {
                $quantity += $cart[$key]['qty'];
                update_item($cart, $key, $quantity);
            } else { 
                // Add item
                $item = [
                    'name' => $product['name'],
                    'cost' => $cost = $product['cost'],
                    'qty'  => $quantity,
                    'total' => $cost = $product['cost'] * $quantity,
                ];
                $cart[$key] = $item;
            }
        }
    }

    // Update an item in the cart
    function update_item(array &$cart, string $key, int $quantity) {
        if (isset($cart[$key])) {
            if ($quantity <= 0) {
                unset($cart[$key]);
            } else {
                $cart[$key]['qty'] = $quantity;
                $total = $cart[$key]['cost'] *
                         $cart[$key]['qty'];
                $cart[$key]['total'] = $total;
            }
        }
    }

    // Get cart subtotal
    function get_subtotal(array $cart, int $decimals = 2) {
        $subtotal = 0;
        foreach ($cart as $item) {
            $subtotal += $item['total'];
        }
        $subtotal_f = number_format($subtotal, $decimals);
        return $subtotal_f;
    }
}
?>