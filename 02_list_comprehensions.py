# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math

serie_start, serie_end, step, multiplo = 10, 100, 2, 3
print(f"\nSerie:\nS = 10,12,14,16,18, ... , 100")
print(f"\nInicio: {serie_start}\tFin: {serie_end}\tSalto: {step}")

print(f"\nSerie S1 conformado por numeros multiplos de {multiplo} de la serie S")
s1 = [n for n in range(serie_start,serie_end+1,step) if n%3==0]
print("S1 = ", s1)

print(f"\nSerie S2 conformado por numeros elevados al cuadrado de la serie S1")
s2 = [math.pow(n,2) for n in s1]
print("S2 = ",s2)

print(f"\nSuma de los numeros mayores a 2000 de la serie S2")
print(sum(n for n in s2 if n>2000))