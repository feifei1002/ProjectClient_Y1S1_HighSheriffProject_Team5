document.getElementById("downloadButton").style.visibility = "hidden";
var videoChunks = []; // Apparently the video is stored in blobs on chunks and we need to save them here
var options = {mimeType: 'video/webm;codecs=vp9'};

function checkUserIsCompatible(){ // Checks if the user's browser supports user media
    var check = !!(navigator.mediaDevices.getUserMedia);
    if(check){
        const constraints = {video: { width: 1024, height: 576}, audio: true};
        const video = document.getElementById("webcam");
        navigator.mediaDevices.getUserMedia(constraints).then((stream) => {video.srcObject = stream;}); // Aks the user for permission then plays their own webcame to them
        prepMediaRecorder(constraints);
    } else {
        document.getElementById("checkComp").style = "display: block;";
    }
}

async function prepMediaRecorder(constraints){ // Async function to get the user's webcam and prepare it for recording
    let stream = null;

    try{
        stream = await navigator.mediaDevices.getUserMedia(constraints);
        mediaRecorder = new MediaRecorder(stream, options);
        mediaRecorder.ondataavailable = handleDataAvailable;
    } catch(error){
        alert("Error");
    }
}

function record(){
    mediaRecorder.start();
    document.getElementById("recordStatus").innerHTML = "Recording...";
}

function stop(){
    mediaRecorder.stop();
    document.getElementById("recordStatus").innerHTML = "Recording Saved";
}

function play(){
    var videoPlayback = document.getElementById("playback");
    var downloadButton = document.getElementById("downloadButton");
    var superBuffer = new Blob(videoChunks);
    videoPlayback.src = window.URL.createObjectURL(superBuffer);
    document.getElementById("downloadButton").style.visibility = "visible";
    downloadButton.href = window.URL.createObjectURL(superBuffer);
}

function handleDataAvailable(event){ // Stores video into the video chunks array
    if(event.data.size > 0){
        videoChunks.push(event.data);
    }
}
checkUserIsCompatible()