
  $(document).ready(function () {
  

  const MAX_DATA_COUNT = 10;
  //connect to the socket server.
  //   var socket = io.connect("http://" + document.domain + ":" + location.port);
  var socket = io.connect();

    //receive player details from server
  socket.on("updatePlayerData", function (msg) {
    console.log("Received playyer Data :: " + msg.row_num + " :: " + msg.username+ " :: " + msg.right+ " :: " + msg.wrong);

  });
  
  //recive a new question from the server
  socket.on("newQuestion", function (msg) {
    console.log("Received new question :: " + msg.question + " :: " + msg.answer1+ " :: " + msg.answer2+ " :: " + msg.answer3);
    

  });
});