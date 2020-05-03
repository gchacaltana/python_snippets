# !/usr/bin/env python
# -*- coding: utf-8 -*-

__file__ = "Triangle.py"

from math import sqrt,pow

class Triangle(object):

    def __init__(self, obj_point_a, obj_point_b, obj_point_c):
        self.point_a = obj_point_a
        self.point_b = obj_point_b
        self.point_c = obj_point_c
    
    def calculateDistance(self, point_start, point_end):
        return sqrt(pow(point_end.x - point_start.x, 2) + pow(point_end.y - point_start.y, 2))
    
    def build(self):
        self.side_AB = self.calculateDistance(self.point_a, self.point_b)
        self.side_AC = self.calculateDistance(self.point_a, self.point_c)
        self.side_BC = self.calculateDistance(self.point_b, self.point_c)
    
    def getPerimeter(self):
        return self.side_AB + self.side_BC + self.side_AC
