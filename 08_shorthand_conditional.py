# !/usr/bin/env python
# -*- coding: utf-8 -*-
from statistics import mean

score_exams = [16,14,17,11,13]
min_score = 13

score_course = mean(score_exams)
# utilizando una expresión condicional abreviada ó shorthand conditional
state_course = 'Aprobado' if score_course>=min_score else 'Desaprobado'

print(f'\nNotas de Evaluaciones: ', str(score_exams))
print(f'Promedio mínimo para aprobar: {min_score}')
print(f'Estado: {state_course.ljust(12)} Promedio Final: {score_course}')