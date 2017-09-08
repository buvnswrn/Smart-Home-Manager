<? PHP      
session_start();
?>

<?PHP

$_SESSION["loggedInUser"] = $username;


    try {
        // open connection to MongoDB server
        $conn = new Mongo('localhost');

        // access database
        $db = $conn->test;

        // access collection
        $collection = $db->items;


        $userName = $_POST['username'];
        $userPass = $_POST['userPassword'];


        $user = $db->$collection->findOne(array('username'=> 'user1', 'password'=> 'pass1'));

        foreach ($user as $obj) {
            echo 'Username' . $obj['username'];
            echo 'password: ' . $obj['password'];
            if($userName == 'user1' && $userPass == 'pass1'){
                echo 'found'            
            }
            else{
                echo 'not found'            
            }

        }

        // disconnect from server
        $conn->close();

    } catch (MongoConnectionException $e) {
        die('Error connecting to MongoDB server');
    } catch (MongoException $e) {
        die('Error: ' . $e->getMessage());
    }

$_SESSION["loggedInUser"] = $correct;

?>