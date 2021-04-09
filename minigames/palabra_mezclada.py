from Normal_Game_NR import Normal_Game_NR
import random
from terminaltables import SingleTable
from colored import fg, bg, attr
import rooms.server_room as server_room
import datetime


def palabras_mezcladas_game(palabras_mezcladas,player):
  """Función donde se ejecuta las mecánicas del juego. Toma las palabras, las coloca en una tabla con ayuda de terminaltables, con la función random.shuffle se desordena el string y lo convierte en una lista y luego con el join esa lista la vuelvo a convertir en string.

  Args:
      [Objeto clase Normal_Game_NR]: ahorcado, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego, False, si no.
  """
  print(palabras_mezcladas.get_name().capitalize())
  print(palabras_mezcladas.get_rules().capitalize())
  question_n=random.randint(0,2)
  info_question=palabras_mezcladas.send_question(question_n)

  words=info_question["words"]
  words_mix=[[f"""Categoría: {info_question["category"]}"""]]
  words_mix_aux=[]

  for i in range(len(words)):
    word=words[i]
    char_list = list(word)
    random.shuffle(char_list)
    word_mix = ''.join(char_list)
    words_mix_aux.append(word_mix)
    word_mix_list=[f"""%s{word_mix}%s""" % (fg(1), attr(0))]
    words_mix.append(word_mix_list)

  guessed_count=0

  while guessed_count<5 and player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    table = SingleTable(words_mix)
    print(table.table)
    guess=input(f"""{info_question["question"]}\n==> """)
    if guess in words:
      print ('%s ¡Correcto! %s' % (fg(2), attr(0)))
      index = words.index(guess)
      words_mix[index+1]=[f"""%s{words_mix_aux[index]}%s""" % (fg(2), attr(0))]
      guessed_count+=1
    else:
      print (f'%s {guess} no está en las palabras :/ %s' % (fg(1), attr(0)))
      print("Pierdes media vida")
      player.set_lives(player.get_lives() - 0.5)
      
  print(table.table)
  if guessed_count==5:
    return True

def main_palabra_mezclada(rack,player):
  info_game=rack.get_info_game()
  palabra_mezcladas = Normal_Game_NR(info_game["name"], info_game["rules"], info_game["award"], info_game["questions"])

  if palabras_mezcladas_game(palabra_mezcladas,player):
    print(f'%sFelicidades, ahora como recompenza obtienes una {palabra_mezcladas.get_award()} %s' % (fg(2), attr(0)))
    player.add_award(palabra_mezcladas.get_award())
    server_room.main_server_room(player)
  else: 
    print("Para la próxima será, no te desanimes")