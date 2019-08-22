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

V2plus hor_ptr = new V2plus(0);
V2plus min_ptr = new V2plus(0);
V2plus sec_ptr = new V2plus(0);
Vector2 screen = null;

float SPEED = 1;
float FPS = 1;

void setup(){

  screen = new Vector2(600,600);
  frameRate(FPS);
  size(600,600);
}

void circulo( float x, float y, float diam){

  stroke(0,0,0);    // Corda linha da figura...
  strokeWeight(1);  // Espessura da linha
  circle(x,y,diam);
}

void circulo( Vector2 pos, float diam){
  circulo(pos.x,pos.y,diam);
}

void pointer( Vector2 pos, float weight){  // Desenha um ponteiro do centro até 'pos'

  stroke(0,0,0);         // Corda linha da figura...
  strokeWeight(weight);  // Espessura da linha
  line(screen.x/2,screen.y/2,pos.x,pos.y);
}

void draw(){

  // Erase the last
  background(220,220,220);

  float pt_size = screen.smaller()*0.01;
  float raio = screen.smaller()*0.9;

  float cx = screen.x/2;
  float cy = screen.y/2;

  // Limites do relógio...
  circulo(cx,cy,raio);

  // Desenha o ponto do meio
  circulo(cx,cy,pt_size);

  // Ponto auxiliar pra desenhar horas: começa em 0h
  Vector2 hora = new Vector2();
  float k = (raio/2)*0.9;

  for( int i = 0; i != 12; ++i){

    hora.x = cx + sin(i*PI/6) * k;
    hora.y = cy - cos(i*PI/6) * k;

    circulo(hora,pt_size);
  }

    // Desenha todos os ponteiros e incrementa seus ângulos

    hor_ptr.x = cx + sin(hor_ptr.angle) * (k*0.5);
    hor_ptr.y = cy - cos(hor_ptr.angle) * (k*0.5);
    hor_ptr.angle += (SPEED*PI)/(108000*FPS);
    pointer(hor_ptr,5);

    min_ptr.x = cx + sin(min_ptr.angle) * (k*0.7);
    min_ptr.y = cy - cos(min_ptr.angle) * (k*0.7);
    min_ptr.angle += (SPEED*PI)/(1800*FPS);
    pointer(min_ptr,3);

    sec_ptr.x = cx + sin(sec_ptr.angle) * (k*0.9);
    sec_ptr.y = cy - cos(sec_ptr.angle) * (k*0.9);
    sec_ptr.angle += (SPEED*PI)/(30*FPS);
    pointer(sec_ptr,1);
}
