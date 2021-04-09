from Normal_Game_NR import Normal_Game_NR
import random
import os
import datetime
from terminaltables import SingleTable
from colored import fg, bg, attr
import rooms.laboratorio_room as laboratorio_room

def set_words(table_data,palabras):
  """Algoritmo donde se colocan las letras en la sopa de letras aleatoriamente.

  Args:
      [list]: table_data, matriz vacía
      [list]: palabras
  Returns:
      [Bool]: True, si se gana el juego, False, si no.
  """
  w=0
  while w<=2:
    palabra=palabras[w]
    combinacion=random.randint(1,3)
    i=0
    if combinacion==1: #horizontal
      combinacion=random.randint(1,2)
      if combinacion==1: #de arriba hacia abajo
        a=random.randint(0,14)
        b=random.randint(0,15-len(palabra))
        while i<len(palabra):
          table_data[a][b]=palabra[i]
          b+=1
          i+=1
      elif combinacion==2: #de abajo hacia arriba
        a=random.randint(0,14)
        b=random.randint(len(palabra),14)
        while i<len(palabra):
          table_data[a][b]=palabra[i]
          b-=1
          i+=1    
    elif combinacion==2: #vertical
      combinacion== random.randint(1,2)
      if combinacion==1: #derecha a izquierda
        a=random.randint(0,14)
        b=random.randint(0,15-len(palabra))
        while i<len(palabra):
          table_data[b][a]=palabra[i]
          b+=1
          i+=1
      elif combinacion==2: #izquierda a derecha
        a=random.randint(0,14)
        b=random.randint(len(palabra),14)
        while i<len(palabra):
          table_data[b][a]=palabra[i]
          b-=1
          i+=1
    elif combinacion==3: #diagonal
      combinacion=random.randint(1,2)
      if combinacion==1:
        a=random.randint(0,15-len(palabra))
        b=random.randint(0,15-len(palabra))
        while i<len(palabra):
          table_data[a][b]=palabra[i]
          b+=1
          a+=1
          i+=1
      elif combinacion==2:
        a=random.randint(len(palabra),14)
        b=random.randint(len(palabra),14)
        while i<len(palabra):
          table_data[a][b]=palabra[i]
          b-=1
          a-=1
          i+=1

    w+=1

  return table_data
  
def verification_words(table_data,palabras):
  """"
  Verifica que no se hayan cruzado palabras

  Args:
    [list]: table_data
    [list]: palabras
  Returns 
    [Bool]: True si no hay palabras cruzada, False si no
  """
  count=0
  for i in range(15):
    for j in range(15):
      if table_data[i][j]!="":
        count+=1

  if count==len(palabras[0])+len(palabras[1])+len(palabras[2]):
    return True
  else:
    return False

def get_clue(player, info_question, n_clue, av_clues):
  """Función que te da las pistas, si te quedan.

  Args:
      [Player]: información del juegador
      [dic]: info_question, información donde se encuentran las pistas
      [int] n_clue, las pistas que se han usado en el juego
      [int] av_clues, las pistas disponibles.
  Returns:
      [int]: n_clue + 1 si  el jugador consume la pista, n_clue si no.
  """
  clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
  if clue == "S":
    if n_clue<=av_clues and player.get_clues_count() > 0:
      print(info_question[f"clue_{n_clue}"])
      player.set_clues_count(player.get_clues_count() - 1)
      return n_clue+1
    else:
      print("No te quedan pistas")
  return n_clue

def sopa_game(sopa_letras,player):
  """Función donde se ejecuta las mecánicas del juego. Primero se crea una matriz 15*15 y se coloca en una lista las palabras que tienen que ser repartidas en el tablero, mediante la funcion set_words, a su vez se va verificando que las palabras no se crucen con la función verification_words hasta finalmente llegar a un loop donde tienes que ingresar las palabras que vayas encontrando.

  Args:
      [Objeto clase Normal_Game_NR]: sopa_letras, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(sopa_letras.get_name().replace("_"," de ").title())
  print(sopa_letras.get_rules().capitalize())
  question_n=random.randint(0,2)
  info_question=sopa_letras.send_question(question_n)
  table_data = [
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ["","","","","","","","","","","","","","",""],
  ]
  palabras = [info_question["answer_1"].lower(),info_question["answer_2"].lower(),info_question["answer_3"].lower()]

  letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  while verification_words(table_data,palabras)==False:
    table_data= [
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ["","","","","","","","","","","","","","",""],
    ]
    set_words(table_data,palabras) 
  
  for i in range(15):
    for j in range(15):
      if table_data[i][j]=="":
        n=random.randint(0,25)
        table_data[i][j]=letters[n]
      
  table = SingleTable(table_data)
  table.inner_row_border = True
  words_guessed = []
  n_clue=1
  av_clues=3
  while len(words_guessed) < 3 and player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    print(table.table)
    guess=input("Ingrese la palabra encontrada: ").lower()
    if guess not in words_guessed:
      if guess in palabras:
        words_guessed.append(guess)
        os.system("clear")
        print(f"Bien {len(words_guessed)}/3")
      else:
        print("La palabra no está. Pierdes media vida")
        player.set_lives(player.get_lives()-0.5)
        n_clue = get_clue(player, info_question, n_clue, av_clues)
    else:
      print("Ya lo habías adivinado. ")
    if len(words_guessed)==3:
      return True
      
def main_sopa_letras(pizarra,player):
  info_game=pizarra.get_info_game()
  sopa_letras = Normal_Game_NR(info_game["name"], info_game["rules"] , info_game["award"],info_game["questions"])
  if sopa_game(sopa_letras,player):
    print(f'%sFelicidades, ahora como recompenza obtienes {sopa_letras.get_award()} %s' % (fg(2), attr(0)))
    player.set_lives(player.get_lives()+1)
    laboratorio_room.main_laboratorio(player)
  else: 
    print("Para la próxima será, no te desanimes")

  