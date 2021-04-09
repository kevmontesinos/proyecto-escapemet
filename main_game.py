from blessed import Terminal
import os
import rooms.biblioteca_room as biblioteca_room
import time

def set_time(player):
  """Coloca el tiempo futuro que tiene el jugador para completar el juego.
  Args:
      [Player]: información del juegador
  """
  player.set_time_future(player.get_time() + time.time())

def main_game(player):
  """Función secundario del juego.

  Args:
      [Player]: información del juegador

  Returns:
      [Bool] True, si se ganó el juego, False, si se perdió.
  """ 

  term = Terminal()
  print(f"{term.home}{term.clear}")
  print(f"""Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {player.get_time()/60} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?
  Presiona 's' para aceptar el reto. """)
  with term.cbreak():
    val = ''
    while val.lower() != "s":
      val = term.inkey(timeout=2)   
  os.system("clear")
  print(f"""Bienvenido {player.get_avatar()} gracias por tu disposición a ayudarnos a resolver este inconveniente, te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.""")
  set_time(player)

  if biblioteca_room.main_biblioteca(player):
    return True
  else:
    return False