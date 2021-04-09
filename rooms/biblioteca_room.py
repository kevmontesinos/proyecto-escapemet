import requests
from Room import Room
from Object import Object
import os
import datetime
import minigames.ahorcado as ahorcado
import minigames.preguntas_matematica as preguntas_matematica
import minigames.cifrado as cifrado

import rooms.plaza_rectorado_room as plaza_rectorado_room 
import rooms.pasillo_lab as pasillo_lab

import designs_room 

def set_room(info_rooms):
  """Con la información del diccionario, sacada de la API instancia la habitación y los direrentes objetos

  Args:
      [Player]: información del juegador

  Returns:
      [Objeto clase Room]: biblioteca
      [Objeto clase Object]: mueble_libros, mueble_sentarse, mueble_gabetas
  """ 
  info_rooms=info_API()
  biblioteca=Room(info_rooms[1]["name"])
  mueble_libros=Object(info_rooms[1]["objects"][0]["name"].title())
  mueble_libros.set_position(info_rooms[1]["objects"][0]["position"])
  mueble_libros.set_game(info_rooms[1]["objects"][0]["game"])
  mueble_sentarse=Object(info_rooms[1]["objects"][1]["name"].title())
  mueble_sentarse.set_position(info_rooms[1]["objects"][1]["position"])
  mueble_sentarse.set_game(info_rooms[1]["objects"][1]["game"])
  mueble_gabetas=Object(info_rooms[1]["objects"][2]["name"].title())
  mueble_gabetas.set_position(info_rooms[1]["objects"][2]["position"])
  mueble_gabetas.set_game(info_rooms[1]["objects"][2]["game"])
  biblioteca.add_object(mueble_libros)
  biblioteca.add_object(mueble_sentarse)
  biblioteca.add_object(mueble_gabetas)
  biblioteca.set_design(designs_room.biblioteca_design())

  return biblioteca, mueble_libros, mueble_sentarse, mueble_gabetas 

def info_API():
  """Coloca los datos de la API en un diccioanario
      
  Returns:
      [dic]: info_rooms, diccionario extraído de la API que guarda toda la información de todos los juegos
  """ 
  url="https://api-escapamet.vercel.app/"
  response = requests.get(url)
  return response.json()

def main_biblioteca(player):
  """Función principal de la biblioteca, donde se setea toda la información relacionada a la biblioteca, objetos y juegos que pertenecen a ella.

  Args:
      [Player]: información del juegador

  Returns:
      [Bool] True, si se ganó el juego, False, si se perdió.
  """ 
  info_rooms=info_API()
  biblioteca, mueble_libros, mueble_sentarse, mueble_gabetas=set_room(info_rooms)
  print(biblioteca.get_design())
  

  while (player.get_time_left() > datetime.timedelta()) and (player.get_lives() > 0) and  ("Parar el cronómetro y ganar el juego" not in player.get_inventory()):
    option=input("""Ingrese qué desee hacer: 
    (A) Moverse hacia la izquierda o (D) moverse hacia la derecha
    (1) Tocar objeto
    (2) Ver inventario
    (3) Ver tiempo restante
    (4) Ver vidas y pistas restantes
    ==> """).upper()
    if option=="A":
      os.system("clear")
      plaza_rectorado_room.main_plaza_rectorado(player)
    elif option=="D":
      os.system("clear")
      pasillo_lab.main_pasillo_lab(player)
    elif option=="1":
      biblioteca.show_objects()
      option=input("Ingrese el número de objeto que desee agarrar objeto desea agarrar: ")
      os.system("clear")
      if option=="1":
        ahorcado.main_ahorcado(mueble_libros,player)
      elif option=="2":
        preguntas_matematica.main_preguntas_mate(mueble_sentarse,player)
      elif option=="3":
        cifrado.main_cifrado(mueble_gabetas,player)
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

  if player.get_time_left() < datetime.timedelta() or player.get_lives() < 0:
    return False
  elif "Parar el cronómetro y ganar el juego" in player.get_inventory():
    return True
  
  

    

  
