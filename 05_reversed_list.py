# !/usr/bin/env python
# -*- coding: utf-8 -*-

books_to_read = ["Python Data Science Handbook", "Understanding Machine Learning", "Linear Algebra Problem Book", "Naked Statistics", "Python for Data Analysis"]
print(f"Libros ordenados por su indice")
print([n for n in books_to_read])
# Devuelve:
# ['Python Data Science Handbook', 'Understanding Machine Learning', 'Linear Algebra Problem Book', 'Naked Statistics', 'Python for Data Analysis']

print(f"\nLibros en orden inverso")
print([n for n in reversed(books_to_read)])
# Devuelve:
# ['Python for Data Analysis', 'Naked Statistics', 'Linear Algebra Problem Book', 'Understanding Machine Learning', 'Python Data Science Handbook']

print(f"\nLibros en ordenados por su nombre")
print([n for n in sorted(books_to_read)])
# Devuelve
# ['Linear Algebra Problem Book', 'Naked Statistics', 'Python Data Science Handbook', 'Python for Data Analysis', 'Understanding Machine Learning']