from Normal_Game_R import Normal_Game_R
import random
from sympy import *
import math
from sympy.parsing.sympy_parser import parse_expr
from colored import fg, bg, attr
import datetime

import rooms.biblioteca_room as biblioteca_room

def calculation(question_n, info_question):
  """Función donde se transforma el string en una expresión parse con parse_expr, luego de tenerla de esta manera se puede sacar la derivada con la libreria sympy con diff, posteriormente con expr.evalf() se evalúa la funcion donde se quiera, posteriormente se transforma la float el número.

  Args:
      [int]: numero de pregunta
      [dic]: info_question, información donde se encuentran las preguntas
  Returns:
      [float]: result, resultado de la derivada
  """
  if question_n==0 or question_n==1:
    ec=info_question["question"].split("f(x)=")[1].replace("sen","sin")
    ec_filt=parse_expr(ec)
    x, y, z = symbols('x y z') #declara x,y,z como variables
    expr=diff(ec_filt, x) #calcula la derivada en funcion de x, en ec_filt va la funcion que quieras evaluar
    result=(expr.evalf(subs={x: math.pi})) #evalua la derivada en pi
  else:
    ec=info_question["question"].split("f(x)=")[1].replace("sen","sin")
    ec_filt=parse_expr(ec)
    x, y, z = symbols('x y z')
    expr=diff(ec_filt, x)
    result=(expr.evalf(subs={x: math.pi/3}))
  result=eval(str(result))
  return result

def get_clue(player, info_question, n_clue):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Player]: información del juegador
      [dic]: info_question, información donde se encuentran las pistas
      [int] n_clue, las pistas que se han usado en el juego
  Returns:
      [int]: n_clue + 1 si  el jugador consume la pista, n_clue si no.
  """
  clue = input("¿Desea gastar una pista? (S/N)\n=>> ").upper()
  if clue == "S":
    if n_clue<=1 and player.get_clues_count() > 0:
      print(info_question[f"clue_{n_clue}"].capitalize())
      player.set_clues_count(player.get_clues_count() - 1)
      return n_clue+1
    else:
      print("No te quedan pistas")  
  return n_clue

def preguntas_mate_game(preguntas_matematica, player):
  """Función donde se ejecuta las mecánicas del juego

  Args:
      [Objeto clase Normal_Game_R]: preguntas_matematica, juego normal requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego.
  """
  print(preguntas_matematica.get_name())
  question_n=random.randint(0,2)
  info_question=preguntas_matematica.send_question(question_n)
  result=calculation(question_n,info_question)
  n_clue=1

  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    while True:
      try:
        guess=float(input(f"""{info_question["question"]}\n==> """))
        break
      except:
        print("Incorreto. Pierdes un cuarto de vida")
        player.set_lives(player.get_lives() - 0.25)
        n_clue=get_clue(player, info_question, n_clue)
    if guess == result:
      return True
    else:
      print("Incorrecto. Pierdes un cuarto de vida")
      player.set_lives(player.get_lives() - 0.25)
      n_clue=get_clue(player, info_question, n_clue)


  
def main_preguntas_mate(mueble_sentarse, player):
  """Función principal del juego, mediante atributo del objeto mueble_sentarse se instancia el juego de la clase Normal_Game_R (Juego con requisitos)

  Args:
      [Objeto clase Object]: mueble_sentarse
      [Player]: información del juegador
  """

  info_game=mueble_sentarse.get_info_game()
  preguntas_mate = Normal_Game_R(info_game["name"], info_game["rules"], info_game["award"], info_game["message_requirement"], info_game["requirement"], info_game["questions"])
  
  if preguntas_mate.get_requirement() in player.get_inventory():
    if preguntas_mate_game(preguntas_mate,player) :
      print (f'%sFelicidades, ahora como recompenza obtienes una {preguntas_mate.get_award()} %s' % (fg(2), attr(0)))
      player.set_lives(player.get_lives()+1)
      biblioteca_room.main_biblioteca(player)
    else: 
      print("Para la próxima será, no te desanimes")
  else:
    print (f'%s{preguntas_mate.get_message_requirement()} %s' % (fg(1), attr(0)))
    biblioteca_room.main_biblioteca(player)


