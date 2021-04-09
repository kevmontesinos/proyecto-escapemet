import requests
from blessed import Terminal
from Room import Room
from Object import Object
import os
import datetime

import minigames.logica_booleana as logica_booleana

import rooms.laboratorio_room as laboratorio_room
import rooms.biblioteca_room as biblioteca_room

import designs_room 

def set_room(info_rooms):
  """Con la información del diccionario, sacada de la API instancia la habitación y los direrentes objetos

  Args:
      [Player]: información del juegador

  Returns:
      [Objeto clase Room]: pasillo_laboratorios
      [Objeto clase Object]: puerta
  """
  pasillo_laboratorios=Room(info_rooms[3]["name"])
  puerta=Object(info_rooms[3]["objects"][0]["name"].title())
  puerta.set_position(info_rooms[3]["objects"][0]["position"])
  puerta.set_game(info_rooms[3]["objects"][0]["game"])

  pasillo_laboratorios.add_object(puerta)
  pasillo_laboratorios.set_design(designs_room.puerta_design())

  return pasillo_laboratorios, puerta

def info_API():
  url="https://api-escapamet.vercel.app/"
  response = requests.get(url)
  return response.json()

def main_pasillo_lab(player):
  """Función principal del pasillo de laboratorios, donde se setea toda la información relacionada a la biblioteca, objetos y juegos que pertenecen a ella. Tiene la condición que si no tienes en tu inventario el libro de Física conseguido en el juego pasado, no puedes pasar a esta habitación.

  Args:
      [Player]: información del juegador

  """
  info_rooms=info_API()
  pasillo_laboratorios, puerta = set_room(info_rooms)
  print(pasillo_laboratorios.get_design())

  while (player.get_time_left() > datetime.timedelta()) and (player.get_lives() > 0) and "Parar el cronómetro y ganar el juego" not in player.get_inventory():
    option=input("""Ingrese qué desee hacer: 
    (A) Moverse hacia la izquierda o (D) moverse hacia la derecha
    (1) Tocar objeto
    (2) Ver inventario 
    (3) Ver tiempo restante
    (4) Ver vidas y pistas restantes
    ==> """).upper()
    if option=="A":
      biblioteca_room.main_biblioteca(player)
    elif option=="D":
      laboratorio_room.main_laboratorio(player)
    elif option=="1":
      pasillo_laboratorios.show_objects()
      option=input("Ingrese el número de objeto que desee agarrar objeto desea agarrar: ")
      if option=="1":
        os.system("clear")
        logica_booleana.main_logica_booleana(puerta,player)
      else:
        print("Por favor, elija una opción válida")
    elif option=="2":
      player.show_inventory()
    elif option=="3":
      if player.get_time_left() > datetime.timedelta():
        print("⏱  Tiempo restante: ")
        print(player.get_time_left())
      else:
        pass
    elif option=="4":
      player.get_bar_health()    
    else:
      print("Elija una opción válida")
