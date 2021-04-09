from Normal_Game_R import Normal_Game_R
import random
import datetime
from colored import fg, bg, attr
import rooms.laboratorio_room as laboratorio_room


def get_clue(player, info_question, n_clue):
  clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
  if clue == "S":
    if n_clue<=1 and player.get_clues_count() > 0:
      print(info_question[f"clue_{n_clue}"])
      player.set_clues_count(player.get_clues_count() - 1)
      return n_clue +1
    else:
      print("No te quedan pistas")
      return n_clue
  else:
    return n_clue

def preguntas_python_game(preguntas_python,player):
  """Función donde se ejecuta las mecánicas del juego.El juego se ayuda de la función eval que es donde se convierte el string a codigo para que lo lea python

  Args:
      [Objeto clase Normal_Game_R]: preguntas_python, juego normal con requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """

  print(preguntas_python.get_name().capitalize())
  print(preguntas_python.get_rules().capitalize())
  question_n=1
  info_question=preguntas_python.send_question(question_n)
  print(info_question["question"])
  n_clue=1
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    while True:
      try:
        input_guess=input("==> ") #aquí el usuario pone su respuesta
        guess = eval(input_guess) # eval() convierte el string en codigo y lo ejecuta
        break
      except:
        print("Incorrecto. Pierdes media vida")
        player.set_lives(player.get_lives() - 0.5)
        n_clue = get_clue(player, info_question, n_clue)
    if question_n==0:
      if len(str(input_guess)) > 2:
        if guess == 50: #aquí veo si el codigo que se ejecutó es la respuesta 
          return True
        else:
          print("Incorrecto. Pierdes media vida")
          player.set_lives(player.get_lives() - 0.5)
          n_clue=get_clue(player, info_question, n_clue)
    else:
      if guess == "sistemas de ingenieria metro la en estudio":
        return True
      else:
        print("Incorrecto")
        player.set_lives(player.get_lives() - 0.5)
        n_clue = get_clue(player, info_question, n_clue)
  
  
def main_preguntas_python(compu_1,player):
  info_game=compu_1.get_info_game()
  preguntas_python = Normal_Game_R(info_game["name"], info_game["rules"], info_game["award"], info_game["message_requirement"], info_game["requirement"], info_game["questions"])
  
  if preguntas_python.get_requirement() in player.get_inventory():
    if preguntas_python_game(preguntas_python,player):
      print(f'%sFelicidades, ahora como recompenza obtienes una {preguntas_python.get_award()} %s' % (fg(2), attr(0)))
      player.add_award(preguntas_python.get_award())
      laboratorio_room.main_laboratorio(player)
    else: 
      print("Para la próxima será, no te desanimes")
  else:
    print(f'%s{preguntas_python.get_message_requirement()} %s' % (fg(1), attr(0)))
    laboratorio_room.main_laboratorio(player)