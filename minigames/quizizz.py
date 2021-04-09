from Normal_Game_NR import Normal_Game_NR
import random
from terminaltables import SingleTable
from colored import fg, bg, attr
import rooms.plaza_rectorado_room as plaza_rectorado_room
import datetime

def get_clue(player, info_question, n_clue):
  """Función que te da las pistas, si te quedan.
  Args:
      [Player]: información del juegador
      [dic]: info_question, información donde se encuentran las pistas
      [int] n_clue, las pistas que se han usado en el juego
  Returns:
      [int]: n_clue + 1 si  el jugador consume la pista, n_clue si no.
  """
  clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
  if clue == "S":
    if n_clue<=1 and player.get_clues_count() > 0:
      print(info_question[f"clue_{n_clue}"])
      player.set_clues_count(player.get_clues_count() - 1)
      print(f"Pistas restantes: {player.get_clues_count()}")
      return n_clue+1
    else:
      print("No te quedan pistas")
  return n_clue
    

def show_question(info_question):
  print(info_question["question"])
  answers=[
  [f"""(1) {info_question["correct_answer"]}""",f"""(2) {info_question["answer_2"]}"""],
  [f"""(3) {info_question["answer_3"]}""",f"""(4) {info_question["answer_4"]}"""]
  ]
  table = SingleTable(answers)
  table.inner_row_border = True
  print(table.table)


def quizizz_game(quizizz,player):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Objeto clase Normal_Game_NR]: quizizz, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego, False, si no.
  """
  print(quizizz.get_name().capitalize())
  print(quizizz.get_rules().capitalize())
  info_question=quizizz.send_question(random.randint(0,2))
  show_question(info_question)
  answers_1=[info_question["correct_answer"],info_question["answer_2"],info_question["answer_3"],info_question["answer_4"]]
  n_clue=1
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    selected_option=input("Ingrese la opción correcta: ")
    if selected_option.isnumeric():
      selected_option=int(selected_option)
      if selected_option >= 1 and selected_option <= 4:
        if answers_1[selected_option-1] == info_question["correct_answer"]:
          return True
        else:
          print("Opción incorrecta :(")
          player.set_lives(player.get_lives() - 0.5)
          print(f"Pierdes media vida\nVidas restantes: {player.get_lives()}")
          n_clue=get_clue(player, info_question, n_clue)
      else:
        print("Opción no válida, por favor, ingresa una opción del 1 al 4.")
    else:
      print("Por favor, ingresa un número como opción.")
  
def main_quizizz(banco_1,player):
  """Función principal del juego, mediante atributo del objeto banco_1 se instancia el juego de la clase Game

  Args:
      [Objeto clase Object]: banco_1
      [Player]: información del juegador
  """
  info_game=banco_1.get_info_game()
  quizizz = Normal_Game_NR(info_game["name"], info_game["rules"] , info_game["award"],info_game["questions"])
  if quizizz_game(quizizz,player):
    print (f'%sFelicidades, ahora como recompenza obtienes una {quizizz.get_award()} %s' % (fg(2), attr(0)))
    player.add_award(quizizz.get_award())
    plaza_rectorado_room.main_plaza_rectorado(player)
  else: 
    print("Para la próxima será, no te desanimes")

