<?php

$name= "localhost";
$uname= "root";
$password = "";

$db_name = "test_db";

$conn = mysqli_connect($name, $uname, $password, $db_name,4306);

if (!$conn) {
	echo "Connection failed!";
}

?>