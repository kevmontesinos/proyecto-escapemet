from Normal_Game_NR import Normal_Game_NR
import random
from colored import fg, bg, attr

import rooms.biblioteca_room as biblioteca_room
import os
import datetime

def show_ahorcado(tries):
  """Donde se guardan los dibujos
  
  Returns:
      [str]: stage, el dibujo
  """
  stages = [  
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]
  return stages[tries]
def get_clue(player, info_question, n_clue):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Player]: información del juegador
      [dic]: info_question, información donde se encuentran las pistas
      [int] n_clue, las pistas que se han usado en el juego
  Returns:
      [int]: n_clue + 1 si  el jugador consume la pista, n_clue si no.
  """
  clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
  if clue == "S":
    if n_clue<=3 and player.get_clues_count() > 0:
      print(info_question[f"clue_{n_clue}"])
      player.set_clues_count(player.get_clues_count() - 1)
      print(f"Pistas restantes: {player.get_clues_count()}")
      return n_clue+1
    else:
      print("No te quedan pistas")
  return n_clue

def ahorcado_game(ahorcado,player):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Objeto clase Normal_Game_NR]: ahorcado, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego, False, si no.
  """
  print(ahorcado.get_name().capitalize())
  print(ahorcado.get_rules().capitalize())
  question_n=random.randint(0,2)
  info_question=ahorcado.send_question(question_n)
  word = info_question["answer"].upper()
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  tries = 6
  n_clue = 1
  print(show_ahorcado(tries))
  print(word_completion)
  print("\n")
  while (not guessed) and tries > 0 and player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    print(f"Intentos restantes: {tries}")
    print(f"""> {info_question["question"]}""")
    guess = input("Ingrese una letra o palabra: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
          print(f"Ya habías intentado con la letra {guess}")
      elif guess not in word:
          print(f"{guess} no está en la palabra. Pierdes un cuarto de vida.")
          tries-=1
          player.set_lives(player.get_lives() - 0.25)
          guessed_letters.append(guess)
          n_clue=get_clue(player, info_question, n_clue)
      else:
          print("Bien, la letra está en la palabra")
          guessed_letters.append(guess)
          word_as_list = list(word_completion)
          indices = [i for i, letter in enumerate(word) if letter == guess]
          for index in indices:
              word_as_list[index] = guess
          word_completion = "".join(word_as_list)
          if "_" not in word_completion:
            guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess != word:
        print(f"{guess} no es la palabra. Pierdes un cuarto de vida.")
        tries-=1
        player.set_lives(player.get_lives() - 0.25)
        n_clue=get_clue(player, info_question, n_clue)
      else:
        guessed = True
        word_completion = word
    else:
      print("No es válido")
    print(show_ahorcado(tries))
    print(word_completion)
    print("\n")
  if guessed:
    return True
  elif guessed == False:
    print(f"Perdiste :( \n La palabra era {word}")
    return False

def main_ahorcado(mueble_libros,player):
  """Función principal del juego, mediante atributo del objeto mueble_libros se instancia el juego de la clase Game

  Args:
      [Objeto clase Object]: mueble_libros
      [Player]: información del juegador
  """
  os.system("clear")
  info_game=mueble_libros.get_info_game()
  ahorcado = Normal_Game_NR(info_game["name"], info_game["rules"] , info_game["award"],info_game["questions"])
  if ahorcado_game(ahorcado,player) :
    print (f'%sFelicidades, ahora como recompenza obtienes un {ahorcado.get_award()} %s' % (fg(2), attr(0)))
    player.add_award(ahorcado.get_award())
    biblioteca_room.main_biblioteca(player)
  else: 
    print("Para la próxima será, no te desanimes.")  
    biblioteca_room.main_biblioteca(player)