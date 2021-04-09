from Normal_Game_NR import Normal_Game_NR
from terminaltables import SingleTable
import time
import os
from colored import fg, bg, attr
import rooms.plaza_rectorado_room as plaza_rectorado_room
import datetime

def clen_table():
  """ Te devuleve una tabla vacía (de forma auxiliar)
  Returns:
      [list] aux_table
  """
  aux_table = [
  ["  ","  ","  ","  "],
  ["  ","  ","  ","  "],
  ["  ","  ","  ","  "],
  ["  ","  ","  ","  "]]
  return aux_table

def get_clue(player, x, y, table_data):
  """Función que te da las pistas, si te quedan. El while loop busca una coincidencia del emoji escogido por el usuario y te imprime la posición en donde se encuentra la carta para que el usuario lo coloque.

  Args:
      [Player]: información del juegador
      [int]: x,y posición del emoji ingresado por el usuario 
      [list] table_data, donde están donde se encuentran cada emoji

  """
  if player.get_clues_count() > 0:
    clue = input("¿Desea gastar una pista? (S/N)\n==> ").upper()
    if clue == "S":
      for i in range(4):
        for j in range(4):
          if table_data[i][j] == table_data[y-1][x-1]:
            if i == y-1 and j == x-1:
              pass
            else:
              print(f"La pareja está en x={j+1} y={i+1}")
              player.set_clues_count(player.get_clues_count() - 1)
              print(f"Pistas restantes: {player.get_clues_count()}")
  else:
    print("No te quedan pistas")


def memoria_game(memoria,player):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Objeto clase Normal_Game_NR]: memoria, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(memoria.get_name().capitalize())
  print(memoria.get_rules().capitalize())
  table_data=[
  ['😀', '🙄', '🤮', '🥰'],
  ['🤮', '😨', '🤓', '😷'],
  ['😨', '🤓', '🥰', '😷'],
  ['🤑', '🤑', '🙄', '😀']]

  enumerate_table=[
  ["y\\x","1","2","3","4"],
  ["1",'😀', '🙄', '🤮', '🥰'],
  ["2",'🤮', '😨', '🤓', '😷'],
  ["3",'😨', '🤓', '🥰', '😷'],
  ["4",'🤑', '🤑', '🙄', '😀']]
  
  empty_table = [
  ["  ","  ","  ","  "],
  ["  ","  ","  ","  "],
  ["  ","  ","  ","  "],
  ["  ","  ","  ","  "]]

  table = SingleTable(enumerate_table)
  table.inner_row_border = True
  print(table.table)
  emoji_guessed=0
  print("¡Tienes 10 segundos para memorizar!\nTrata de memorizar las posicion x y y de determinado emoji.")
  n=0
  while n<10:
    time.sleep(1)
    n+=1
  os.system("clear")

  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    try:
      x=int(input("Seleccione la posición x del cuadro: "))
      y=int(input("Seleccione la posición y del cuadro: "))
      aux_table=clen_table()
      aux_table[y-1][x-1] = table_data[y-1][x-1]
      table_2=SingleTable(aux_table)
      table_2.inner_row_border = True
      print(table_2.table)
      get_clue(player, x, y, table_data)
      x2=int(input("Seleccione la posición x de la pareja: "))
      y2=int(input("Seleccione la posición y de la pareja: "))
      aux_table = clen_table()
      if x==x2 and y==y2:
        raise Exception 
      if table_data[y-1][x-1] == table_data[y2-1][x2-1]:
        if empty_table[y-1][x-1] == "  " and empty_table[y2-1][x2-1]=="  ":
          empty_table[y-1][x-1] = table_data[y-1][x-1]
          empty_table[y2-1][x2-1] = table_data[y2-1][x2-1]
          table_1=SingleTable(empty_table)
          table_1.inner_row_border = True
          os.system("clear")
          print("Vas por buen camino!")
          print(table_1.table)
          emoji_guessed+=1
          if emoji_guessed==8:
            break
        else:
          print("Ya lo habías adivinado!")
      else:
        aux_table[y-1][x-1] = table_data[y-1][x-1]
        aux_table[y2-1][x2-1] = table_data[y2-1][x2-1]
        table_2=SingleTable(aux_table)
        table_2.inner_row_border = True
        print("No era la pareja. Pierdes un cuarto de vida.")
        player.set_lives(player.get_lives() - 0.25)
        print(table_2.table)
        time.sleep(4)
        aux_table = clen_table()
        os.system("clear") 
        table_1=SingleTable(empty_table)
        table_1.inner_row_border = True
        print(table_1.table)

    except:
      print("Posición de la tabla no válido, valor no númerico ingresado o misma casilla escogida.")
  if emoji_guessed == 8:
    return True

def main_memoria(banco_2,player):
  """Función principal del juego, mediante atributo del objeto banco_2 se instancia el juego de la clase Normal_Game_NR (juego con requisitos)

  Args:
      [Objeto clase Object]: banco_2
      [Player]: información del juegador
  """
  info_game=banco_2.get_info_game()
  memoria = Normal_Game_NR(info_game["name"], info_game["rules"] , info_game["award"],info_game["questions"])
  if memoria_game(memoria,player):
    print (f'%sFelicidades, ahora como recompenza obtienes un {memoria.get_award()} %s' % (fg(2), attr(0)))
    player.add_award(memoria.get_award())
    plaza_rectorado_room.main_plaza_rectorado(player)
  else: 
    print("Para la próxima será, no te desanimes")

