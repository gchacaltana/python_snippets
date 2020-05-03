# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana Buleje"

from math import sqrt,pow

class Point(object):
    def __init__(self,name, x,y):
        self.name = name
        self.x, self.y = x, y

class CartesianPlane(object):

    def __init__(self, obj_point_a, obj_point_b, obj_point_c):
        self.console_line_length = 40
        self.point_a = obj_point_a
        self.point_b = obj_point_b
        self.point_c = obj_point_c
        
    def calculatePointsDistance(self, point_start, point_end):
        return sqrt(pow(point_end.x-point_start.x,2)+pow(point_end.y-point_start.y,2))
    
    def printPointsDistance(self, point_start, point_end):
        print("{} -> {}: {}".format(point_start.name,point_end.name,self.calculatePointsDistance(point_start,point_end)))

    def displayLegendPoints(self):
        print("\nPuntos: A (x1,y1), B (x2,y2), C (x3,y3)\n")
        self.displayConsoleLine()
        print("Asignacion Multiple de variables\n")
        self.displayConsoleLine()
        print("x1 = 2")
        print("x2, x3 = x1 ^ 2, 5 * x1")
        print("y1, y2, y3 = 2 * x1, x2 ^ 2, (x1 * x2) + 1")
        self.displayConsoleLine()
        print("Punto A (x1,y1): ({},{})".format(self.point_a.x,self.point_a.y))
        print("Punto B (x2,y2): ({},{})".format(self.point_b.x,self.point_b.y))
        print("Punto C (x3,y3): ({},{})".format(self.point_c.x,self.point_c.y))
    
    def displayConsoleLine(self):
        print("\n".ljust(self.console_line_length,'*'),'\n')

    def displayPointsDistance(self):
        self.displayConsoleLine()
        print("Distancia de Puntos")
        self.displayConsoleLine()
        self.printPointsDistance(self.point_a,self.point_b)
        self.printPointsDistance(self.point_a,self.point_c)
        self.printPointsDistance(self.point_b,self.point_c)
    
    def displayTrianglePerimeter(self):
        distance_ab = self.calculatePointsDistance(self.point_a, self.point_b)
        distance_ac = self.calculatePointsDistance(self.point_a, self.point_c)
        distance_bc = self.calculatePointsDistance(self.point_b, self.point_b)
        self.triangle_perimeter = distance_ab + distance_ac + distance_bc
        print("\nEl perimetro del triangulo es {}".format(self.triangle_perimeter))


if __name__=='__main__':
    
    # Asignación múltiple
    x1 = 2
    x2,x3 = pow(x1,2), 5*x1
    y1,y2,y3 = 2*x1, pow(x2,2), x2*x1+1

    point_a = Point('A',x1,y1)
    point_b = Point('B',x2,y2)
    point_c = Point('C',x3,y3)
    
    plane = CartesianPlane(point_a, point_b, point_c)
    plane.displayLegendPoints()
    plane.displayPointsDistance()
    plane.displayTrianglePerimeter()