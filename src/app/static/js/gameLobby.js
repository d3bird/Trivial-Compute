//set all the vars for the players 

//the size of each board square
//needed to caluculate possition to move the player
const width = 50
const height = 50

//the base colors of the board
red = "rgb(200 0 0)";//red
green = "rgb(9 200 0)";//green
blue = "rgb(0 0 200)";//blue
yellow = "rgb(255 255 0)";//yellow
white = "rgb(255 255 255)";//white

//player colors
pink = "rgb(255 0 255)";//red
purple = "rgb(75 0 130)";//green
light_red = "rgba(189 90 107)";//light red
iron = "rgba(59 54 50 1)";//iron

//thses are the player inforamtion to control the graphics objetcs
playerName_p1="player 1"
blue_wedge_p1 = false; 
red_wedge_p1 = false; 
green_wedge_p1 = false; 
yellow_wedge_p1 = false; 
let playerXLoc_p1 = 4;
let playerYLoc_p1 = 4;
let PlayerColor_p1 = purple

playerName_p2="player 2"
blue_wedge_p2 = false; 
red_wedge_p2 = false; 
green_wedge_p2 = false; 
yellow_wedge_p2 = false; 
let playerXLoc_p2 = 4;
let playerYLoc_p2 = 4;
let PlayerColor_p2 = pink

playerName_p3="player 3"
blue_wedge_p3 = false; 
red_wedge_p3 = false; 
green_wedge_p3 = false; 
yellow_wedge_p3 = false; 
let playerXLoc_p3 = 4;
let playerYLoc_p3 = 4;
let PlayerColor_p3 = light_red

playerName_p4="player 4"
blue_wedge_p4 = false; 
red_wedge_p4 = false; 
green_wedge_p4 = false; 
yellow_wedge_p4 = false; 
let playerXLoc_p4 = 4;
let playerYLoc_p4 = 4;
let PlayerColor_p4 = iron


//this handles all of the connections
  $(document).ready(function () {
  

  const MAX_DATA_COUNT = 10;
  //connect to the socket server.
  //   var socket = io.connect("http://" + document.domain + ":" + location.port);
  var socket = io.connect();

    //receive player details from server
  socket.on("updatePlayerData", function (msg) {
    //console.log("Received playyer Data :: " + msg.row_num + " :: " + msg.username+ " :: " + msg.right+ " :: " + msg.wrong);

    if (msg.row_num == "none") {
       // console.log("can not not update if row is none");
        return;
    }
    let row = msg.row_num [msg.row_num .length - 1];
    row = Number(row) + Number(1)
   // console.log("# of row elms : "+ document.getElementById("playersTable").rows.length)
    //console.log("# of cel elms : " +document.getElementById("playersTable").rows[row].cells.length)
    document.getElementById("playersTable").rows[row].cells[0].innerHTML = msg.username;
    document.getElementById("playersTable").rows[row].cells[1].innerHTML = msg.sql_id;
    document.getElementById("playersTable").rows[row].cells[2].innerHTML = row;
    document.getElementById("playersTable").rows[row].cells[3].innerHTML = msg.wrong;
    document.getElementById("playersTable").rows[row].cells[4].innerHTML = msg.right;

    if (row == 1){
      playerName_p1 = msg.username;
      refresh_board();
    } else if (row == 2){
      playerName_p2 = msg.username;
      refresh_board();
    }else if (row == 3){
      playerName_p3 = msg.username;
      refresh_board();
    }else if (row == 4){
      playerName_p4 = msg.username;
      refresh_board();
    }

    //Received playyer Data :: none :: guest :: 0 :: 0
    //Received playyer Data :: player3 :: zxc :: 0 :: 0
  });
  
  socket.on("updatePlayerloc", function (msg) {
    //console.log("Received playyer Data :: " + msg.row_num + " :: " + msg.username+ " :: " + msg.right+ " :: " + msg.wrong);

    if (msg.player_num == "none") {
       // console.log("can not not update if row is none");
        return;
    }

    if (msg.player_num  == 1){
      playerXLoc_p1 = msg.X;
      playerYLoc_p1 = msg.Y;
      refresh_board();
    } else if (msg.player_num  == 2){
      layerXLoc_p2 = msg.X;
      playerYLoc_p2 = msg.Y;
      refresh_board();
    }else if (msg.player_num  == 3){
      layerXLoc_p3 = msg.X;
      playerYLoc_p3 = msg.Y;
      refresh_board();
    }else if (msg.player_num  == 4){
      layerXLoc_p4 = msg.X;
      playerYLoc_p4 = msg.Y;
      refresh_board();
    }

    //Received playyer Data :: none :: guest :: 0 :: 0
    //Received playyer Data :: player3 :: zxc :: 0 :: 0
  });

  socket.on("updatePlayerwedges", function (msg) {
    console.log("recived wedge data");
    if (msg.player_num == 1){
      blue_wedge_p1 = msg.blue; 
      red_wedge_p1 = msg.red; 
      green_wedge_p1 = msg.green; 
      yellow_wedge_p1 = msg.yellow; 
      refresh_board();
    } else if (msg.player_num == 2){
      blue_wedge_p1 = msg.blue; 
      red_wedge_p1 = msg.red; 
      green_wedge_p1 = msg.green; 
      yellow_wedge_p1 = msg.yellow; 
      refresh_board();
    }else if (msg.player_num == 3){
      blue_wedge_p3 = msg.blue; 
      red_wedge_p3 = msg.red; 
      green_wedge_p3 = msg.green; 
      yellow_wedge_p4 = msg.yellow; 
      refresh_board();
    }else if (msg.player_num == 4){
      blue_wedge_p4 = msg.blue; 
      red_wedge_p4 = msg.red; 
      green_wedge_p4 = msg.green; 
      yellow_wedge_p4 = msg.yellow; 
      refresh_board();
    }
   
  });

  //recive a new question from the server
  socket.on("newQuestion", function (msg) {
   // console.log("Received new question :: " + msg.question + " :: " + msg.answer1+ " :: " + msg.answer2+ " :: " + msg.answer3);
    
    document.getElementById("quest").innerHTML = msg.question;
    document.getElementById("answ1").value = msg.answer1;
    document.getElementById("answ2").value = msg.answer2;
    document.getElementById("answ3").value = msg.answer3;

  });
});


refresh_board();


function refresh_board(){
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);

  drawBoard();
  draw_score_text(1);
  draw_score_text(2);
  draw_score_text(3);
  draw_score_text(4);
  drawPlayers(playerXLoc_p1, playerYLoc_p1, PlayerColor_p1);
  drawPlayers(playerXLoc_p2, playerYLoc_p2, PlayerColor_p2);
  drawPlayers(playerXLoc_p3, playerYLoc_p3, PlayerColor_p3);
  drawPlayers(playerXLoc_p4, playerYLoc_p4, PlayerColor_p4);
}

function drawBoard() {
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");

  roll_text="roll again"
  center_text="center"
  hq_text="HQ"


  let x = 0
  let y = 0

  midx = 4* width
  lastx = 8* width
  //row 1
  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text,x+ (width/8),y +(height/2))
  x+=width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x+=width  

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text,x+ (width/4),y +(height/2))
  x+=width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x+=width  

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text,x+ (width/8),y +(height/2))
  x+=width
  

  //row 2
  y+=height
  x =0
  context.fillStyle = red;
  context.fillRect(x, y, width, height);

  context.fillStyle = yellow;
  context.fillRect(midx, y, width, height);

  context.fillStyle = red;
  context.fillRect(lastx, y, width, height);

  //row 3
  y+=height
  context.fillStyle = green;
  context.fillRect(x, y, width, height);

  context.fillStyle = blue;
  context.fillRect(midx, y, width, height);

  context.fillStyle = green;
  context.fillRect(lastx, y, width, height);

  //row 4
  y+=height

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);

  context.fillStyle = green;
  context.fillRect(midx, y, width, height);

  context.fillStyle = blue;
  context.fillRect(lastx, y, width, height);

  //row 5
  y+=height
  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
    context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text,x+ (width/4),y +(height/2))
  x+=width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x+=width  

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(center_text,x+ (width/8),y +(height/2))

  x+=width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x+=width  

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
    context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text,x+ (width/4),y +(height/2))
  x+=width

   //row 6
  y+=height
  x =0
  context.fillStyle = red;
  context.fillRect(x, y, width, height);

  context.fillStyle = yellow;
  context.fillRect(midx, y, width, height);

  context.fillStyle = red;
  context.fillRect(lastx, y, width, height);

  //row 7
  y+=height
  context.fillStyle = green;
  context.fillRect(x, y, width, height);

  context.fillStyle = blue;
  context.fillRect(midx, y, width, height);

  context.fillStyle = green;
  context.fillRect(lastx, y, width, height);

  //row 8
  y+=height

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);

  context.fillStyle = green;
  context.fillRect(midx, y, width, height);

  context.fillStyle = blue;
  context.fillRect(lastx, y, width, height);

  //row 9
  y+=height
  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text,x+ (width/8),y +(height/2))

  x+=width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x+=width  

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
    context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text,x+ (width/4),y +(height/2))
  x+=width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x+=width  

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x+=width

  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text,x+ (width/8),y +(height/2))
  drawPlayers();
}

function movePlayer(username, direction){
  // 0 =                north
  // 1 =                west
  // 2 =                east
  // 3 =                south

  console.log("moving "+ username)

  xloc = -1
  yloc = -1

  if (username  == 1) {
    if (direction == 0 ){
      console.log("north");
      if (playerYLoc_p1 <= 0){
        playerYLoc_p1 = 0;
      }else{
        playerYLoc_p1 -=1;
      }
    }else if (direction == 1 ){
      console.log("west");
      if (playerXLoc_p1 <= 0){
        playerXLoc_p1 = 0;
      }else{
        playerXLoc_p1 -=1;
      }
    }else if (direction == 2 ){
      console.log("east");
      if (playerXLoc_p1 > 7){
        playerXLoc_p1 = 8;
      }else{
        playerXLoc_p1+=1;
      }
    }else if (direction == 3 ){
      console.log("south");
      if (playerYLoc_p1 > 7){
        playerYLoc_p1 = 8;
      }else{
        playerYLoc_p1+=1;
      }
    }
    xloc = playerXLoc_p1
    yloc = playerYLoc_p1
  }else if (username == 2){
    if (direction == 0 ){
      console.log("north");
      if (playerYLoc_p2 <= 0){
        playerYLoc_p2 = 0;
      }else{
        playerYLoc_p2 -=1;
      }
    }else if (direction == 1 ){
      console.log("west");
      if (playerXLoc_p2 <= 0){
        playerXLoc_p2 = 0;
      }else{
        playerXLoc_p2 -=1;
      }
    }else if (direction == 2 ){
      console.log("east");
      if (playerXLoc_p2 > 7){
        playerXLoc_p2 = 8;
      }else{
        playerXLoc_p2+=1;
      }
    }else if (direction == 3 ){
      console.log("south");
      if (playerYLoc_p2 > 7){
        playerYLoc_p2 = 8;
      }else{
        playerYLoc_p2+=1;
      }
    }
    xloc = playerXLoc_p2
    yloc = playerYLoc_p2

  }else if (username == 3){
    if (direction == 0 ){
      console.log("north");
      if (playerYLoc_p3 <= 0){
        playerYLoc_p3 = 0;
      }else{
        playerYLoc_p3 -=1;
      }
    }else if (direction == 1 ){
      console.log("west");
      if (playerXLoc_p3 <= 0){
        playerXLoc_p3 = 0;
      }else{
        playerXLoc_p3 -=1;
      }
    }else if (direction == 2 ){
      console.log("east");
      if (playerXLoc_p3 > 7){
        playerXLoc_p3 = 8;
      }else{
        playerXLoc_p3+=1;
      }
    }else if (direction == 3 ){
      console.log("south");
      if (playerYLoc_p3 > 7){
        playerYLoc_p3 = 8;
      }else{
        playerYLoc_p3+=1;
      }
    }
    xloc = playerXLoc_p3
    yloc = playerYLoc_p3

  }else if (username ==4){
    if (direction == 0 ){
      console.log("north");
      if (playerYLoc_p4 <= 0){
        playerYLoc_p4 = 0;
      }else{
        playerYLoc_p4 -=1;
      }
    }else if (direction == 1 ){
      console.log("west");
      if (playerXLoc_p4 <= 0){
        playerXLoc_p4 = 0;
      }else{
        playerXLoc_p4 -=1;
      }
    }else if (direction == 2 ){
      console.log("east");
      if (playerXLoc_p4 > 7){
        playerXLoc_p4 = 8;
      }else{
        playerXLoc_p4+=1;
      }
    }else if (direction == 3 ){
      console.log("south");
      if (playerYLoc_p4 > 7){
        playerYLoc_p4 = 8;
      }else{
        playerYLoc_p4+=1;
      }
    }
    xloc = playerXLoc_p4
    yloc = playerYLoc_p4

  }

  console.log("x cord = " + xloc);
  console.log("y cord = " + yloc);

  refresh_board();

  output = xloc + "," + yloc
  return output
}

function drawPlayers(playerX, playerY,PlayerColor){
  const canvas = document.querySelector("#gl-canvas");
  // Initialize the GL context
  const context = canvas.getContext("2d");

  context.beginPath();
  const endAngle = Math.PI + (Math.PI * 3) / 2

  x = (playerX * width) + 25  ; // x coordinate
  y = (playerY *height) + 25 ; // y coordinate
  const radius = 10; // Arc radius
  const startAngle = 0; // Starting point on circle
  const counterclockwise =0
  context.arc(x, y, radius, startAngle, endAngle, counterclockwise);
  context.fillStyle = PlayerColor;
  context.fill();
  context.stroke();
}

function draw_score_text(player_num){

  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");

  height_score = height / 2
  width_score = width / 2

  p1x = (2 * width); // x coordinate
  p1y = (2 * height); // y coordinate
  let name = "unknown"
  if (player_num == 1){
    name = playerName_p1;
    blue_wedge = blue_wedge_p1;
    yellow_wedge = yellow_wedge_p1;
    red_wedge = red_wedge_p1;
    green_wedge = green_wedge_p1;
    context.fillStyle = PlayerColor_p1;
  } else if (player_num == 2){
    p1x = (6 * width); // x coordinate
    p1y = (2 * height); // y coordinate
    name = playerName_p2;
    blue_wedge = blue_wedge_p2;
    yellow_wedge = yellow_wedge_p2;
    red_wedge = red_wedge_p2;
    green_wedge = green_wedge_p2;
    context.fillStyle = PlayerColor_p2;
  }else if (player_num == 3){
    p1x = (2 * width); // x coordinate
    p1y = (6 * height); // y coordinate
    name = playerName_p3;
    blue_wedge = blue_wedge_p3;
    yellow_wedge = yellow_wedge_p3;
    red_wedge = red_wedge_p3;
    green_wedge = green_wedge_p3;
    context.fillStyle = PlayerColor_p3;
  }else if (player_num == 4){
    p1x = (6 * width); // x coordinate
    p1y = (6 * height); // y coordinate
    name = playerName_p4;
    blue_wedge = blue_wedge_p4;
    yellow_wedge = yellow_wedge_p4;
    red_wedge = red_wedge_p4;
    green_wedge = green_wedge_p4;
    context.fillStyle = PlayerColor_p4;
  }

  context.fillText(name,p1x,p1y -height_score)
  

  if (blue_wedge){
      context.fillStyle = blue;
      context.fillRect(p1x, p1y, width_score, height_score);
  }
  p1x += width_score;
  if (red_wedge) {
    context.fillStyle = red;
    context.fillRect(p1x, p1y, width_score, height_score);
  }
  p1y+=height_score;
  if (green_wedge){
    context.fillStyle = green;
    context.fillRect(p1x, p1y, width_score, height_score);
  }
  p1x -= width_score;

  if (yellow_wedge){
    context.fillStyle = yellow;
    context.fillRect(p1x, p1y, width_score, height_score);
  }

}

function calculateSquareIDFromCords(x,y){
  let output = ""

  console.log("y cord = " + playerYLoc_p1);
  return output
}
