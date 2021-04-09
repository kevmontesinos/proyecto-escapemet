import time
import datetime
class Player(): #Clase donde se guarda toda la información del usuario
  def __init__(self,username, password, age, avatar):
    self.username = username
    self.__password = password
    self.__age = age
    self.avatar = avatar
    self.difficulty = None
    self.lives = 5
    self.time = None
    self.time_future = None 
    self.clues_count = None
    self.__inventory = []  
  
  def get_username(self):
    return self.username
  
  def get_avatar(self):
    return self.avatar

  def set_difficulty(self,diff):
    self.difficulty = diff
  def get_difficulty(self):
    return self.difficulty

  def get_lives(self):
    return self.lives
  def set_lives(self, new_lives):
    self.lives = new_lives

  def get_bar_health(self):
    print(f"❤️  Vidas: {self.lives} ")
    print(f"🔑  Pistas: {self.clues_count} ")

  def get_clues_count(self):
    return self.clues_count
  def set_clues_count(self, new_clues_count):
    self.clues_count = new_clues_count

  def get_time(self):
    return self.time
  def set_time(self, new_time):
    self.time = new_time

  def get_inventory(self):
    return self. __inventory
  def show_inventory(self):
    if len(self.__inventory) > 0:
      print("Inventario: ")
      for i in range(len(self.__inventory)):
        print(f"{i+1}.{self.__inventory[i]}")
    else:
      print("Usted todavía no posee recompensas")
  def add_award(self, new_award):
    if new_award not in self.__inventory:
      self.__inventory.append(new_award)
    else:
      print("Sin embargo, ya tenías la recompenza en tu inventario.")
  
  def set_time_future(self, new_time):
    self.time_future = new_time
  
  def get_time_left(self):
    return datetime.timedelta(seconds=round(self.time_future-time.time()))