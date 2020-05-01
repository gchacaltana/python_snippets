# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana Buleje"
from statistics import mean

def average(a,b):
    return mean([a,b])

courses = ['Programación de Sistemas','Estadística Básica', 'Algebra Lineal', 'Matrices Distribuidas', 'Redes Neuronales']
score_01, score_02, score_min = [15,18,12,19,13], [18,16,13,16,18], 13

# Usamos "map" para invocar función "average" a cada elemento de las listas.
score_course_final = list(map(average,score_01,score_02))
score_final = mean(score_course_final)

if __name__ == "__main__":
    for x in range(0,len(courses)):
        print("\nCurso: {}".format(courses[x]))
        print("\n{} {}".format('Nota 1 :'.ljust(14),score_01[x]))
        print("{} {}".format('Nota 2 :'.ljust(14),score_02[x]))
        print("{} {}".format('Nota Final :'.ljust(14),score_course_final[x]))
        print("Estado: {}".format('Aprobado' if score_course_final[x]>=score_min else 'Desaprobado'))
        print("\n{}".format(''.ljust(30,'*')))
    print("\nPromedio Final: {}".format(score_final))
    print("Estado Final: {}".format('Aprobado' if score_final>=score_min else 'Desaprobado'))

# Devuelve
# Curso: Programación de Sistemas

# Nota 1 :       15
# Nota 2 :       18
# Nota Final :   16.5
# Estado: Aprobado

# ******************************

# Curso: Estadística Básica

# Nota 1 :       18
# Nota 2 :       16
# Nota Final :   17
# Estado: Aprobado

# ******************************

# Curso: Algebra Lineal

# Nota 1 :       12
# Nota 2 :       13
# Nota Final :   12.5
# Estado: Desaprobado

# ******************************

# Curso: Matrices Distribuidas

# Nota 1 :       19
# Nota 2 :       16
# Nota Final :   17.5
# Estado: Aprobado

# ******************************

# Curso: Redes Neuronales

# Nota 1 :       13
# Nota 2 :       18
# Nota Final :   15.5
# Estado: Aprobado

# ******************************

# Promedio Final: 15.8
# Estado Final: Aprobado