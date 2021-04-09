from Game import Game

class Normal_Game_R(Game): #Clase hija de Game, aquí se guardan los juegos que piden requisitos
  def __init__(self, name, rules, award, message_requirement, requirement,questions):
    Game.__init__(self, name, rules, award)
    self.__message_requirement = message_requirement
    self.__requirement = requirement
    self.__questions = questions
  
  def get_message_requirement(self):
    return self.__message_requirement

  def get_requirement(self):
    return self.__requirement

  def send_question(self,number):
    return self.__questions[number]
