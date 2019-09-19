#!/usr/bin/env python
# coding: utf-8

from math import pi, sin, cos
from random import uniform
from sys import argv

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

Dx = 0.1
Dy = 0.1

X0 = -1
Y0 = -1

XN = 1
YN = 1

#####################################
######## Constroi o polígono ########
#####################################

def f(x,y):
	return x**2 + y**2

def fcor(x,y):
	return (abs(x-X0)/abs(X0-XN),abs(y-Y0)/abs(Y0-YN),0)

#####################################
## Começa o desenho desse polígono ##
#####################################

frame = 0

def draw():
	y = Y0
	while y < YN:
		x = X0
		glBegin(GL_QUAD_STRIP)
		while x < XN:
			glColor3fv(fcor(x,y))
			glVertex3fv((x,y,f(x,y)))
			glColor3fv(fcor(x,y))
			glVertex3fv((x,y+Dy,f(x,y+Dy)))
			x += Dx
		glEnd()
		y += Dy

def desenha():
	global frame
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#	glRotate(1,0,1,0)
	glRotate(1,1,0,0)

	draw()

#	draw_polygon(basef[0],basef[1])
#	draw_polygon(tetof[0],tetof[1])
#	laterais()

	glutSwapBuffers()
	frame += 1

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow('Malha')
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
