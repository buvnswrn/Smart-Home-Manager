<?php 
require 'vendor/autoload.php';
/*connection*/
$client = new MongoDB\Client;
$shm = $client->shm;
$users = $shm->users;
/*Collecting User details*/
$name = $_POST["mail"];
$pwd = $_POST["pass"];
$pwd = sha1($pwd);

$query = array(
    '$and'=> array(
    array("email"=>$name),
    array("password"=>$pwd)
                )
    );
    
    // print_r($query);
$details=$users->findOne($query);
// print_r($details);
if($details){
header('Location:req.php');
}
else{
    echo 'fucked';
}
?>