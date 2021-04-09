from Normal_Game_R import Normal_Game_R
import random
import os

import rooms.pasillo_lab as pasillo_lab
from colored import fg, bg, attr
import datetime

def logica_bool_game(logica_bool,player):
  """Función donde se ejecuta las mecánicas del juego. Se pide un input, y si coincide con la respuesta dada por la API returna True la función

  Args:
      [Objeto clase Normal_Game_R]: ahorcado, juego normal con requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(logica_bool.get_name().capitalize())
  print(logica_bool.get_rules().capitalize())
  info_question=logica_bool.send_question(random.randint(0,1))
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    guess=input(f"""{info_question["question"]}\n==> """).lower().capitalize()
    if guess == info_question["answer"]:
      return True
    else:
      os.system("clear")
      print("Incorrecto.\n")
      player.set_lives(player.get_lives()-0.5)

def main_logica_booleana(puerta,player):
  """Función principal del juego, mediante atributo del objeto puerta se instancia el juego de la clase Normal_Game_R

  Args:
      [Objeto clase Object]: puerta
      [Player]: información del juegador
  """
  info_game=puerta.get_info_game()
  logica_booleana = Normal_Game_R(info_game["name"], info_game["rules"], info_game["award"], info_game["message_requirement"], info_game["requirement"], info_game["questions"])

  if logica_booleana.get_requirement() in player.get_inventory():
    if logica_bool_game(logica_booleana,player):
      print (f'%sFelicidades, ahora como recompenza obtienes un {logica_booleana.get_award()} %s' % (fg(2), attr(0)))
      player.add_award(logica_booleana.get_award())
      pasillo_lab.main_pasillo_lab(player)
    else: 
     print("Para la próxima será, no te desanimes")
  else:
    print(f'%s{logica_booleana.get_message_requirement()} %s' % (fg(1), attr(0)))
    pasillo_lab.main_pasillo_lab(player)
