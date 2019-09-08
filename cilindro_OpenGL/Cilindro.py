#!/usr/bin/env python
# coding: utf-8

from math import pi, sin, cos
from random import uniform
from sys import argv

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

N = int(argv[1]) if len(argv) == 2 else 3
H = 3
R = 2

assert N > 2, "N inválido...\n"

def rand_color():
	return (uniform(0.000001,1),uniform(0.000001,1),uniform(0.000001,1))

#####################################
######## Constroi o polígono ########
#####################################

###################
# Constroi o teto #
###################

# List<Vector3>
tetov = [(R*sin(2*pi*(float(i)/N)),H,R*cos(2*pi*(float(i)/N))) for i in range(N)]

# List<Tuple<Vector3,Vector3>>
#tetol =  [(tetov[i],tetov[i+1]) for i in range(N-1)]
#tetol += [(tetov[-1],tetov[0])]

# Tuple<List<Vector3>,Color>
tetof = (tetov,rand_color())

###################
# Constroi a base #
###################

# List<Vector3>
basev = [(i[0],0,i[2]) for i in tetov]

# List<Tuple<Vector3,Vector3>>
#basel =  [(basev[i],basev[i+1]) for i in range(N-1)]
#basel += [(basev[-1],basev[0])]

# Tuple<List<Vector3>,Color>
basef = (basev,rand_color())

###################
# Define os lados #
###################

# List<Vector3>
#ladov = basev + tetov

# List<Tuple<Vector3,Vector3>>
#ladol =  [(basev[i],tetov[i]) for i in range(N)]
#ladol += basel + tetol

# List<Tuple<Tuple<Vector3,Vector3,Vector3,Vector3>,Color>>
ladof =  [((tetov[i],basev[i],basev[i+1],tetov[i+1]),rand_color()) for i in range(N-1)]
ladof += [((tetov[-1],basev[-1],basev[0],tetov[0]),rand_color())]

#####################################
## Começa o desenho desse polígono ##
#####################################

frame = 0

def laterais():
	glBegin(GL_QUADS)
	for f in ladof:
		glColor3fv(f[1])
		for p in f[0]:
			glVertex3fv(p)
	glEnd()

def draw_polygon( vert_list, color):
	glBegin(GL_POLYGON)
	glColor3fv(color)
	for p in vert_list:
		glVertex3fv(p)
	glEnd()
 
def desenha():
	global frame
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#	glRotate(1,0,1,0)
	glRotate(1,1,0,0)

	draw_polygon(basef[0],basef[1])
	draw_polygon(tetof[0],tetof[1])
	laterais()

	glutSwapBuffers()
	frame += 1

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow('"CILINDRO"')
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
