//set all the vars for the players 

//the size of each board square
//needed to caluculate possition to move the player
const width = 50
const height = 50

//the base colors of the board
red = "rgb(200 0 0)";//red
red = "rgb(255 109 116)";//red
green = "rgb(9 200 0)";//green
green = "rgb(79 221 195)";//green
blue = "rgb(0 0 200)";//blue
blue = "rgb(71 96 136)";//blue
yellow = "rgb(255 255 0)";//yellow
yellow = "rgb(255 197 98)";//yellow
white = "rgb(255 255 255)";//white

questColor = "rgb(211 211 211)"
questButtonColor = "rgb(222 179 25)"
questBackgroundColor = "rgb(0 190 156)"

victoryBannerColor = "rgb(0 190 156)"

//player colors
pink = "rgb(255 0 255)";//red
purple = "rgb(75 0 130)";//green
light_red = "rgb(189 90 107)";//light red
iron = "rgb(59 54 50 1)";//iron

//misc numbers needed for determing if a button was clicked on
let startButtonX = -1;
let startButtonY = -1;
let startButtonWidth = -1;
let startButtonHeight = -1;

let dirButton1X = -1;
let dirButton1Y = -1;
let dirButton1Width = -1;
let dirButton1Height = -1;

let dirButton2X = -1;
let dirButton2Y = -1;
let dirButton2Width = -1;
let dirButton2Height = -1;

let dirButton3X = -1;
let dirButton3Y = -1;
let dirButton3Width = -1;
let dirButton3Height = -1;

quest = "example question";
answer1 = "adsadsdsa";
answer2 = "jtyjytjkty";
answer3 = "44535ewerw";

//thses are the player inforamtion to control the graphics objetcs
playerName_p1 = "player 1"
blue_wedge_p1 = false;
red_wedge_p1 = false;
green_wedge_p1 = false;
yellow_wedge_p1 = false;
let playerXLoc_p1 = 4;
let playerYLoc_p1 = 4;
let PlayerColor_p1 = purple
let Player1_connected = false


playerName_p2 = "player 2"
blue_wedge_p2 = false;
red_wedge_p2 = false;
green_wedge_p2 = false;
yellow_wedge_p2 = false;
let playerXLoc_p2 = 4;
let playerYLoc_p2 = 4;
let PlayerColor_p2 = pink
let Player2_connected = false

playerName_p3 = "player 3"
blue_wedge_p3 = false;
red_wedge_p3 = false;
green_wedge_p3 = false;
yellow_wedge_p3 = false;
let playerXLoc_p3 = 4;
let playerYLoc_p3 = 4;
let PlayerColor_p3 = light_red
let Player3_connected = false

playerName_p4 = "player 4"
blue_wedge_p4 = false;
red_wedge_p4 = false;
green_wedge_p4 = false;
yellow_wedge_p4 = false;
let playerXLoc_p4 = 4;
let playerYLoc_p4 = 4;
let PlayerColor_p4 = iron
let Player4_connected = false

//determines what to display
//0 lobby
//1 gameboard
//2 question
//3 choice
//4 roll button
//5 vicory state
let gameState = 2;
let winner = "this should not be here"
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
    let row = msg.row_num[msg.row_num.length - 1];
    row = Number(row) + Number(1)
    // console.log("# of row elms : "+ document.getElementById("playersTable").rows.length)
    //console.log("# of cel elms : " +document.getElementById("playersTable").rows[row].cells.length)
    document.getElementById("playersTable").rows[row].cells[0].innerHTML = msg.username;
    document.getElementById("playersTable").rows[row].cells[1].innerHTML = msg.sql_id;
    document.getElementById("playersTable").rows[row].cells[2].innerHTML = row;
    document.getElementById("playersTable").rows[row].cells[3].innerHTML = msg.wrong;
    document.getElementById("playersTable").rows[row].cells[4].innerHTML = msg.right;

    if (row == 1) {
      playerName_p1 = msg.username;
      Player1_connected = true;
      display_game();
    } else if (row == 2) {
      playerName_p2 = msg.username;
      Player2_connected = true;
      display_game();
    } else if (row == 3) {
      playerName_p3 = msg.username;
      Player3_connected = true;
      display_game();
    } else if (row == 4) {
      playerName_p4 = msg.username;
      Player4_connected = true;
      display_game();
    }

    //Received playyer Data :: none :: guest :: 0 :: 0
    //Received playyer Data :: player3 :: zxc :: 0 :: 0
  });

  socket.on("updatePlayerloc", function (msg) {
    console.log("Received playyer Data :: " + msg.player + " :: " + msg.X + " :: " + msg.Y);



    if (String(msg.player) == String(playerName_p1)) {
      console.log("p1 updated")
      playerXLoc_p1 = msg.X;
      playerYLoc_p1 = msg.Y;
      display_game();
    } else if (String(msg.player) == String(playerName_p2)) {
      console.log("p2 updated")
      playerXLoc_p2 = msg.X;
      playerYLoc_p2 = msg.Y;
      display_game();
    } else if (String(msg.player) == String(playerName_p3)) {
      console.log("p3 updated")
      playerXLoc_p3 = msg.X;
      playerYLoc_p3 = msg.Y;
      display_game();
    } else {//if (String(msg.player)  == String(playerName_p4)){
      console.log("p4 updated")
      playerXLoc_p4 = msg.X;
      playerYLoc_p4 = msg.Y;
      display_game();
    }

    //Received playyer Data :: none :: guest :: 0 :: 0
    //Received playyer Data :: player3 :: zxc :: 0 :: 0
  });

  socket.on("updatePlayerwedges", function (msg) {
    console.log("recived wedge data");
    if (msg.player_num == 1) {
      blue_wedge_p1 = msg.blue;
      red_wedge_p1 = msg.red;
      green_wedge_p1 = msg.green;
      yellow_wedge_p1 = msg.yellow;

      if (blue_wedge_p1 && red_wedge_p1 && green_wedge_p1 && yellow_wedge_p1) {
        gameState = 5;
        winner = playerName_p1;
      }
      display_game();
    } else if (msg.player_num == 2) {
      blue_wedge_p2 = msg.blue;
      red_wedge_p2 = msg.red;
      green_wedge_p2 = msg.green;
      yellow_wedge_p2 = msg.yellow;
      if (blue_wedge_p2 && red_wedge_p2 && green_wedge_p2 && yellow_wedge_p2) {
        gameState = 5;
        winner = playerName_p1;
      }

      if (blue_wedge_p2 && red_wedge_p2 && green_wedge_p2 && yellow_wedge_p2) {
        gameState = 5;
        winner = playerName_p2;
      }
      display_game();
    } else if (msg.player_num == 3) {
      blue_wedge_p3 = msg.blue;
      red_wedge_p3 = msg.red;
      green_wedge_p3 = msg.green;
      yellow_wedge_p3 = msg.yellow;

      if (blue_wedge_p3 && red_wedge_p3 && green_wedge_p3 && yellow_wedge_p3) {
        gameState = 5;
        winner = playerName_p3;
      }
      display_game();
    } else if (msg.player_num == 4) {
      blue_wedge_p4 = msg.blue;
      red_wedge_p4 = msg.red;
      green_wedge_p4 = msg.green;
      yellow_wedge_p4 = msg.yellow;

      if (blue_wedge_p4 && red_wedge_p4 && green_wedge_p4 && yellow_wedge_p4) {
        gameState = 5;
        winner = playerName_p4;
      }
      display_game();
    }

  });

  function getCursorPosition(canvas, event) {
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left
    const y = event.clientY - rect.top
    console.log("x: " + x + " y: " + y)

    //all the possible button clicks for the loby screen
    if (gameState == 0) {
      //check to see if the start button was clicked 
      if (startButtonX != -1 &&
        startButtonY != -1 &&
        startButtonWidth != -1 &&
        startButtonHeight != -1) {

        if (was_space_clicked(x, y, startButtonX, startButtonY, startButtonWidth, startButtonHeight)) {
          console.log("start button was clicked")

        }
      }
    }


  }

  function was_space_clicked(x, y, startX, startY, width, height) {
    if ((x >= startX && x <= (startX + width)) &&
      (y >= startY && y <= (startY + height))) {
      return true;
    }
    return false;
  }

  const canvas_envents = document.querySelector('#gl-canvas')
  canvas_envents.addEventListener('mousedown', function (e) {
    getCursorPosition(canvas_envents, e)
  })

  //recive a new question from the server
  socket.on("newQuestion", function (msg) {
    // console.log("Received new question :: " + msg.question + " :: " + msg.answer1+ " :: " + msg.answer2+ " :: " + msg.answer3);

    quest = msg.question;
    answer1 = msg.answer1;
    answer2 = msg.answer2;
    answer3 = msg.answer3;
    document.getElementById("quest").innerHTML = msg.question;
    document.getElementById("answ1").value = msg.answer1;
    document.getElementById("answ2").value = msg.answer2;
    document.getElementById("answ3").value = msg.answer3;

  });
});

display_game();



function display_game() {


  //0 lobby
  //1 gameboard
  //2 question
  //3 choice
  //4 roll button
  //5 vicory state
  if (gameState == 0) {
    draw_lobby_waiting();
  } else {
    refresh_board();
    if (gameState == 2) {
      draw_question_card();
    } else if (gameState == 3) {

    } else if (gameState == 4) {
      drawRollButton();
    } else if (gameState == 5) {
      draw_victory_banner();
    }

  }
}

function refresh_board() {
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);

  drawBoard();
  draw_score_text(1);
  draw_score_text(2);
  draw_score_text(3);
  draw_score_text(4);
  console.log("p1");
  drawPlayers(playerXLoc_p1, playerYLoc_p1, PlayerColor_p1);
  console.log("p2");
  drawPlayers(playerXLoc_p2, playerYLoc_p2, PlayerColor_p2);
  console.log("p3");
  drawPlayers(playerXLoc_p3, playerYLoc_p3, PlayerColor_p3);
  console.log("p4");
  drawPlayers(playerXLoc_p4, playerYLoc_p4, PlayerColor_p4);
  console.log("end");

}

function drawBoard() {
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");

  roll_text = "roll again"
  center_text = "center"
  hq_text = "HQ"


  let x = 0
  let y = 0

  midx = 4 * width
  lastx = 8 * width
  //row 1
  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text, x + (width / 8), y + (height / 2))
  x += width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text, x + (width / 4), y + (height / 2))
  x += width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text, x + (width / 8), y + (height / 2))
  x += width


  //row 2
  y += height
  x = 0
  context.fillStyle = red;
  context.fillRect(x, y, width, height);

  context.fillStyle = yellow;
  context.fillRect(midx, y, width, height);

  context.fillStyle = red;
  context.fillRect(lastx, y, width, height);

  //row 3
  y += height
  context.fillStyle = green;
  context.fillRect(x, y, width, height);

  context.fillStyle = blue;
  context.fillRect(midx, y, width, height);

  context.fillStyle = green;
  context.fillRect(lastx, y, width, height);

  //row 4
  y += height

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);

  context.fillStyle = green;
  context.fillRect(midx, y, width, height);

  context.fillStyle = blue;
  context.fillRect(lastx, y, width, height);

  //row 5
  y += height
  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text, x + (width / 4), y + (height / 2))
  x += width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(center_text, x + (width / 8), y + (height / 2))

  x += width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text, x + (width / 4), y + (height / 2))
  x += width

  //row 6
  y += height
  x = 0
  context.fillStyle = red;
  context.fillRect(x, y, width, height);

  context.fillStyle = yellow;
  context.fillRect(midx, y, width, height);

  context.fillStyle = red;
  context.fillRect(lastx, y, width, height);

  //row 7
  y += height
  context.fillStyle = green;
  context.fillRect(x, y, width, height);

  context.fillStyle = blue;
  context.fillRect(midx, y, width, height);

  context.fillStyle = green;
  context.fillRect(lastx, y, width, height);

  //row 8
  y += height

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);

  context.fillStyle = green;
  context.fillRect(midx, y, width, height);

  context.fillStyle = blue;
  context.fillRect(lastx, y, width, height);

  //row 9
  y += height
  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text, x + (width / 8), y + (height / 2))

  x += width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = blue;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(hq_text, x + (width / 4), y + (height / 2))
  x += width

  context.fillStyle = yellow;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = red;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = green;
  context.fillRect(x, y, width, height);
  x += width

  context.fillStyle = white;
  context.fillRect(x, y, width, height);
  context.fillStyle = "rgb(0 0 0 )";
  context.fillText(roll_text, x + (width / 8), y + (height / 2))
}

function movePlayer(username, direction) {
  // 0 =                north
  // 1 =                west
  // 2 =                east
  // 3 =                south

  console.log("moving " + username)

  xloc = -1
  yloc = -1

  if (username == 1) {
    if (direction == 0) {
      console.log("north");
      if (playerYLoc_p1 <= 0) {
        playerYLoc_p1 = 0;
      } else {
        playerYLoc_p1 -= 1;
      }
    } else if (direction == 1) {
      console.log("west");
      if (playerXLoc_p1 <= 0) {
        playerXLoc_p1 = 0;
      } else {
        playerXLoc_p1 -= 1;
      }
    } else if (direction == 2) {
      console.log("east");
      if (playerXLoc_p1 > 7) {
        playerXLoc_p1 = 8;
      } else {
        playerXLoc_p1 += 1;
      }
    } else if (direction == 3) {
      console.log("south");
      if (playerYLoc_p1 > 7) {
        playerYLoc_p1 = 8;
      } else {
        playerYLoc_p1 += 1;
      }
    }
    xloc = playerXLoc_p1
    yloc = playerYLoc_p1
  } else if (username == 2) {
    if (direction == 0) {
      console.log("north");
      if (playerYLoc_p2 <= 0) {
        playerYLoc_p2 = 0;
      } else {
        playerYLoc_p2 -= 1;
      }
    } else if (direction == 1) {
      console.log("west");
      if (playerXLoc_p2 <= 0) {
        playerXLoc_p2 = 0;
      } else {
        playerXLoc_p2 -= 1;
      }
    } else if (direction == 2) {
      console.log("east");
      if (playerXLoc_p2 > 7) {
        playerXLoc_p2 = 8;
      } else {
        playerXLoc_p2 += 1;
      }
    } else if (direction == 3) {
      console.log("south");
      if (playerYLoc_p2 > 7) {
        playerYLoc_p2 = 8;
      } else {
        playerYLoc_p2 += 1;
      }
    }
    xloc = playerXLoc_p2
    yloc = playerYLoc_p2

  } else if (username == 3) {
    if (direction == 0) {
      console.log("north");
      if (playerYLoc_p3 <= 0) {
        playerYLoc_p3 = 0;
      } else {
        playerYLoc_p3 -= 1;
      }
    } else if (direction == 1) {
      console.log("west");
      if (playerXLoc_p3 <= 0) {
        playerXLoc_p3 = 0;
      } else {
        playerXLoc_p3 -= 1;
      }
    } else if (direction == 2) {
      console.log("east");
      if (playerXLoc_p3 > 7) {
        playerXLoc_p3 = 8;
      } else {
        playerXLoc_p3 += 1;
      }
    } else if (direction == 3) {
      console.log("south");
      if (playerYLoc_p3 > 7) {
        playerYLoc_p3 = 8;
      } else {
        playerYLoc_p3 += 1;
      }
    }
    xloc = playerXLoc_p3
    yloc = playerYLoc_p3

  } else {//if (username ==4){
    if (direction == 0) {
      console.log("north");
      if (playerYLoc_p4 <= 0) {
        playerYLoc_p4 = 0;
      } else {
        playerYLoc_p4 -= 1;
      }
    } else if (direction == 1) {
      console.log("west");
      if (playerXLoc_p4 <= 0) {
        playerXLoc_p4 = 0;
      } else {
        playerXLoc_p4 -= 1;
      }
    } else if (direction == 2) {
      console.log("east");
      if (playerXLoc_p4 > 7) {
        playerXLoc_p4 = 8;
      } else {
        playerXLoc_p4 += 1;
      }
    } else if (direction == 3) {
      console.log("south");
      if (playerYLoc_p4 > 7) {
        playerYLoc_p4 = 8;
      } else {
        playerYLoc_p4 += 1;
      }
    }
    xloc = playerXLoc_p4
    yloc = playerYLoc_p4

  }

  console.log("x cord = " + xloc);
  console.log("y cord = " + yloc);

  display_game();

  output = xloc + "," + yloc
  return output
}

function drawPlayers(playerX, playerY, PlayerColor) {
  const canvas = document.querySelector("#gl-canvas");
  // Initialize the GL context
  const context = canvas.getContext("2d");

  console.log("player color : " + String(PlayerColor))

  context.beginPath();
  const endAngle = Math.PI + (Math.PI * 3) / 2

  x = (playerX * width) + 25; // x coordinate
  y = (playerY * height) + 25; // y coordinate
  const radius = 10; // Arc radius
  const startAngle = 0; // Starting point on circle
  const counterclockwise = 0
  context.arc(x, y, radius, startAngle, endAngle, counterclockwise);
  context.fillStyle = PlayerColor;
  context.fill();
  context.stroke();
}

function draw_score_text(player_num) {

  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");

  height_score = height / 2
  width_score = width / 2

  p1x = (2 * width); // x coordinate
  p1y = (2 * height); // y coordinate
  let name = "unknown"
  if (player_num == 1) {
    name = playerName_p1;
    blue_wedge = blue_wedge_p1;
    yellow_wedge = yellow_wedge_p1;
    red_wedge = red_wedge_p1;
    green_wedge = green_wedge_p1;
    context.fillStyle = PlayerColor_p1;
  } else if (player_num == 2) {
    p1x = (6 * width); // x coordinate
    p1y = (2 * height); // y coordinate
    name = playerName_p2;
    blue_wedge = blue_wedge_p2;
    yellow_wedge = yellow_wedge_p2;
    red_wedge = red_wedge_p2;
    green_wedge = green_wedge_p2;
    context.fillStyle = PlayerColor_p2;
  } else if (player_num == 3) {
    p1x = (2 * width); // x coordinate
    p1y = (6 * height); // y coordinate
    name = playerName_p3;
    blue_wedge = blue_wedge_p3;
    yellow_wedge = yellow_wedge_p3;
    red_wedge = red_wedge_p3;
    green_wedge = green_wedge_p3;
    context.fillStyle = PlayerColor_p3;
  } else if (player_num == 4) {
    p1x = (6 * width); // x coordinate
    p1y = (6 * height); // y coordinate
    name = playerName_p4;
    blue_wedge = blue_wedge_p4;
    yellow_wedge = yellow_wedge_p4;
    red_wedge = red_wedge_p4;
    green_wedge = green_wedge_p4;
    context.fillStyle = PlayerColor_p4;
  }

  context.fillText(name, p1x, p1y - height_score)


  if (blue_wedge) {
    context.fillStyle = blue;
    context.fillRect(p1x, p1y, width_score, height_score);
  }
  p1x += width_score;
  if (red_wedge) {
    context.fillStyle = red;
    context.fillRect(p1x, p1y, width_score, height_score);
  }
  p1y += height_score;
  if (green_wedge) {
    context.fillStyle = green;
    context.fillRect(p1x, p1y, width_score, height_score);
  }
  p1x -= width_score;

  if (yellow_wedge) {
    context.fillStyle = yellow;
    context.fillRect(p1x, p1y, width_score, height_score);
  }

}

function draw_lobby_waiting() {
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");
  context.fillStyle = "green";
  context.fillRect(0, 0, canvas.width, canvas.height);

  xText = 20;
  yText = 15;

  p1Text = "player 1 : " + playerName_p1;
  p2Text = "player 2 : " + playerName_p2;
  p3Text = "player 3 : " + playerName_p3;
  p4Text = "player 4 : " + playerName_p4;
  context.fillStyle = "rgb(255 255 255)";
  context.fillText(p1Text, xText, yText);

  yText += 15
  context.fillText(p2Text, xText, yText);

  yText += 15
  context.fillText(p3Text, xText, yText);

  yText += 15
  context.fillText(p4Text, xText, yText);

  //one is here for testing
  if (Player4_connected) {
    //if (Player1_connected && Player2_connected && Player3_connected && Player4_connected){
    yText += 15

    startButtonX = xText;
    startButtonY = yText;
    startButtonWidth = 80;
    startButtonHeight = 40;

    context.fillStyle = "rgb(255 0 0)";
    context.fillRect(xText, yText, startButtonWidth, startButtonHeight);
    yText += 15
    context.fillStyle = "rgb(0 0 0)";
    context.fillText("click to start", xText, yText);
  }
}

function draw_question_card() {
  resetDirButtons();

  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");

  //questButtonColor = "rgb(222 179 25)"
  //questBackgroundColor = "rgb(0 190 156)"

  //quest = "";
  //answer1 = "";
  //answer2 = "";
  //answer3 = "";

 

  //const width = 50
  //const height = 50
  
  boardSizeX = (width * 9);
  boardSizeY = (height *9);
  cardSizeX = boardSizeX / 2
  cardSizeY = (boardSizeY / 2) + (boardSizeY/6)
  backX = (boardSizeX/2)/2;
  backY = (boardSizeY/2)/2;

  buttonLength = (cardSizeX - (cardSizeX/8));
  buttonHeight = 50;
  buttonSpacing = 10;

  context.fillStyle = questBackgroundColor;
  context.fillRect(backX, backY, cardSizeX, cardSizeY);


  backX+= (cardSizeX/16)
  backY += (buttonSpacing);

  context.fillStyle = questColor;
  context.fillRect(backX, backY, buttonLength, buttonHeight);

  backY += (buttonHeight);
  backY += (buttonHeight + buttonSpacing);

  context.fillStyle = questButtonColor;
  context.fillRect(backX, backY, buttonLength, buttonHeight);

  backY += (buttonHeight + buttonSpacing);

  context.fillStyle = questButtonColor;
  context.fillRect(backX, backY, buttonLength, buttonHeight);
  backY += (buttonHeight + buttonSpacing);

  context.fillStyle = questButtonColor;
  context.fillRect(backX, backY, buttonLength, buttonHeight);

}

function calculateSquareIDFromCords(x, y) {
  let output = ""

  console.log("y cord = " + playerYLoc_p1);
  return output
}

function resetDirButtons() {
  dirButton1X = -1;
  dirButton1Y = -1;
  dirButton1Width = -1;
  dirButton1Height = -1;

  dirButton2X = -1;
  dirButton2Y = -1;
  dirButton2Width = -1;
  dirButton2Height = -1;

  dirButton3X = -1;
  dirButton3Y = -1;
  dirButton3Width = -1;
  dirButton3Height = -1;
}


function drawRollButton() {

}

function draw_victory_banner() {


}