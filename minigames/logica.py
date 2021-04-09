from Normal_Game_R import Normal_Game_R
import random
from colored import fg, bg, attr
import rooms.plaza_rectorado_room as plaza_rectorado_room
import os
import datetime


def logica_game(logica,player):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Objeto clase Normal_Game_NR]: logica, juego normal con requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(logica.get_name().capitalize())
  print(logica.get_rules().capitalize())
  question_n=random.randint(0,1)
  info_question=logica.send_question(question_n)
  info_question=info_question.replace("+","  +  ").replace("=","  = ").replace("x","  x  ").replace("-","  -  ").replace("\n ","\n")
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    if question_n==0:
      correct_answer="67"
      print(info_question)
      answer=input("Ingrese su respuesta: ")
      if correct_answer == answer:
        return True
      else:
        os.system("clear")
        print("No es correcto. Pierdes una vida")
        player.set_lives(player.get_lives() - 1)
    else:
      correct_answer="41"
      print(info_question)
      answer=input("Ingrese su respuesta: ")
      if correct_answer == answer:
        return True
      else:
        os.system("clear")
        print("No es correcto. Pierdes una vida")
        player.set_lives(player.get_lives() - 1)
  
def main_logica(saman,player):
  """Función principal del juego, mediante atributo del objeto saman se instancia el juego de la clase Game

  Args:
      [Objeto clase Object]: saman
      [Player]: información del juegador
  """
  info_game=saman.get_info_game()
  logica = Normal_Game_R(info_game["name"], info_game["rules"], info_game["award"], info_game["message_requirement"], info_game["requirement"], info_game["questions"])

  if (logica.get_requirement()[0] in player.get_inventory()) and (logica.get_requirement()[1] in player.get_inventory()):
    if logica_game(logica,player):
      print(f'%sFelicidades, ahora como recompenza obtienes una {logica.get_award()} %s' % (fg(2), attr(0)))
      player.add_award(logica.get_award()) 
      plaza_rectorado_room.main_plaza_rectorado(player) 
    else:
      print("Para la próxima será, no te desanimes")
  else:
    print(f'%s{logica.get_message_requirement()} %s' % (fg(1), attr(0)))
    player.set_lives(player.get_lives() - 1 )
    plaza_rectorado_room.main_plaza_rectorado(player) 