import requests
from blessed import Terminal
from Room import Room
from Object import Object
import os
import datetime

import rooms.laboratorio_room as laboratorio_room

import minigames.final_game as final_game
import minigames.palabra_mezclada as palabra_mezclada
import minigames.numero_entre as numero_entre

import designs_room 

def set_room(info_rooms):
  """Con la información del diccionario, sacada de la API instancia la habitación y los direrentes objetos

  Args:
      [Player]: información del juegador

  Returns:
      [Objeto clase Room]: cuarto_servidores
      [Objeto clase Object]: puerta, rack, papelera
  """
  cuarto_servidores=Room(info_rooms[2]["name"])
  puerta=Object(info_rooms[4]["objects"][0]["name"].title())
  puerta.set_position(info_rooms[4]["objects"][0]["position"])
  puerta.set_game(info_rooms[4]["objects"][0]["game"])
  rack=Object(info_rooms[4]["objects"][1]["name"].title())
  rack.set_position(info_rooms[4]["objects"][1]["position"])
  rack.set_game(info_rooms[4]["objects"][1]["game"])
  papelera=Object(info_rooms[4]["objects"][2]["name"].title())
  papelera.set_position(info_rooms[4]["objects"][2]["position"])
  papelera.set_game(info_rooms[4]["objects"][2]["game"])

  cuarto_servidores.add_object(puerta)
  cuarto_servidores.add_object(rack)
  cuarto_servidores.add_object(papelera)
  cuarto_servidores.set_design(designs_room.server_design())

  return cuarto_servidores, puerta, rack, papelera

def info_API():
  url="https://api-escapamet.vercel.app/"
  response = requests.get(url)
  return response.json()

def main_server_room(player):
  info_rooms=info_API()
  cuarto_servidores, puerta, rack, papelera = set_room(info_rooms)
  print(cuarto_servidores.get_design())
  

  while (player.get_time_left() > datetime.timedelta()) and (player.get_lives() > 0) and "Parar el cronómetro y ganar el juego" not in player.get_inventory():
    option=input("""Ingrese qué desee hacer: 
    (A) Moverse hacia la izquierda 
    (1) Tocar objeto
    (2) Ver inventario
    (3) Ver tiempo restante
    (4) Ver vidas y pistas restantes
    ==> """).upper()
    if option=="A":
      laboratorio_room.main_laboratorio(player)
    elif option=="1":
      cuarto_servidores.show_objects()
      option=input("Ingrese el número de objeto que desee agarrar objeto desea agarrar: ")
      if option=="1":
        #os.system("clear")
        final_game.main_final_game(puerta, player)
      elif option=="2":
        #os.system("clear")
        palabra_mezclada.main_palabra_mezclada(rack,player)
      elif option=="3":
        #os.system("clear")
        numero_entre.main_numero_entre(papelera,player)
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