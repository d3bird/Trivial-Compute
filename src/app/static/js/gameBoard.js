
//thses are the players cords for what square they are on 
let playerXLoc = 0;
let playerYLoc = 0;
let PlayerColor = "rgb(75 0 130)"

//the size of each board square
//needed to caluculate possition to move the player
const width = 50
const height = 50

refresh_board();
function refresh_board(){
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);

  drawBoard();
  drawPlayers();
}

function drawBoard() {
  const canvas = document.querySelector("#gl-canvas");
  const context = canvas.getContext("2d");

  red = "rgb(200 0 0)";//red
  green = "rgb(9 200 0)";//green
  blue = "rgb(0 0 200)";//blue
  yellow = "rgb(255 255 0)";//yellow
  black = "rgb(255 255 255)";//black


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
    if (playerYLoc <= 0){
      playerYLoc = 0;
    }else{
      playerYLoc -=1;
    }
  }else if (direction == 1 ){
    console.log("west");
    if (playerXLoc <= 0){
      playerXLoc = 0;
    }else{
      playerXLoc -=1;
    }
  }else if (direction == 2 ){
    console.log("east");
    if (playerXLoc > 7){
      playerXLoc = 8;
    }else{
      playerXLoc+=1;
    }
  }else if (direction == 3 ){
    console.log("south");
    if (playerYLoc > 7){
      playerYLoc = 8;
    }else{
      playerYLoc+=1;
    }
  }
  
  console.log("x cord = " + playerXLoc);
  console.log("y cord = " + playerYLoc);

  
  refresh_board();
}

function drawPlayers(){
  const canvas = document.querySelector("#gl-canvas");
  // Initialize the GL context
  const context = canvas.getContext("2d");

  pink = "rgb(255 0 255)";//red
  purple = "rgb(75 0 130)";//green
  light_red = "rgba(189 90 107)";//light red
  iron = "rgb(165 156 148)";//iron

  context.beginPath();
  const endAngle = Math.PI + (Math.PI * 3) / 2

  x = (playerXLoc * width) + 25  ; // x coordinate
  y = (playerYLoc *height) + 25 ; // y coordinate
  const radius = 10; // Arc radius
  const startAngle = 0; // Starting point on circle
  const counterclockwise =0
  context.arc(x, y, radius, startAngle, endAngle, counterclockwise);
  context.fillStyle = PlayerColor;
  context.fill();
  context.stroke();
}


function calculateSquareIDFromCords(x,y){

  return 0
}