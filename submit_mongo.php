<?php
require 'vendor/autoload.php';
/*connection*/
$client = new MongoDB\Client;
$shm = $client->shm;
$users = $shm->users;
/*Collecting User details*/
$name = $_POST["user"];
$pwd = $_POST["pass"];
$pwd = sha1($pwd);
$mail = $_POST["mail"];

/*Creating a Document*/
$details = array(
    "name"=>$name,
    "password"=>$pwd,
    "email"=>$mail
);
/*inserting (insert one is used to insert a single document,insert() shows error here, donno wtf is tat )*/
$result = $users->insertOne($details);
//echo "User:".$name." pass:".$pwd." mailid:".$mail.".";
echo "Account Creation Successful";
header('Location:index.html');



?>