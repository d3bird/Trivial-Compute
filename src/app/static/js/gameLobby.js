
  $(document).ready(function () {
  

  const MAX_DATA_COUNT = 10;
  //connect to the socket server.
  //   var socket = io.connect("http://" + document.domain + ":" + location.port);
  var socket = io.connect();

    //receive player details from server
  socket.on("updatePlayerData", function (msg) {
    console.log("Received playyer Data :: " + msg.row_num + " :: " + msg.username+ " :: " + msg.right+ " :: " + msg.wrong);

    if (msg.row_num == "none") {
        console.log("can not not update if row is none");
        return;
    }
    let row = msg.row_num [msg.row_num .length - 1];

    document.getElementById("playersTable").rows[row].cells[0].innerHTML = msg.username;
    document.getElementById("playersTable").rows[row].cells[1].innerHTML = msg.sql_id;
    document.getElementById("playersTable").rows[row].cells[2].innerHTML = row;
    document.getElementById("playersTable").rows[row].cells[3].innerHTML = msg.wrong;
    document.getElementById("playersTable").rows[row].cells[4].innerHTML = msg.right;

    //Received playyer Data :: none :: guest :: 0 :: 0
    //Received playyer Data :: player3 :: zxc :: 0 :: 0
  });
  
  //recive a new question from the server
  socket.on("newQuestion", function (msg) {
    console.log("Received new question :: " + msg.question + " :: " + msg.answer1+ " :: " + msg.answer2+ " :: " + msg.answer3);
    

  });
});