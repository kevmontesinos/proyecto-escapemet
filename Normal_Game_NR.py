from Game import Game

class Normal_Game_NR(Game): #Clase hija de Game, aquí se guardan los juegos que no piden requisitos
  def __init__(self, name, rules, award, questions):
    Game.__init__(self, name, rules, award)
    self.__questions = questions
  
  def send_question(self,number):
    return self.__questions[number]