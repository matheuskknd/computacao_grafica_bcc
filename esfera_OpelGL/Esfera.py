#!/usr/bin/env python
# coding: utf-8

from math import pi, sin, cos
from random import uniform
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

def rand_color():
	return (uniform(0.000001,1),uniform(0.000001,1),uniform(0.000001,1))

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

########################
# Cria todas as linhas #
########################

# List<Tuple<Vector3,Vector3>>
linha =  [(basev,i) for i in anel[0]]
linha += [(tetov,i) for i in anel[-1]]

for i in range(A-1):
	linha += [(anel[i][j],anel[i][j+1]) for j in range(N-1)]
	linha += [(anel[i][-1],anel[i][0])]

for i in range(A-2):
	linha += [(anel[i][j],anel[i+1][j]) for j in range(N)]

#######################
# Cria todas as faces #
#######################

# Tuple<Tuple<Vector3,Vector3,Vector3>,Color>
tampa =  [((tetov,anel[-1][i],anel[-1][i+1]),rand_color()) for i in range(-1,N-1)]
tampa += [((basev,anel[0][i],anel[0][i+1]),rand_color()) for i in range(-1,N-1)]

# Tuple<Tuple<Vector3,Vector3,Vector3,Vector3>,Color>
lado = []

for i in range(A-2):
	lado += [((anel[i][j],anel[i+1][j],anel[i+1][j+1],anel[i][j+1]),rand_color()) for j in range(-1,N-1)]

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

def draw_trig( faces):
	glBegin(GL_TRIANGLES)
	for f in faces:
		glColor3fv(f[1])
		for p in f[0]:
			glVertex3fv(p)
	glEnd()

def draw_quad( faces):
	glBegin(GL_QUADS)
	for f in faces:
		glColor3fv(f[1])
		for p in f[0]:
			glVertex3fv(p)
	glEnd()

def draw_lines():
	glBegin(GL_LINES)
	glColor3fv((1,1,1))
	for par in linha:
		for p in par:
			glVertex3fv(p)
	glEnd()
 
def desenha():
	global frame
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#	glRotate(1,0,1,0)
	glRotate(1,1,0,0)

	draw_points([[basev,tetov]])
	draw_points(anel)

	draw_lines()

	draw_trig(tampa)
	draw_quad(lado)

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
