# !/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__=='__main__':

    # Lista 1: Nombre de los jugadores.
    players = ['Alvaro Revoredo', 'Mike Frist', 'Paula Jimenez','Gonzalo Chacaltana','Felipe Ayala']
    
    # Lista 2: País de procedencia.
    countries = ['Uruguay','Brasil','México','Perú','Chile']

    # Lista 3: Puntaje
    scores = [89.2,81.8,83.4,82.6,80.9]

    print("\nResultado ordenado por puntaje de menor a mayor")
    # Creamos una lista de diccionarios a partir de las 3 listas, mediante una sintaxis de compresión.
    competition = [{'score':scores[i], 'player':players[i],'country':countries[i]} for i in range(len(players))]

    for data in sorted(competition, key=lambda x: x['score'], reverse=False):
        print(f"Jugador: {data['player'].ljust(30)}Pais: {data['country'].ljust(15)}Puntaje: {data['score']}")

    # Devuelve
    # Jugador: Felipe Ayala                  Pais: Chile          Puntaje: 80.9
    # Jugador: Mike Frist                    Pais: Brasil         Puntaje: 81.8
    # Jugador: Gonzalo Chacaltana            Pais: Perú           Puntaje: 82.6
    # Jugador: Paula Jimenez                 Pais: México         Puntaje: 83.4
    # Jugador: Alvaro Revoredo               Pais: Uruguay        Puntaje: 89.2

    print("\nResultado ordenado por puntaje de mayor a menor")

    for data in sorted(competition, key=lambda x: x['score'], reverse=True):
        print(f"Jugador: {data['player'].ljust(30)}Pais: {data['country'].ljust(15)}Puntaje: {data['score']}")

    # Devuelve
    # Jugador: Alvaro Revoredo               Pais: Uruguay        Puntaje: 89.2
    # Jugador: Paula Jimenez                 Pais: México         Puntaje: 83.4
    # Jugador: Gonzalo Chacaltana            Pais: Perú           Puntaje: 82.6
    # Jugador: Mike Frist                    Pais: Brasil         Puntaje: 81.8
    # Jugador: Felipe Ayala                  Pais: Chile          Puntaje: 80.9