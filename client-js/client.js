//var io = require('socket.io-client');
var socket = io.connect('http://localhost:5000', {reconnect: true});

//connect listener
socket.on('connect', function (socket) {
    console.log('Connected!');
});

//response listener
socket.on('response', function (ret) {
    console.log(ret);
    emit('thank you my server!');
});

//message sender
var emit = function(text){
  socket.emit('client_message', text);
}
