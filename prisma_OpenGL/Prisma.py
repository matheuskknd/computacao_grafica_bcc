#!/usr/bin/env python
# coding: utf-8

from math import pi, sin, cos
from sys import argv, stdout
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

N = int(argv[1]) if len(argv) == 2 else 4
FPS = 50
H = 5
R = 5
assert N > 0, "N inválido...\n"

#####################################
# Começa criação lógica do polígono #
#####################################

############################################
# Constroi a base

# List<Vector3>
basev = [(R*sin(2*pi*(float(i)/N)),0,R*cos(2*pi*(float(i)/N))) for i in range(N)]

# List<Tuple<Vector3,Vector3>>
#basel = [(basev[-1],basev[0])]
#basel += [(basev[i],basev[i+1]) for i in range(len(basev)-1)]

# List<Vector3>
basef = basev

############################################
# Adiciona o topo e suas respectivas linhas

# Vector3
topov = (0,H,0)

# List<Tuple<Vector3,Vector3>>
#topol = [(topov,basev[i]) for i in range(len(basev))]

# List<Tuple<Vector3,Vector3,Vector3>>
topof = [(topov,basev[-1],basev[0])]
topof += [(topov,basev[i],basev[i+1]) for i in range(len(basev)-1)]

#####################################
## Começa o desenho desse polígono ##
#####################################

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
frame = 0

def laterais():
	glBegin(GL_TRIANGLES)
	k = 0
	for f in topof:
		glColor3fv(cores[k%len(cores)])
		k += 1
		for p in f:
			glVertex3fv(p)
	glEnd()

def fundo():
	glBegin(GL_POLYGON)
	for p in basev:
		glVertex3fv(p)
	glEnd()
 
def desenha():
	global frame
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#	glRotate(1,0,1,0)
	glRotate(1,1,0,0)
	laterais()
	fundo()

	glutSwapBuffers()
	frame += 1
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(1000/FPS,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
