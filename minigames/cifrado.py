from Normal_Game_R import Normal_Game_R
import random
from terminaltables import SingleTable
from colored import fg, bg, attr
import datetime

import rooms.biblioteca_room as biblioteca_room

def cifrador(text,x,letters):
  """
  Función donde se cifra el mensaje
      [string] result, el mensaje cifrado.
  """
  result=""
  for i in range(len(text)):
    if text[i]!=" ":
      aux=(letters.index(text[i]) + x) % 27
      result+=letters[aux]
    else:
      result+=" "
  return result

def show_abecedario(x,letters):
  """
  Función que muestra el abecedario normal y también con el cifrado
  """
  cript_abc=[]
  for i in range(len(letters)):
    aux=(letters.index(letters[i]) + x) % 27
    cript_abc.append(letters[aux])
  
  table_data=[cript_abc,letters]

  table = SingleTable(table_data)
  table.inner_row_border = True
  print(table.table)

  
def cifrado_game(cifrado,player):
  """
  Función donde se ejecuta las mecánicas del juego

  Args:
      [Objeto clase Normal_Game_R]: cifrado, juego normal requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego
  """
  print(cifrado.get_name().capitalize())
  print(cifrado.get_rules().capitalize())
  info_question=cifrado.send_question(random.randint(0,2))
  text=info_question["question"].replace("S","s").replace("á","a")
  x=info_question["desplazamiento"]
  letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    show_abecedario(x,letters)
    guess=input(f"Descifre el siguiente mensaje: {cifrador(text,x,letters)}\n==> ").lower()
    if guess==text:
      return True
    else:
      print("La palabra descifrada no es la correcta. Pierdes una vida.")
      player.set_lives(player.get_lives() - 1)


def main_cifrado(mueble_gabetas,player):
  """Función principal del juego, mediante atributo del objeto mueble_gabetas se instancia el juego de la clase Normal_Game_R (Juego con requisitos)

  Args:
      [Objeto clase Object]: mueble_gabetas
      [Player]: información del juegador
  """
  info_game=mueble_gabetas.get_info_game()
  cifrado = Normal_Game_R(info_game["name"], info_game["rules"], info_game["award"], info_game["message_requirement"], info_game["requirement"], info_game["questions"])
  
  if cifrado.get_requirement() in player.get_inventory():
    if cifrado_game(cifrado,player):
      print (f'%sFelicidades, ahora como recompenza obtienes un {cifrado.get_award()} %s' % (fg(2), attr(0)))
      player.add_award(cifrado.get_award().replace(": Si estas gradudado puedes pisar el Samán",""))
      biblioteca_room.main_biblioteca(player)
    else: 
      print("Para la próxima será, no te desanimes")
  else:
    print (f'%s{cifrado.get_message_requirement()} %s' % (fg(1), attr(0)))
    biblioteca_room.main_biblioteca(player)
