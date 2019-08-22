class Vector2{

  float x, y;

  Vector2( float x, float y){
    this.x = x;
    this.y = y;
  }

  Vector2(){
    this.x = 0;
    this.y = 0;
  }

  float smaller(){
    return screen.x > screen.y ? screen.y : screen.x;
  }
}

class V2plus extends Vector2{

  V2plus( float angle){

    this.angle = angle;
  }

  float angle;
}

V2plus terra = new V2plus(0);
V2plus lua = new V2plus(0);
V2plus sol = new V2plus(0);
Vector2 screen = null;

float SPEED = 1000000;
float FPS = 60;

void setup(){

  screen = new Vector2(600,600);
  frameRate(FPS);
  size(600,600);
}

void draw_terra(){  // Desenha a terra

  stroke(0,0,0);    // Corda linha da figura...
  strokeWeight(1);  // Espessura da linha
  fill(0,0,255);
  circle(terra.x,terra.y,screen.smaller()*0.06);
}

void draw_lua(){  // Desenha a lua

  stroke(0,0,0);    // Corda linha da figura...
  strokeWeight(1);  // Espessura da linha
  fill(255,255,255);
  circle(lua.x,lua.y,screen.smaller()*0.01);
}

void draw_sol(){  // Desenha o sol

  stroke(0,0,0);    // Corda linha da figura...
  strokeWeight(1);  // Espessura da linha
  fill(255,255,0);
  circle(sol.x,sol.y,screen.smaller()*0.3);
}

void draw(){

  // Erase the last
  background(0,0,0);

  // Dá a posição do sol e desenha
  sol.x = screen.x/2;
  sol.y = screen.y/2;
  draw_sol();

  // Distance
  float dist = (screen.smaller()/2)*0.6;

  // Dá a posição da terra e desenha
  terra.x = sol.x + sin(terra.angle) * dist;
  terra.y = sol.y - cos(terra.angle) * dist;
  terra.angle += (SPEED*PI)/(15778800*FPS);
  draw_terra();

  // Dá a posição da lua e desenha
  lua.x = terra.x + sin(lua.angle) * (dist/4);
  lua.y = terra.y - cos(lua.angle) * (dist/4);
  lua.angle += (SPEED*PI)/(1314900*FPS);
  draw_lua();

  // Evita overflow de ponto flutuante
  terra.angle -= terra.angle > SPEED*PI ? SPEED*PI : 0;
  lua.angle -= lua.angle > SPEED*PI ? SPEED*PI : 0;
}
