from Final_Game import  Final_Game
import random
import rooms.biblioteca_room as biblioteca_room
import datetime
import os

def ppt_game(final_game,player):
  """Función donde se ejecuta las mecánicas del juego. Un simple piedra papel o tijeras :(

  Args:
      [Objeto clase Final_Game]: final_game, juego normal sin requisitos donde está toda la información del juego.
      [Player]: información del juegador
  Returns:
      [Bool]: True, si se gana el juego, False, si no.
  """
  os.system("clear")
  print(final_game.get_name())
  print(final_game.get_rules())
  while player.get_time_left() > datetime.timedelta() and player.get_lives() > 0:
    while True:
      try:
        user_election = input("\nIngresa una opción (piedra ✊ , papel 🖐  o tijeras ✌️  ): ").lower()
        if not (user_election == "piedra" or user_election == "papel" or user_election == "tijeras"):
          raise Exception
        break
      except:
        print("No válido.")
    posible_elections = ["piedra", "papel", "tijeras"]
    computer_election = random.choice(posible_elections)
    print(f"Escogiste {user_election} y tu rival: {computer_election}.\n")

    if user_election == computer_election:
        print(f"Ambos escogieron {user_election}. Empate.")
    elif user_election == "piedra":
        if computer_election == "tijeras":
          return True
        else:
            print("Papel tapa piedra. Perdiste una vida.")
    elif user_election == "papel":
        if computer_election == "piedra":
          return True    
        else:
            print("Tijera corta papel. Perdiste una vida.")
    elif user_election == "tijeras":
        if computer_election == "papel":
          return True
        else:
            print("Piedra rompe tijeras. Perdiste una vida.")

def main_final_game(puerta,player):
  info_game=puerta.get_info_game()
  final_game= Final_Game("Piedra, papel o tijeras", "Pierdes media vida por partida perdida", info_game["award"], info_game["requirement"], info_game ["message_requirement"])
  if final_game.get_requirement()[0] in player.get_inventory() and final_game.get_requirement()[1] in player.get_inventory():
    if ppt_game(final_game,player):
      player.add_award(final_game.get_award())
  else:
    print(final_game.get_message_requirement() + " y también, el Disco Duro")