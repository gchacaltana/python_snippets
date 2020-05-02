# !/usr/bin/env python
# -*- coding: utf-8 -*-

def isGoodPassword(password:str):
    len_password = len(password)>8
    has_symbols = not set('@&$_').isdisjoint(password.lower())
    has_numbers = not set('1234567890').isdisjoint(password.lower())
    has_vowels = not set('aeiou').isdisjoint(password.lower())
    return has_symbols & len_password & has_numbers & has_vowels

if __name__ == '__main__':

    passwords = ['123456','sistemas','xf@9ops_','segura','zx3kulP@i_','secreto','v8$nbep1bf_','cumple1304']

    print(list(filter(isGoodPassword,passwords)))

# Devuelve:
# ['zx3kulP@i_', 'v8$nbep1bf_']