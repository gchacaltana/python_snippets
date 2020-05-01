# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Declaración y asignación múltiple de variables.
x ,y, z = 2, 3, 5

# x = 2
# y = 3
# z = 5

print(f"\n1ra Asignacion")
print(f"x = {x} \ty = {y}\tz = {z}")
# Devuelve: 2 3 5

print(f"\n2da Asignacion")
print(f"y, x = x, z")
y, x = x, z
# y = x
# x = z

print(f"x = {x} \ty = {y}\tz = {z}")
# Devuelve:
# x = 5
# y = 2
# z = 5

print(f"\n3ra Asignacion")
print(f"x, z = 2y, 3x")
x, z = 2*y, 3*x
# x = 2y
# z = 3x

print(f"x = {x} \ty = {y}\tz = {z}")

# Ejemplo
# r = 2x + 3y - 2z

r = 2*x + 3*y - 2*z
print(f"\nr = 2x + 3y - 2z")
print(f"r = 2({x}) + 3({y}) - 2({z})")
print(f"r = {r}")