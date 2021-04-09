class Object():
  def __init__(self,name):
    self.name = name
    self.__position = "position"
    self.__info_game = {}

  def show_name(self):
    return self.name
  def set_position(self,position):
    self.__position=position
  
  def set_game(self,game):
    self.__info_game = game
  def get_info_game(self):
    return self.__info_game
  
  def show_game(self):
    print(self.__info_game)