<?php

// start the session with a persistent cookie of 1 year
$lifetime = 60 * 60 * 24 * 365;             // 1 year in seconds
session_set_cookie_params($lifetime, '/');
session_start();

if (!isset($_SESSION['tasklist'])) {
    $_SESSION['tasklist'] = [];
}
$action = filter_input(INPUT_POST, 'action');

// always reset error array - deletes any previous error messages
$_SESSION['errors'] = [];

switch($action) {
    case 'add':
        $new_task = filter_input(INPUT_POST, 'newtask');
        if (empty($new_task)) {
            $_SESSION['errors'][] = 'The new task cannot be empty.';
        } else {
            $_SESSION['tasklist'][] = $new_task;
        }
        header('Location: task_list.php');
        break;
    case 'delete':
        $task_index = filter_input(INPUT_POST, 'taskid', FILTER_VALIDATE_INT);
        if ($task_index === NULL || $task_index === FALSE) {
            $_SESSION['errors'][] = 'The task cannot be deleted.';
        } else {
            unset($_SESSION['tasklist'][$task_index]);
            $_SESSION['tasklist'] = array_values($_SESSION['tasklist']);
        }
        header('Location: task_list.php');
        break;
    default:
        include('task_list.php');
        break;
}

?>