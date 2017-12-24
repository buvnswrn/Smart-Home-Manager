var globalstream;
// function edit($i) {
// console.log("Fucked");
// var data=document.getElementsByName("content-"+$i)[0];
// var name=data.find('#name');
// console.log(data);
// }
    function startcamera() {
  
      var streaming = false,
          video        = document.querySelector('#video'),
          canvas       = document.querySelector('#canvas'),
          startbutton  = document.querySelector('#startbutton'),
          width = 320,
          height = 0;
    
      navigator.getMedia = ( navigator.getUserMedia ||
                             navigator.webkitGetUserMedia ||
                             navigator.mozGetUserMedia ||
                             navigator.msGetUserMedia);
    
      navigator.getMedia(
        {
          video: true,
          audio: false
        },
        function(stream) {
            globalstream=stream;
          if (navigator.mozGetUserMedia) {
            video.mozSrcObject = globalstream;
          } else {
            var vendorURL = window.URL || window.webkitURL;
            video.src = vendorURL.createObjectURL(globalstream);
          }
          video.play();
        },
        function(err) {
            console.log('An error occured! ' + err);
        }
      );
     
      video.addEventListener('canplay', function(ev){
        if (!streaming) {
          height = video.videoHeight / (video.videoWidth/width);
          video.setAttribute('width', width);
          video.setAttribute('height', height);
          canvas.setAttribute('width', width);
          canvas.setAttribute('height', height);
          streaming = true;
        }
      }, false);
    
      function takepicture() {
        canvas.width = width;
        canvas.height = height;
        canvas.getContext('2d').drawImage(video, 0, 0, width, height);
        var data = canvas.toDataURL();
        
        console.log(data);
        document.getElementById('capturedImage').value = data;
        //document.getElementsById('submit').disabled=false;
        /*$.ajax({
          type: "POST",
          url: "req_mongodb.php",
          data: { 
             imgBase64: data
          }
        }).done(function(o) {
          console.log('saved'); 
         
        });*/
        video.style.display='none';
        canvas.style.display='inline';
      }
      
    
      ClickPic.addEventListener('click', function(ev){
        console.log('removed');
        takepicture();
        ev.preventDefault();
      }, false);
     
    }
    function closecamera(){
        video= document.querySelector('#video');
        canvas= document.querySelector('#canvas');
        video.style.display='';
        video.pause();
        video.src='';
        globalstream.getTracks()[0].stop();
        console.log('released');
        canvas.style.display='none'; 
        }
    function printreq(){
        var checkedValue = null; 
        var inputElements = document.getElementsByClassName('cb');
        for(var i=0; inputElements[i]; ++i){
              if(inputElements[i].checked){
                   checkedValue = inputElements[i].value;
                   console.log(checkedValue);
                
              }
        }        
    }