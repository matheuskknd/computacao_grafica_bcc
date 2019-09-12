void setup(){

	size(800,500);
}

void draw(){

	background(0,0,0,0);
	float ax = 10;
	float ay = 300;
	float bx = 790;
	float by = 300;
	int ordem = 4;
	fractal(ax,ay,bx,by,ordem);
}

void fractal( float ax, float ay, float bx, float by, int ordem){

	if(ordem == 0){

		stroke(255);
		line(ax,ay,bx,by);

	}else{

		float cx = ax + (bx-ax)/3.0;
		float cy = ay + (by-ay)/3.0;
		float dx = ax + 2.0*(bx-ax)/3.0;
		float dy = ay + 2.0*(by-ay)/3.0;
		float ex = ((dx-cx)*cos(-PI/3)-(dy-cy)*sin(-PI/3))+cx;
		float ey = ((dx-cx)*sin(-PI/3)+(dy-cy)*cos(-PI/3))+cy;
		fractal(ax,ay,cx,cy,ordem-1);
		fractal(cx,cy,ex,ey,ordem-1);
		fractal(ex,ey,dx,dy,ordem-1);
		fractal(dx,dy,bx,by,ordem-1);
	}
}
