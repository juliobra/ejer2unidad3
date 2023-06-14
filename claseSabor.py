
class Sabores:
  __idSabor: int
  __igredientes: str
  __nombreSabor: str
  
  def __init__(self,idSabor, ingredientes, nombreSabor):
    self.__idSabor= idSabor
    self.__ingredientes= ingredientes
    self.__nombreSabor= nombreSabor
  def getid(self):
    return self.__idSabor

  def getingredientes(self):
    return self.__ingredientes

  def getnombresabor(self):
    return self.__nombreSabor

  def __str__(self):
    return "id: {}, ingredientes: {}, nombresabor: {}".format(self.__idSabor, self.__ingredientes, self.__nombreSabor)

    