# !/usr/bin/env python
# -*- coding: utf-8 -*-

__file__ = "__main__.py"
__author__ = "Gonzalo Chacaltana"

from Triangle import Triangle
from Point import Point

class App(object):
    def __init__(self):
        self.console_line_length = 40

    def display(self, triangle):
        self.triangle = triangle
        self.displayLegendPoints()
        self.displayPointsDistance()
        self.displayTrianglePerimeter()

    def displayLegendPoints(self):
        print("\nPuntos: A (x1,y1), B (x2,y2), C (x3,y3)\n")
        self.displayConsoleLine()
        print("Asignacion Multiple de variables\n")
        self.displayConsoleLine()
        print("x1 = 2")
        print("x2, x3 = x1 ^ 2, 5 * x1")
        print("y1, y2, y3 = 2 * x1, x2 ^ 2, (x1 * x2) + 1")
        self.displayConsoleLine()
        print("Punto {} (x,y): ({},{})".format(self.triangle.point_a.name,self.triangle.point_a.x,self.triangle.point_a.y))
        print("Punto {} (x,y): ({},{})".format(self.triangle.point_b.name,self.triangle.point_b.x,self.triangle.point_b.y))
        print("Punto {} (x,y): ({},{})".format(self.triangle.point_c.name,self.triangle.point_c.x,self.triangle.point_c.y))
    
    def displayConsoleLine(self):
        print("\n".ljust(self.console_line_length,'*'),'\n')

    def displayPointsDistance(self):
        self.displayConsoleLine()
        print("Distancia de Puntos")
        self.displayConsoleLine()
        print("{} -> {}: {}".format(self.triangle.point_a.name,self.triangle.point_b.name,self.triangle.side_AB))
        print("{} -> {}: {}".format(self.triangle.point_a.name,self.triangle.point_c.name,self.triangle.side_AC))
        print("{} -> {}: {}".format(self.triangle.point_b.name,self.triangle.point_c.name,self.triangle.side_BC))
        
    
    def displayTrianglePerimeter(self):
        print("\nEl perimetro del triangulo es {}".format(self.triangle.getPerimeter()))

if __name__=='__main__':
    
    # Asignación múltiple de variables.
    x1 = 2
    x2,x3 = pow(x1,2), 5*x1
    y1,y2,y3 = 2*x1, pow(x2,2), x2*x1+1

    point_a = Point('A',x1,y1)
    point_b = Point('B',x2,y2)
    point_c = Point('C',x3,y3)
    
    triangle = Triangle(point_a, point_b, point_c)
    triangle.build()

    console = App()
    console.display(triangle)
    