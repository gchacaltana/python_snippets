# !/usr/bin/env python
# -*- coding: utf-8 -*-

serie_start = 10
serie_end = 100
step = 3
print(f"Inicio: {serie_start}\tFin: {serie_end}\tSalto: {step}")
print([n+1 for n in range(serie_start,serie_end,step) if n<=serie_end])