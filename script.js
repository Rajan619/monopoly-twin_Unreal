let video = document.getElementById("video");
let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

let startBtn = document.getElementById("startBtn");
let status = document.getElementById("status");
let log = document.getElementById("log");

let previousFrame = null;
let visionReady = false;

function logMsg(msg){
log.innerText = msg + "\n" + log.innerText;
}

function waitForOpenCV(){

if(typeof cv !== "undefined"){
status.innerText = "OpenCV Ready";
visionReady = true;
}else{
setTimeout(waitForOpenCV,200);
}

}

waitForOpenCV();

startBtn.onclick = async function(){

if(!visionReady){
alert("OpenCV still loading");
return;
}

const stream = await navigator.mediaDevices.getUserMedia({
video:{
facingMode:"environment",
width:{ideal:640},
height:{ideal:640}
}
});

video.srcObject = stream;

video.onloadedmetadata = ()=>{
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;

status.innerText="Camera running";

requestAnimationFrame(processFrame);
};

};

function processFrame(){

ctx.drawImage(video,0,0,canvas.width,canvas.height);

let src = cv.imread(canvas);

let gray = new cv.Mat();
cv.cvtColor(src,gray,cv.COLOR_RGBA2GRAY);

if(previousFrame){

let diff = new cv.Mat();
cv.absdiff(gray,previousFrame,diff);

let motion = cv.mean(diff)[0];

if(motion>10){
status.innerText="Motion detected (hand?)";
}else{
status.innerText="Board stable";
}

diff.delete();
}

previousFrame = gray.clone();

src.delete();
gray.delete();

requestAnimationFrame(processFrame);

}
