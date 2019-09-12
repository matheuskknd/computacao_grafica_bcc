#!/usr/bin/env python
# coding: utf-8

from math import pi, sin, cos
from sys import argv

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

A = int(argv[2])+1 if len(argv) >= 3 else 4
N = int(argv[1]) if len(argv) >= 2 else 4

H = 1
R = 2

assert N > 2, "N inválido...\n"
assert A > 0, "A inválido...\n"

#####################################
######## Constroi o polígono ########
#####################################

#####################
# Constroi os polos #
#####################

# Vector3
tetov = (0,H*R,0)

# Vector3
basev = (0,-H*R,0)

#######################
## Constroi os aneis ##
#######################

# List<List<Vector3>>
anel = [[None] * N for i in range(A-1)]

for i in range(A):
	if A != 0 and i+1 == A:
		break
	teta = -(pi/2)+pi*float(i+1)/A
	for j in range(N):
		fi = 2*pi*float(j)/N
		anel[i][j] = (R*cos(teta)*cos(fi),R*sin(teta),R*cos(teta)*sin(fi))

#####################################
## Começa o desenho desse polígono ##
#####################################

frame = 0

def draw_points( vert_list):
	glBegin(GL_POINTS)
	glColor3fv((1,1,1))
	for sublist in vert_list:
		for p in sublist:
			glVertex3fv(p)
	glEnd()

def desenha():
	global frame
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#	glRotate(1,0,1,0)
	glRotate(1,1,0,0)

	draw_points([[basev,tetov]])
	draw_points(anel)

	glutSwapBuffers()
	frame += 1

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)


 
# PROGRAMA PRINCIPAL
glutInit(argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
