# !/usr/bin/env python
# -*- coding: utf-8 -*-

computerResearchers = ["Andrew NG", "Yann LeCun", "Yoshua Bengio", "Carol Reiley", "Sebastian Thrun", "Jeff Dean", "Pieter Abbeel"]
# Indices de la Lista computerResearchers
# 0 => Andrew NG 
# 1 => Yann LeCun
# 2 => Yoshua Bengio
# 3 => Carol Reiley
# 4 => Sebastian Thrun
# 5 => Jeff Dean
# 6 => Pieter Abbeel

# <Nombre Lista>[posición inicial : posición final]
# Si la posición final ("n") es 2, python lo interpreta como 1. Siempre es "n" - 1
print(computerResearchers[0:1])
# Devuelve: ['Andrew NG']

print(computerResearchers[1:2])
# Devuelve: ['Yann LeCun']

print(computerResearchers[1:3])
# Devuelve: ['Yann LeCun', 'Yoshua Bengio']

print(computerResearchers[2:6:2])
# <Nombre Lista>[posición inicial : posición final : saltos]
# Devuelve: ['Yoshua Bengio', 'Sebastian Thrun']

print(computerResearchers[:3])
# <Nombre Lista>[ : posición final]
# Si la posición inicial es vacío es igual a 0.
# Devuelve: ['Andrew NG', 'Yann LeCun', 'Yoshua Bengio']

print(computerResearchers[4:])
# <Nombre Lista>[posición inicial : ]
# Si la posición final es vacío significa que python cogerá hasta el último elemento de la lista.
# Devuelve: ['Sebastian Thrun', 'Jeff Dean', 'Pieter Abbeel']

print(computerResearchers[:])
# <Nombre Lista>[ : ]
# Si la posición inicial y final están vacíos, python cogerá todos los elementos de la lista.
# Devuelve: ['Andrew NG', 'Yann LeCun', 'Yoshua Bengio', 'Carol Reiley', 'Sebastian Thrun', 'Jeff Dean', 'Pieter Abbeel']