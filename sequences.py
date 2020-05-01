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
print(computerResearchers[0:1])
# Devuelve: ['Andrew NG']

print(computerResearchers[1:2])
# Devuelve: ['Yann LeCun']

print(computerResearchers[1:3])
# Devuelve: ['Yann LeCun', 'Yoshua Bengio']

print(computerResearchers[2:6:2])
# <Nombre Lista>[posición inicial : posición final : saltos]
# Devuelve: ['Yoshua Bengio', 'Sebastian Thrun']