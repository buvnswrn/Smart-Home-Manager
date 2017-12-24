<?php 
require 'vendor/autoload.php';
$m =new MongoDB\Client;
foreach ($m->listDatabases() as $databaseInfo) {
    var_dump($databaseInfo);
}
$db=$m->shm;
$coll=$db->users;
$cursor=$coll->find();
foreach ($cursor as $document) {
    echo $document["name"] . "\n";
}
?>