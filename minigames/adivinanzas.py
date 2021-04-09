from Normal_Game_R import Normal_Game_R
import random
from colored import fg, bg, attr
import rooms.laboratorio_room as laboratorio_room
import os
import datetime

def get_clue(player, info_question, n_clue):
  clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
  if clue == "S":
    if n_clue<=3 and player.get_clues_count() > 0:
      print(info_question[f"clue_{n_clue}"])
      player.set_clues_count(player.get_clues_count() - 1)
      return n_clue+1
    else:
      print("No te quedan pistas")
  return n_clue

def adivinanzas_game(adivinanzas,player):
  """Función donde se ejecuta las mecánicas del juego. Se selecciona una de las preguntas que hay en el API, y si el jugador acierta alguna de las palabras retorna True.

  Args:
      [Objeto clase Normal_Game_R]: adivinanzas, juego normal con requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(adivinanzas.get_name())
  print(adivinanzas.get_rules().capitalize())
  question_n=random.randint(0,2)
  info_question=adivinanzas.send_question(question_n)
  n_clue=1
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    guess=input(f"""{info_question["question"]}\n==> """)
    if guess in info_question["answers"]:
      return True
    else:
      print("No es correcto. Pierdes media vida")
      player.set_lives(player.get_lives() - 0.5)
      n_clue=get_clue(player, info_question, n_clue) 

def main_adivinanzas(compu_2,player):
  os.system("clear")
  info_game=compu_2.get_info_game()
  adivinanzas = Normal_Game_R(info_game["name"], info_game["rules"], info_game["award"], info_game["message_requirement"], "contraseña", info_game["questions"])
  
  if adivinanzas.get_requirement() in player.get_inventory():
    if adivinanzas_game(adivinanzas,player):
      print (f'%sFelicidades, ahora como recompenza obtienes una {adivinanzas.get_award()} %s' % (fg(2), attr(0)))
      player.add_award(adivinanzas.get_award())
      laboratorio_room.main_laboratorio(player)
    else: 
      print("Para la próxima será, no te desanimes")
  else:
    print(f'%s{adivinanzas.get_message_requirement()} %s' % (fg(1), attr(0)))
    laboratorio_room.main_laboratorio(player)