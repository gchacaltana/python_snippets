# !/usr/bin/env python
# -*- coding: utf-8 -*-

researcher = "Andrew NG"
# El contenido de una cadena de texto se comporta como una lista.
# 0 => A
# 1 => n
# 2 => d
# 3 => r
# 4 => e
# 5 => w
# 6 =>  
# 7 => N
# 8 => G

print(researcher[0:6])
# Devuelve: Andrew

print(researcher[7:9])
# Devuelve: NG

print(researcher[::-1])
# Devuelve: GN werdnA

# Secuencia Inversa
# Podemos interpretar las posiciones inversas de la siguiente forma:
# -9 => A
# -8 => n
# -7 => d
# -6 => r
# -5 => e
# -4 => w
# -3 =>  
# -2 => N
# -1 => G
print(researcher[-1])
# Devuelve: G

print(researcher[-2:])
# Devuelve: NG

print(researcher[-9:-3])
# Devuelve: Andrew