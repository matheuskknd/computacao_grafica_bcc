#!/usr/bin/env python
# coding: utf-8

from math import pi, sin, cos
from random import uniform
from math import sqrt
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

#https://www.opengl.org/wiki/Calculating_a_Surface_Normal
#Begin Function CalculateSurfaceNormal (Input Triangle) Returns Vector
#  Set Vector U to (Triangle.p2 minus Triangle.p1)
#  Set Vector V to (Triangle.p3 minus Triangle.p1)
#  Set Normal.x to (multiply U.y by V.z) minus (multiply U.z by V.y)
#  Set Normal.y to (multiply U.z by V.x) minus (multiply U.x by V.z)
#  Set Normal.z to (multiply U.x by V.y) minus (multiply U.y by V.x)
#  Returning Normal
#End Function

# Type: Tuple[Vector3,Vector3,Vector3]
def calculaNormalFace(face):
	x = 0
	y = 1
	z = 2

	v0 = face[0]
	v1 = face[1]
	v2 = face[2]

	U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
	V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )

	N = ( U[y]*V[z]-U[z]*V[y], U[z]*V[x]-U[x]*V[z], U[x]*V[y]-U[y]*V[x] )
	NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])

	return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

# Type: List[Tuple[Tuple[Vector3,Vector3,Vector3,Vector3],Color]]
def draw_quad( faces):
	glBegin(GL_QUADS)

	for face in faces:
		glNormal3fv(calculaNormalFace(face[0]))
		glColor3fv(face[1])	# FIXME

		for vertex in face[0]:
			glVertex3fv(vertex)

	glEnd()

# Type: List[Tuple[List[Vector3],Color]]
def draw_polygon( faces):
	for face in faces:
		glBegin(GL_POLYGON)

		glNormal3fv(calculaNormalFace(face[0]))
		glColor3fv(face[1])	# FIXME

		for vertex in face[0]:
			glVertex3fv(vertex)

		glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glRotatef(2,1,3,0)

	draw_polygon([basef,tetof])
	draw_quad(ladof)

	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	gluPerspective(45,float(w)/h,0.1,50.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
#	mat_ambient = (0.0, 0.0, 0.5, 1.0)
	mat_ambient = (0.8, 0.0, 0.0, 1.0)
	mat_diffuse = (1.0, 0.0, 0.0, 1.0)
	mat_specular = (1.0, 1.0, 1.0, 1.0)
	mat_shininess = [100]
	light_position = (0, 8, 0)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_SMOOTH)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)

if __name__ == '__main__':

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow('"CILINDRO" Delux')
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutTimerFunc(50,timer,1)
	init()
	glutMainLoop()

