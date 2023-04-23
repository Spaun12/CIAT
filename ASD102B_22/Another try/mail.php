<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $message = $_POST["message"];

    $to = "michael.connell.techvet@gmail.com";
    $subject = "New message from your website";
    $headers = "From: " . $email . "\r\n" .
               "Reply-To: " . $email . "\r\n" .
               "Content-Type: text/plain; charset=UTF-8";

    if (mail($to, $subject, $message, $headers)) {
        header("Location: contact.html?mailsent");
    } else {
        header("Location: contact.html?mailerror");
    }
}
?>
