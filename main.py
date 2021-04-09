from Player import Player
import re
from blessed import Terminal
import os
import main_game
import datetime

def win_screen(player):
  print("""
  ███████ ███████ ██      ██  ██████ ██ ██████   █████  ██████  ███████ ███████ 
  ██      ██      ██      ██ ██      ██ ██   ██ ██   ██ ██   ██ ██      ██      
  █████   █████   ██      ██ ██      ██ ██   ██ ███████ ██   ██ █████   ███████ 
  ██      ██      ██      ██ ██      ██ ██   ██ ██   ██ ██   ██ ██           ██ 
  ██      ███████ ███████ ██  ██████ ██ ██████  ██   ██ ██████  ███████ ███████ 
  
  """)
  print("Has evitado una catastrofe en la unimet.")
  print(f"""
  Tus estadísticas {player.get_username()}:
  Tiempo: {datetime.timedelta(seconds=(player.get_time() - player.get_time_left().total_seconds()))}
  Vidas restantes: {player.get_lives()}
  Pistas restantes: {player.get_clues_count()}
  Dificultad: {player.get_difficulty()}
  """)


def lose_screen(player):
  print("""
  ██▓███  ▓█████  ██▀███  ▓█████▄  ██▓  ██████ ▄▄▄█████▓▓█████ 
  ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▓██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ 
  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   
  ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ 
  ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓ ░██░▒██████▒▒  ▒██▒ ░ ░▒████▒
  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░
  ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒  ▒ ░░ ░▒  ░ ░    ░     ░ ░  ░
  ░░          ░     ░░   ░  ░ ░  ░  ▒ ░░  ░  ░    ░         ░   
              ░  ░   ░        ░     ░        ░              ░  ░
                             ░                                     
  """)
  if not (player.get_time_left() > datetime.timedelta()):
    print("Se te acabó el tiempo")
  elif not (player.get_lives() > 0):
    print("Te quedaste sin vidas")


def set_statistics(player):
  complete_time = player.get_time() - player.get_time_left().total_seconds()
  with open("records.txt","a") as records:
    records.write(player.get_username() + ",")
    records.write(str(complete_time) + ",")
    records.write(player.get_difficulty() + "\n")

def show_statistics():
  """Muestra las estadísticas de los usuarios que hayan jugado

  Args:
      [dic]: dic, diccionario con la información de usuarios registrados

  Returns:
      [Objeto clase "Player"]: Objeto en donde está toda la información del usuario durante la partida, ya instanciado.
  """
  statistics=[]
  try:
    with open("records.txt") as u:
      for line in u:
        aux={}
        aux["username"] = line.split(",")[0]
        aux["time"] = line.split(",")[1]
        aux["difficulty"] = line.split(",")[2].replace("\n","")
        statistics.append(aux)     
  except:
    pass
  if len(statistics)==0:
    print("Todavía no hay usuarios para mostrar estadisticas")
  else:
    print("TOP 5 Mejores tiempos: ")
    order_list =sorted(statistics, key = lambda i: float(i['time']))
    for i in range(5):
      try:
        print(f"""Pos.{i+1 } - {order_list[i]["username"]} TIEMPO: {order_list[i]["time"]} DIFICULTAD: {order_list[i]["difficulty"]}""")
      except:
        break
  

def get_instructions():
  """Muestra las instrucciones del juego.
  """ 
  print("""
El juego consiste en diferentes cuartos, donde hay objetos y cada objeto tiene un acertijo a resolver. 
Cada cuarto posee objetos, los cuales tienen consigo juegos asociados.
Cada vez que gana un juego obtiene una recompensa que le puede servir para resolver la problemática del juego. 
Para ganar hace falta completar todos los juegos.
  """)

def set_info_level():
  """Lee el archivo donde está la información de los niveles de dificultad y los coloca en un diccionario..

  Returns:
      [dic]: info_level, diccionario con toda la información de los niveles de dificultad.
  """ 
  
  info_level={}
  with open("lives_clues_time.txt","r") as info:
    for line in info:
      info_level[line.split(",")[0]] = {}
      info_level[line.split(",")[0]]["lives"]=float(line.split(",")[1])
      info_level[line.split(",")[0]]["clues"]=float(line.split(",")[2])
      info_level[line.split(",")[0]]["time"]=float(line.split(",")[3].replace("\n",""))

  return info_level
      

def difficulty_level(player):
  """Coloca la dificultad, seteando en la clase Player las vidas, pistas y tiempo que tendrá para completar el juego.

  Args:
      [Objeto clase "Player"]: Objeto en donde está toda la información del usuario durante la partida
  """
  info_level=set_info_level()
  while True:
    try:
      level=input(f"""Ingrese el nivel de dificultad en la que desea jugar:
      (1) Fácil: {int(info_level["easy"]["lives"])} vidas y {int(info_level["easy"]["clues"])} pistas
      (2) Medio: {int(info_level["medium"]["lives"])} vidas y {int(info_level["medium"]["clues"])} pistas
      (3) Difícil: {int(info_level["hard"]["lives"])} vidas y {int(info_level["hard"]["clues"])} pistas
      ==> """)
      if level=="1":
        level="easy"
      elif level=="2":
        level="medium"
      elif level=="3":
        level="hard"
      else:
        raise Exception
      break
    except:
      print("Seleccione una opción correcta.")

  player.set_lives(info_level[level]["lives"])
  player.set_clues_count(info_level[level]["clues"])
  player.set_time((info_level[level]["time"]*60))
  player.set_difficulty(level)


def validate_user(users):
  """Valida el usuario y contraseña de un usuario ya registrado.

  Args:
      [dic]: dic, diccionario con la información de usuarios registrados

  Returns:
      [Objeto clase "Player"]: Objeto en donde está toda la información del usuario durante la partida, ya instanciado.
  """ 
  while True:
    try:
      username = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contraseña: ")
      if username in users.keys():
        if users[username]["password"]==password:
          break
        else:
          raise Exception
      else:
        raise Exception
    except:
      print("Usuario o contraseña incorrectas")
      
  print("Usted ha sido loggeado correctamente.")

  return Player(username, users[username]["password"], users[username]["age"], users[username]["avatar"]) 

def avatar_selection():
  """Ofrece los avatares disponibles para que el usuario escoja uno.

  Returns:
      [str]: avatar, el avatar escogido por el usuario.
  """ 
  avatars=["Scharifker","Eugenio Mendoza","Pelusa","Gandhi"]
  while True:
    try:
      avatar=input("""Selecciona tu ávatar: 
      (1) Scharifker
      (2) Eugenio Mendoza
      (3) Pelusa                      
      (4) Gandhi 
      ==> """)
      avatar=avatars[int(avatar)-1]
      break
    except:
      print("El ávatar seleccionado no existe.")
  return avatar

def validate_not_repeat(users,username):
  """Valida que el nombre de usuario no esté ya registrado

  Args:
      [dic]: dic, diccionario con la información de usuarios registrados
      [str]: username, nombre de usuario propuesto por el usuario

  Returns:
      [Bool]: True, si el username no está registrado, False, si lo está.
  """ 
  if username in users:
    return False
  else:
    return True

def validate_username(username):
  """Valida que el nombre de usuario cumple con los requisitos los cuales son: contenga unicamente letras, numeros, puntos y guión bajo.

  Args:
      [str]: username, nombre de usuario propuesto por el usuario

  Returns:
      [Bool]: True, si el username es valida, False si no.
  """ 
  flag = 0
  while True:  
    if (len(username)<6):
      flag = -1
      break
    elif not re.match('^[a-z0-9._]*$', username):
      flag = -1
      break
    else:
      return True
  if flag ==-1:
    return False
    
def validate_password(password):
  """Valida que la contraseña cumple con los requisitos los cuales son: tenga por lo menos 6 caracteres, no contenga ',' y contenga letras y números.

  Args:
      [str]: password, contraseña propuesta por el usuario

  Returns:
      [Bool]: True, si la contraseña es valida, False si no.
  """ 
  flag = 0
  while True:  
    if (len(password)<6):
      flag = -1
      break
    elif not re.search("[a-z]", password):
      flag = -1
      break
    elif not re.search("[0-9]", password):
      flag = -1
      break
    if "," in password:
      flag = -1
      break
    elif re.search("\s", password):
        flag = -1
        break
    else:
      flag = 0
      return True
  if flag ==-1:
    return False

def register(users):
  """Registra a nuevos usuarios, validando que no estén ya registrados.

  Args:
      [dic]: users, con los usuarios ya registrados

  Returns:
      [Objeto clase "Player"]: Objeto en donde está toda la información del usuario durante la partida, aquí ya está instanciado.
  """ 
  while True:
    try:
      username=input("Ingrese su nombre de usuario: ")
      if not validate_not_repeat(users, username):
        raise NameError
      if not validate_username(username):
        raise Exception
      password=input("Ingrese su contraseña: ")
      if not validate_password(password):
        raise Exception
      re_password=input("Repita nuevamente su contraseña: ")
      if not (password == re_password):
        raise Exception
      break
    except NameError:
      print("Nombre de usuario ya registrado")
    except:
      print("Usuario o contraseña no permitido\nVerique que su nombre de usuario contenga unicamente letras, numeros, puntos y guión bajo.\nVerifique que su contraseña tenga por lo menos 6 caracteres, no contenga ',' y contenga letras y números. ")

  while True:
    try:
      age = int(input("Ingrese su edad: "))
      if not (age > 0):
        raise Exception
      break
    except:
      print("Dato no válido.")

  avatar=avatar_selection()

  with open("users.txt","a") as users:
    users.write(username + ",")
    users.write(password + ",")
    users.write(str(age) + ",")
    users.write(avatar + "\n") 

  return Player(username,password, age, avatar)
      
def menu(users):
  """Muestra las principales opciones para iniciar el juego, ver las intrucciones y ver records de quienes ya hayan jugado.

  Args:
      [dic]: users, con los usuarios ya registrados

  Returns:
      [Objeto clase "Player"]: Objeto en donde está toda la información del usuario durante la partida.
  """  
  while True:
    while True:
      try:
        option=input("""    ---Menú---
(1) Comenzar nueva partida
(2) Ver las instrucciones
(3) Ver records
==> """)
        if not (option=="1" or option=="2" or option=="3"):
          raise Exception
        break
      except:
        print("Escoja una opción correcta.")

    if option=="1":
      while True:
        try:
          option=input("""\n---¿Qué desea hacer?---
(1) Crear nuevo usuario
(2) Continuar con usuario ya creado
==> """)
          if not (option=="1" or option=="2"):
            raise Exception
          break
        except:
          print("Escoja una opcion correcta")

      if option=="1":
        player=register(users)
      elif option=="2":
        player=validate_user(users)
      difficulty_level(player)
      return player
    elif option=="2":
      get_instructions()
    elif option=="3":
      show_statistics()


def intro():
  """Imprime la bienvenida del juego
  """
  term = Terminal()
  print(f"{term.home}{term.clear}")
  print("Presione 'q' para empezar")
  with term.cbreak():
    val = ''
    while val.lower() != "q":
      val = term.inkey(timeout=2)
  os.system("clear")
  print("""
██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  
██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██    
██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██    
██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██     
██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████    

                                 █████  
                                ██   ██ 
                                ███████ 
                                ██   ██ 
                                ██   ██  

███████╗███████╗ ██████╗ █████╗ ██████╗  █████╗ ███╗   ███╗███████╗████████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔════╝╚══██╔══╝
█████╗  ███████╗██║     ███████║██████╔╝███████║██╔████╔██║█████╗     ██║   
██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝     ██║   
███████╗███████║╚██████╗██║  ██║██║     ██║  ██║██║ ╚═╝ ██║███████╗   ██║   
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   
""")

def set_users():
  """Coloca todos los users que ya están registrados en el archivo de texto en un diccionario.
  Returns:
      [dict]: users, con todos los usuarios registrados.
  """
  users={}
  try:
    with open("users.txt") as u:
      for line in u:
        users[line.split(",")[0]] = {}
        users[line.split(",")[0]]["password"]=line.split(",")[1]
        users[line.split(",")[0]]["age"]=line.split(",")[2]
        users[line.split(",")[0]]["avatar"]=line.split(",")[3].replace("\n","")
  except:
    pass
  return users

def main():
  """Función principal de todo el programa.
  """
  users=set_users()
  intro()
  player = menu(users)
  if main_game.main_game(player):
    os.system("clear")
    set_statistics(player)
    win_screen(player)
  else:
    os.system("clear")
    lose_screen(player)
  
if __name__ == "__main__":
  main()