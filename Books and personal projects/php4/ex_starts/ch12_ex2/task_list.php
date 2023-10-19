<!DOCTYPE html>
<html>
<head>
    <title>Task List Manager</title>
    <link rel="stylesheet" href="main.css"/>
</head>
<body>
    <header>
        <h1>Task List Manager</h1>
    </header>
    <main>
        <!-- part 1: the errors -->
        <?php if (is_array($errors) && count($errors) > 0) : ?>
        <h2>Errors</h2>
        <ul>
            <?php foreach($errors as $error) : ?>
                <li><?php echo htmlspecialchars($error); ?></li>
            <?php endforeach; ?>
        </ul>
        <?php endif; ?>

        <!-- part 2: the tasks -->
        <h2>Tasks</h2>
        <?php if (is_array($task_list) && count($task_list) > 0) : ?>
            <ul>
            <?php foreach( $task_list as $id => $task ) : ?>
                <li><?php echo $id + 1 . '. ' . 
                        htmlspecialchars($task); ?></li>
            <?php endforeach; ?>
            </ul>
        <?php else: ?>
            <p>There are no tasks in the task list.</p>
        <?php endif; ?>
        <br>

        <!-- part 3: the add form -->
        <h2>Add Task</h2>
        <form action="." method="post" >
            <?php if (is_array($task_list) && count($task_list) > 0) : ?>
                <?php foreach( $task_list as $task ) : ?>
                    <input type="hidden" name="tasklist[]" 
                           value="<?php echo htmlspecialchars($task); ?>">
                <?php endforeach; ?>
            <?php endif; ?>
                    
            <input type="hidden" name="action" value="add">
            <label>Task:</label>
            <input type="text" name="newtask" id="newtask" > <br>
            <label>&nbsp;</label>
            <input type="submit" value="Add Task">
        </form>
        <br>

        <!-- part 4: the delete form -->
        <?php if (is_array($task_list) && count($task_list) > 0) : ?>
        <h2>Delete Task</h2>
        <form action="." method="post" >
            <?php foreach( $task_list as $task ) : ?>
              <input type="hidden" name="tasklist[]" 
                     value="<?php echo htmlspecialchars($task); ?>">
            <?php endforeach; ?>
            <input type="hidden" name="action" value="delete">
            <label>Task:</label>
            <select name="taskid">
                <?php foreach($task_list as $id => $task) : ?>
                    <option value="<?php echo $id; ?>">
                        <?php echo htmlspecialchars($task); ?>
                    </option>
                <?php endforeach; ?>
            </select>
            <br>
            <label>&nbsp;</label>
            <input type="submit" value="Delete Task">
        </form>
        <?php endif; ?>
    </main>
</body>
</html>