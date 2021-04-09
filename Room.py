class Room():
  def __init__(self, name):
    self.name = name
    self.__design = ""
    self.__objects = []
    self.__info_objects = []
  
  def get_name(self):
    return self.name

  def set_design(self,design):
    self.__design = design
  def get_design(self):
    return self.__design
  def print_design(self):
    print(self.__design)

  def add_object(self,new_object):
    self.__objects.append(new_object)
  def show_objects(self):
    for i in range(len(self.__objects)):
      print(f"{i+1}. {self.__objects[i].show_name()}")
  
  def set_info_objects(self, info):
    self.__info_objects = info
  def get_info_objects(self):
    return self.__info_objects