import requests
from blessed import Terminal
from Room import Room
from Object import Object
import os
import datetime

import rooms.biblioteca_room as biblioteca_room

import minigames.logica as logica
import minigames.quizizz as quizizz
import minigames.memoria as memoria

import designs_room 

def set_room(info_rooms):
  """Con la información del diccionario, sacada de la API instancia la habitación y los direrentes objetos

  Args:
      [Player]: información del juegador

  Returns:
      [Objeto clase Room]: plaza_rectorado
      [Objeto clase Object]: saman, banco_1, banco_2
  """
  plaza_rectorado=Room(info_rooms[2]["name"])
  saman=Object(info_rooms[2]["objects"][0]["name"].title())
  saman.set_position(info_rooms[2]["objects"][0]["position"])
  saman.set_game(info_rooms[2]["objects"][0]["game"])
  banco_1=Object(info_rooms[2]["objects"][1]["name"].title())
  banco_1.set_position(info_rooms[2]["objects"][1]["position"])
  banco_1.set_game(info_rooms[2]["objects"][1]["game"])
  banco_2=Object(info_rooms[2]["objects"][2]["name"].title())
  banco_2.set_position(info_rooms[2]["objects"][2]["position"])
  banco_2.set_game(info_rooms[2]["objects"][2]["game"])

  plaza_rectorado.add_object(saman)
  plaza_rectorado.add_object(banco_1)
  plaza_rectorado.add_object(banco_2)
  plaza_rectorado.set_design(designs_room.saman_design())

  return plaza_rectorado, saman, banco_1, banco_2


def info_API():
  url="https://api-escapamet.vercel.app/"
  response = requests.get(url)
  return response.json()

def main_plaza_rectorado(player):
  """Función principal de la plaza de rectorado, donde se setea toda la información relacionada a la biblioteca, objetos y juegos que pertenecen a ella. Tiene la condición que si no tienes en tu inventario el libro de Física conseguido en el juego pasado, no puedes pasar a esta habitación.

  Args:
      [Player]: información del juegador
  """
  info_rooms=info_API()
  plaza_rectorado, saman, banco_1, banco_2 = set_room(info_rooms)
  print(plaza_rectorado.get_design())
  
  while (player.get_time_left() > datetime.timedelta()) and (player.get_lives() > 0) and  ("Parar el cronómetro y ganar el juego" not in player.get_inventory()):
    option=input("""Ingrese qué desee hacer: 
  (D) Moverse hacia la derecha
  (1) Tocar objeto
  (2) Ver inventario
  (3) Ver tiempo restante
  (4) Ver vidas y pistas restantes
  ==> """).upper()
    if option=="D":
      os.system("clear")
      biblioteca_room.main_biblioteca(player)
    elif option=="1":
      plaza_rectorado.show_objects()
      option=input("Ingrese el número de objeto que desee agarrar objeto desea agarrar: ")
      os.system("clear")
      if option=="1":
        logica.main_logica(saman,player)
      elif option=="2":
        quizizz.main_quizizz(banco_1,player)
      elif option=="3":
        memoria.main_memoria(banco_2,player)
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

  #player.pause(player)