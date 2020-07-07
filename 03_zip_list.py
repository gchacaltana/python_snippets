# !/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__=='__main__':

    # Lista 1: Nombre de los jugadores.
    players = ['Alvaro Revoredo', 'Mike Frist', 'Paula Jimenez','Gonzalo Chacaltana','Felipe Ayala']
    
    # Lista 2: País de procedencia.
    countries = ['Uruguay','Brasil','México','Perú','Chile']

    # Lista 3: Puntaje
    scores = [89.2,81.8,83.4,82.6,80.9]

    # Utilizamos la función zip() para unir las 3 listas.
    for player,country,score in zip(players,countries,scores):
        print('Jugador: {} Pais: {} Puntaje: {}'.format(player.ljust(30),country.ljust(15),score))

    # Devuelve
    # Jugador: Alvaro Revoredo               Pais: Uruguay         Puntaje: 89.2
    # Jugador: Mike Frist                    Pais: Brasil          Puntaje: 81.8
    # Jugador: Paula Jimenez                 Pais: México          Puntaje: 83.4
    # Jugador: Gonzalo Chacaltana            Pais: Perú            Puntaje: 82.6
    # Jugador: Felipe Ayala                  Pais: Chile           Puntaje: 80.9