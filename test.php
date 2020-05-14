<?php
    $command = escapeshellcmd('python testing.py');
    $output = shell_exec($command);
    echo $output;
?>