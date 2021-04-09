from Normal_Game_NR import Normal_Game_NR
import random
from terminaltables import SingleTable
from colored import fg, bg, attr
import rooms.server_room as server_room
import datetime

def get_clue(player, answer, correct_answer):
  """Función que te da las pistas, si te quedan. Después de ejecutarse el algoritmo te dice si estás cerca o no.

  Args:
      [Player]: información del juegador
      [int]: answer, la respuesta del usuario
      [int] correct_answer, la respuesta correcta eligida al azar
  """
  clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
  if clue == "S":
    if player.get_clues_count() > 0:
      if answer < correct_answer:
        if (correct_answer - answer) <= 3:
          print("Estás cerca, estás un poco bajo")
        else:
          print("Estás muy abajo")
      else:
        if (answer - correct_answer) <= 3:
          print("Estás cerca, estás un poco arriba")
        else:
          print("Estás muy arriba")
    else:
      print("No tienes pistas ya")
    player.set_clues_count(player.get_clues_count() - 1)

def numero_entre_game(numero_entre,player):
  """Función donde se ejecuta las mecánicas del juego. Se escoje un numero random con random y el usuario debe adivinar.

  Args:
      [Objeto clase Normal_Game_NR]: ahorcado, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(numero_entre.get_name().title())
  print(numero_entre.get_rules().capitalize())
  info_question=numero_entre.send_question(0)

  correct_answer=random.randint(1,15)
  failed_in_a_row = 0
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    answer=int(input(f"""{info_question["question"]}\n==> """))
    if answer < correct_answer or answer > correct_answer:
      print (f'%s "{answer}" no es el número :/ %s' % (fg(1), attr(0)))
      get_clue(player, answer, correct_answer)
      failed_in_a_row += 1
    else:
      print ('%s ¡Correcto! %s' % (fg(2), attr(0)))
      return True
    if failed_in_a_row==3:
      print("Por perder tres consecutivas, pierdes un cuarto de vida.")
      player.set_lives(player.get_lives() - 0.25)
      failed_in_a_row = 0

def main_numero_entre(papelera,player):
  info_game=papelera.get_info_game()
  numero_entre = Normal_Game_NR(info_game["name"], info_game["rules"] , info_game["award"],info_game["questions"])
  if numero_entre_game(numero_entre,player):
    print(f"Felicidades, ahora como recompenza obtienes {numero_entre.get_award()}")
    player.add_award(numero_entre.get_award().replace("tí","Ti"))
    server_room.main_server_room(player)
  else: 
    print("Para la próxima será, no te desanimes")