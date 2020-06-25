//The peer var
var peer = new Peer();
var conn = null;

let video = document.getElementById('video')
let canvas = document.getElementById('canvas')
let snap = document.getElementById('snap')
let constraint = { audio: true, video: { width: 1280, height: 720 } };
let otherId = ''



//The mediaStream object


//To display the peer ID
function getPeerId() {
    //display the peer Id on the Page
    div = document.createElement('div')
    div.innerHTML = peer._id
    div.id = "PeerId"
    doc = document.getElementById("myId")
    doc.appendChild(div)

}

// peer.on('connection', function (conn) {
//     console.log("connected to peer")
//     conn.on('data', function (data) {
//         // Will print 'hi!'
//         console.log(data);
//     });
// });


peer.on('call', call => {
    console.log("IncomingCall")
    navigator.mediaDevices.getUserMedia(constraint)
        .then(stream => {
            console.log("Streaming")
            call.answer(stream)
            call.on('stream', rmtStream => {
                video.srcObject = rmtStream


            })
        })
})
function connectToPeer() {
    console.log("calling..")
    otherId = document.getElementById('IncomingPeerId').value

    console.log(otherId)
    if (otherId != peer._id) {
        navigator.mediaDevices.getUserMedia(constraint)
            .then(stream => {
                call = peer.call(otherId, stream)
                call.on("stream", rmtStream => {
                    video.srcObject = rmtStream
                }

                )
            })
    }else{
        console.error("Don't Enter the Same Peer Id as the Destination Peer ID")
    }
}
//When someone calls 
//peer.on('call') returns a promise
//then Create a new mediaStream Object using getUSerMedia
//this also returns a promise
//then answer the call 
//this also returns a promise
//then show the stream in the canvas
//if error occurs console.log("error")
//When Somone calls
//-------------------------------Actual iimplementation---------------------------------------
// peer.on('call', function(call) {
//   getUserMedia({video: true, audio: true}, function(stream) {
//     call.answer(stream); // Answer the call with an A/V stream.
//     call.on('stream', function(remoteStream) {
//       video.srcObj = stream;
//     });
//   }, function(err) {
//     console.log('Failed to get local stream' ,err);
//   });
// });
//------------------------------------------------------------------------------------

// This is just to create a connection with the peer
async function handleConnect() {
    id = document.getElementById('IncomingPeerId').value
    stream = await navigator.mediaDevices.getUserMedia(constraint)
    var call = peer.call(id, stream)
    remoteStream = await call.on('stream')
    video.srcObj = remoteStream


}

//Get a mediaStream object .. this returns a promise
//then call the peer using his/her id this also returns a promise
//the await untill the   stream is available using call.on('stream') this also returns a promise
//when it is finally available render the media on the canvas..

// getUserMedia({video: true, audio: true}, function(stream) {
//     var call = peer.call('another-peers-id', stream);
//     call.on('stream', function(remoteStream) {
//       // Show stream in some video/canvas element.
//     });
//   }, function(err) {
//     console.log('Failed to get local stream' ,err);
//   });

//When another peer connects 
//when data is sent 
// console.log(data)
    // peer.on('connection',function (connectObj) {
    //     console.log("Incoming connection")
    //     connectObj.on('data',function (data) {
    //             console.log("Recieved:")
    //             console.log(data)
    //             })

    //     })



//Capturing from the webcam
//this is only for modern browsers to declare that every variables must be declared//


//access webcam
// async function init(){
//     try {
//         let  stream  = await getUserMedia(constraint);
//         handleSucess(stream);
//     }catch(e){
//         console.log("Error:" + e)
//     }
// }

// //success
// function handleSucess(stream){
//     window.stream = stream
//     video.srcObjec = stream
// }

// //load init()
// init()

// //draw Image
// var context  = canvas.getContext('2d');
// snap.addEventListener('click',function(){context.drawImage(video,0,0,640,480);
// });










//this worked!!
// navigator.mediaDevices.getUserMedia(constraint)
// .then(stream => {
// call = peer.call("uoj59rt4c0r00000",stream)
// call.on("stream",rmtStream => {
// video.srcObject = rmtStream
// }

// )
// })







// peer.on('call',call => {
//     console.log("IncomingCall")
//     navigator.mediaDevices.getUserMedia(constraint)
//     .then(stream => {
//         console.log("Streaming")
//         call.answer(stream)
//         call.on('stream',rmtStream => {
//         video.srcObject = rmtStream

//     })
//     })
//     })