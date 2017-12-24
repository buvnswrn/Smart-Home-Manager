<!DOCTYPE html>
<html>
<head>

    <title>
        User Profile
    </title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta charset='utf-8'>
    
    <link rel='stylesheet' href='css/req_style.css'>
    <script id='jsbin-javascript' src='js/Webcam.js'></script>
    <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
    <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
   <link href='https://fonts.googleapis.com/css?family=Dosis|Raleway' rel='stylesheet'>
</head>
<body>
<div id='container'>
    <div id='header'>
        <center><h1>Smart Home Manager </h1></center>
    </div>
    <div id='body'>
    <?php
    require 'vendor/autoload.php';
    /*connection*/
    $client = new MongoDB\Client;
    $shm = $client->shm;
    $data = $shm->data;
    $user_datas=$data->find();
    $i=0;    
foreach ($user_datas as $data){
            echo ("<div id='content' >
            <div id='nameimage'>
            <div id='edit' class='editing'><b> <strong> &nbsp;Edit </strong></b></div>Name:<p id='name'>".$data->Name."</p>
                <div id='image'>
            <div id='obj-id'>".$data->_id."</div>
                    Image:<br>
                    <img src='".$data->Image."'> 
                </div>
            </div><br>
            <div id='req'>
                <div id='item'>
                    Fan:<label class='switch'>
                        <input type='checkbox'".$data->Fan." disabled>
                        <span class='slider'></span>
                        </label> &nbsp;&nbsp;&nbsp;
                </div>

                <div id='item'>Light:<label class='switch'>
                    <input type='checkbox'".$data->Light." disabled>
                    <span class='slider'></span>
                    </label>
                </div>

                <div id='item'>Modem:<label class='switch' >
                    <input type='checkbox'".$data->Modem." disabled>
                    <span class='slider'></span>
                    </label>
                </div>

                <div id='item'>Tv:<label class='switch'>
                    <input type='checkbox'".$data->TV." disabled>
                    <span class='slider'></span>
                    </label>
                </div>

                <div id='item'>Music System:<label class='switch'>
                    <input type='checkbox'".$data->Music_System." disabled>
                    <span class='slider'></span>
                    </label>
                </div>
            </div>
            <div id='delete' class='del'>Delete</div>
        </div>");
        $i++;
            }
?>
    <div id='add'>
            <button class='w3-button w3-xlarge w3-circle w3-blue' id='mod' data-toggle='modal' data-target='#myModal' onclick='startcamera()'>+</button>
    </div>
        <div class='modal fade' id='myModal' role='dialog'>
            <div class='modal-dialog'>
            
            
            <div class='modal-content'>
                <div class='modal-header'>
                <button type='button' class='close' data-dismiss='modal' onclick='closecamera()'>&times;</button>
                <h4 class='modal-title' id="modal_heading">Add A Person</h4>
                </div>
                <div class='modal-body'>
                    <form id="req-form" enctype="multipart/form-data" action="req_mongodb.php" method="post">
                        Name:<input type='text' placeholder='Enter Your Name'name="name" id="mod-name"/><br>
                            <div>
                                Image:<br>
                                
                                <video id='video'>video</video><br>
                                
                                <div>
                                    <canvas id='canvas' style='display:none'></canvas>
                                </div><br><button id='ClickPic'>Take photo</button><br>
                                <input type="hidden" value="" id="capturedImage" name="Imagedata"/>
                            </div>
                            <input id="user-id" style="display:none" value="" name="user-id"></input>
                            <div id='req'>
                                    <div id='item'>Fan:<label class='switch'>
                                            <input type='checkbox'class="cb" name="reqs[]" value="Fan" >
                                            <span class='slider'></span>
                                            </label> &nbsp;&nbsp;&nbsp;
                                    </div>

                                    <div id='item'>Light:<label class='switch'>
                                        <input type='checkbox' class="cb" name="reqs[]" value='Light'>
                                        <span class='slider'></span>
                                        </label>
                                    </div>

                                    <div id='item'>Modem:<label class='switch'>
                                        <input type='checkbox' class="cb" name="reqs[]" value='Modem'>
                                        <span class='slider'></span>
                                        </label>
                                    </div>

                                    <div id='item'>Tv:<label class='switch'>
                                        <input type='checkbox' class="cb" name="reqs[]" value='TV'>
                                        <span class='slider'></span>
                                        </label>
                                    </div>

                                    <div id='item'>Music System:<label class='switch'>
                                        <input type='checkbox' class="cb" name="reqs[]" value='Music_System'>
                                        <span class='slider'></span>
                                        </label>
                                    </div>
                            </div>
                            <input type="submit" id='submit' name="action" value="Submit" />
                            <input type="submit" id="update" name="action" value="Update"/>
                    </form>

                </div>
                <div class='modal-footer'>
                    <p>&copy;Smart Home Manager</p>
                </div>
            </div>
            
            </div>
            
        </div>
    </div>
</div>
<script>
$('.editing').click(function(){
    var $this= $ (this).parent();
    name=$this.find('#name').text();
    id=$this.find('#obj-id').text();
    console.log("Name: "+name);
    console.log("Id: "+id);
    // $this.children('#edit').click(function(){
    $('#mod').click();
    $('#submit').hide();
    $('#update').show();
    $('#user-id').val(id);
    $('#mod-name').val(name);
    $('#modal_heading').text("Edit Your Details");
    // });
});
$('.del').click(function(){
    var $this=$ (this).parent();
    id=$this.find('#obj-id').text();
    $.ajax({
        type:"POST",
        url:'req_mongodb.php',
        data:{
            action:"Delete",
            obj_id:id},
        success: function(resultData){
          //alert(resultData+" Id:"+id);
          location.reload();
      }
        
        }).done(function(o) {
          console.log('deleted');
    });
})
</script>

</body>
</html> 

    
    


