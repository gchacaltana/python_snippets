# !/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pow

if __name__=='__main__':

    # Asignación múltiple
    serie_start, serie_end, step, multiplo = 10, 100, 2, 3

    # Creamos la serie S, mediante comprensión de lista.
    s = [n for n in range(serie_start,serie_end+1,step)]

    print(f"\Sucesión:\nS = ",s)
    print(f"\nInicio: {serie_start}\tFin: {serie_end}\tSalto: {step}")

    print(f"\Sucesión S1 conformado por los numeros multiplos de {multiplo} de la sucesión S")
    s1 = [n for n in range(serie_start,serie_end+1,step) if n%3==0]
    print("\nS1 = ", s1)

    print(f"\Sucesión S2 conformado por numeros elevados al cuadrado de la sucesión S1")
    s2 = [pow(n,2) for n in s1]
    print("\nS2 = ",s2)

    print(f"\nSuma de los numeros mayores a 2000 de la sucesión S2 = {sum(n for n in s2 if n>2000)}")