class Game():
  def __init__(self, name, rules, award):
    self.__name = name  
    self.__rules = rules
    self.__award = award

  def get_name(self):
    return self.__name 
  def get_rules(self):
    return self.__rules
  def get_award(self):
    return self.__award