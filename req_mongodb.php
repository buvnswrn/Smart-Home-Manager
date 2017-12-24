<?php 
require 'vendor/autoload.php';
/*connection*/
header("Location: http://localhost/Smart-Home-Manager-master/req.php", true, 301);

$client = new MongoDB\Client;
$shm = $client->shm;
$data = $shm->data;
if($_POST["action"]=="Delete"){
$id=$_POST["obj_id"];
$deleteResult=$data->deleteOne(["_id"=>new \MongoDB\BSON\ObjectID($id)]);
//printf("Deleted %d document(s)\n", $deleteResult->getDeletedCount());
//echo($id);
}
else{
$name=$_POST["name"];
$req=$_POST["reqs"];
$img=$_POST["Imagedata"];
$id=$_POST["user-id"];
//echo "<div>".$name."</div>";
/*$reqs=array(
	"Name"=>'No',
	"Fan"=>'No',
	"Light"=>'No',
	"Music System"=>'No',
	"Modem"=>'No',
	"TV"=>'No'
);*/

$a = array('Fan', 'Light', 'Music_System', 'TV', 'Modem');

$reqs["Name"]=$name;
$reqs["Image"]=$img;
	foreach($a as $i) {
	$reqs[$i] = ' ';
}


foreach($req as $item){
	$reqs[$item] = 'Checked';
}

// echo "The Array is seen like :";
// var_dump($reqs);
// echo 'Your Ugly Face:<img src="'.$img.'" />';
if($_POST["action"]=="Submit"){
$result=$data->insertOne($reqs);
exit();
}
if($_POST["action"]=="Update"){
	echo $id;
	$result=$data->replaceOne(['_id'=>new \MongoDB\BSON\ObjectID($id)],$reqs);
	// printf("Matched %d document(s)\n", $result->getMatchedCount());
	// printf("Modified %d document(s)\n", $result->getModifiedCount());
	// echo "Action here is update";
	exit();
}
}
?> 
