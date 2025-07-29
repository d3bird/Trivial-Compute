



//the size of each board square
//needed to caluculate possition to move the player
const width = 50
const height = 50

//the base colors of the board
  red = "rgb(200 0 0)";//red
  green = "rgb(9 200 0)";//green
  blue = "rgb(0 0 200)";//blue
  yellow = "rgb(255 255 0)";//yellow
  black = "rgb(255 255 255)";//black

//player colors
  pink = "rgb(255 0 255)";//red
  purple = "rgb(75 0 130)";//green
  light_red = "rgba(189 90 107)";//light red
  iron = "rgb(165 156 148)";//iron

//thses are the player inforamtion to control the graphics objetcs
playerName_p1="player 1"
blue_wedge_p1 = true; 
red_wedge_p1 = true; 
green_wedge_p1 = true; 
yellow_wedge_p1 = true; 
let playerXLoc_p1 = 0;
let playerYLoc_p1 = 0;
let PlayerColor_p1 = purple

playerName_p2="player 2"
blue_wedge_p2 = true; 
red_wedge_p2 = true; 
green_wedge_p2 = true; 
yellow_wedge_p2 = true; 
let playerXLoc_p2 = 0;
let playerYLoc_p2 = 0;
let PlayerColor_p2 = pink

playerName_p3="player 3"
blue_wedge_p3 = true; 
red_wedge_p3 = true; 
green_wedge_p3 = true; 
yellow_wedge_p3 = true; 
let playerXLoc_p3 = 0;
let playerYLoc_p3 = 0;
let PlayerColor_p3 = light_red

playerName_p4="player 4"
blue_wedge_p4 = true; 
red_wedge_p4 = true; 
green_wedge_p4 = true; 
yellow_wedge_p4 = true; 
let playerXLoc_p4 = 0;
let playerYLoc_p4 = 0;
let PlayerColor_p4 = iron


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
  drawPlayers();
}

function drawBoard() {
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");


  let x = 0
  let y = 0

  midx = 4* width
  lastx = 8* width
  //row 1
  context.fillStyle = black;
  context.fillRect(x, y, width, height);
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

  context.fillStyle = black;
  context.fillRect(x, y, width, height);
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

  context.fillStyle = black;
  context.fillRect(x, y, width, height);
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
  context.fillStyle = black;
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
  x+=width

  context.fillStyle = black;
  context.fillRect(x, y, width, height);

  drawPlayers();
}

function movePlayer(direction){
  // 0 =                north
  // 1 =                west
  // 2 =                east
  // 3 =                south
  console.log("moving player");
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
  
  console.log("x cord = " + playerXLoc_p1);
  console.log("y cord = " + playerYLoc_p1);

  
  refresh_board();
}

function drawPlayers(){
  const canvas = document.querySelector("#gl-canvas");
  // Initialize the GL context
  const context = canvas.getContext("2d");



  context.beginPath();
  const endAngle = Math.PI + (Math.PI * 3) / 2

  x = (playerXLoc_p1 * width) + 25  ; // x coordinate
  y = (playerYLoc_p1 *height) + 25 ; // y coordinate
  const radius = 10; // Arc radius
  const startAngle = 0; // Starting point on circle
  const counterclockwise =0
  context.arc(x, y, radius, startAngle, endAngle, counterclockwise);
  context.fillStyle = PlayerColor_p1;
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
  if (red_wedge_p1) ;{
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