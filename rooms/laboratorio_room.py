import requests
from blessed import Terminal
from Room import Room
from Object import Object
import os
import datetime

import minigames.sopa_letras as sopa_letras
import minigames.preguntas_python as preguntas_python
import minigames.adivinanzas as adivinanzas

import rooms.pasillo_lab as pasillo_lab
import rooms.server_room as server_room

import designs_room 

def set_room(info_rooms):
  """Con la información del diccionario, sacada de la API instancia la habitación y los direrentes objetos

  Args:
      [Player]: información del juegador

  Returns:
      [Objeto clase Room]: laboratorio_sl001
      [Objeto clase Object]: pizarra, compu_1, compu_2
  """
  info_rooms=info_API()
  laboratorio_sl001=Room(info_rooms[0]["name"])
  pizarra=Object(info_rooms[0]["objects"][0]["name"].title())
  pizarra.set_position(info_rooms[0]["objects"][0]["position"])
  pizarra.set_game(info_rooms[0]["objects"][0]["game"])
  compu_1=Object(info_rooms[0]["objects"][1]["name"].title())
  compu_1.set_position(info_rooms[0]["objects"][1]["position"])
  compu_1.set_game(info_rooms[0]["objects"][1]["game"])
  compu_2=Object(info_rooms[0]["objects"][2]["name"].title())
  compu_2.set_position(info_rooms[0]["objects"][2]["position"])
  compu_2.set_game(info_rooms[0]["objects"][2]["game"])

  laboratorio_sl001.add_object(pizarra)
  laboratorio_sl001.add_object(compu_1)
  laboratorio_sl001.add_object(compu_2)
  laboratorio_sl001.set_design(designs_room.laboratorio_design())
  laboratorio_sl001.set_design(designs_room.laboratorio_design())

  return laboratorio_sl001, pizarra, compu_1, compu_2


def info_API():
  url="https://api-escapamet.vercel.app/"
  response = requests.get(url)
  return response.json()

def main_laboratorio(player):
  """Función principal del laboratorio, donde se setea toda la información relacionada a la biblioteca, objetos y juegos que pertenecen a ella. Tiene la condición que si no tienes en tu inventario el libro de Física conseguido en el juego pasado, no puedes pasar a esta habitación.

  Args:
      [Player]: información del juegador
  """
  if "libro de Física" in player.get_inventory():
    info_rooms= info_API()
    laboratorio_sl001, pizarra, compu_1, compu_2=set_room(info_rooms)
    print(laboratorio_sl001.get_design())

    while (player.get_time_left() > datetime.timedelta()) and (player.get_lives() > 0) and "Parar el cronómetro y ganar el juego" not in player.get_inventory():
      option=input("""Ingrese qué desee hacer: 
      (A) Moverse hacia la izquierda o (D) moverse hacia la derecha
      (1) Tocar objeto
      (2) Ver inventario 
      (3) Ver tiempo restante
      (4) Ver vidas y pistas restantes
      ==> """).upper()
      if option=="A":
        pasillo_lab.main_pasillo_lab(player)
      elif option=="D":
        server_room.main_server_room(player)
      elif option=="1":
        laboratorio_sl001.show_objects()
        option=input("Ingrese el número de objeto que desee agarrar objeto desea agarrar: ")
        os.system("clear")
        if option=="1":
          sopa_letras.main_sopa_letras(pizarra,player)
        elif option=="2":
          preguntas_python.main_preguntas_python(compu_1,player)
        elif option=="3":
          adivinanzas.main_adivinanzas(compu_2,player)
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
  else:
    os.system("clear")
    print("Primero tienes que completar el juego del pasillo para abrir la puerta.")
    pasillo_lab.main_pasillo_lab(player)
    