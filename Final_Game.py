from Game import Game

class Final_Game(Game): #Clase hija de Game, aquí se guarda el juego final
  def __init__(self, name, rules, award, requirement, message_requirement):
    Game.__init__(self, name, rules, award)
    self.__requirement = requirement
    self.__message_requirement = message_requirement
  
  def get_message_requirement(self):
    return self.__message_requirement

  def get_requirement(self):
    return self.__requirement