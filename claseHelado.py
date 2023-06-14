from claseSabor import Sabores
class Helado:
  __gramos: int
  __precio: int
  __sabor: list
  def __init__(self, gramos, precio):
    self.__gramos= gramos
    self.__precio= precio
    self.__sabor= []

  @classmethod
  def getgramos(cls):
    return cls.__gramos

  @classmethod
  def getprecio(cls):
    return cls.__precio

  def getsabores(self):
    return self.__sabor

  def agregarSabor(self,sabor):
    self.__sabor.append(sabor)

  def __str__(self):
    listaSabor= ",".join(str(sabores) for sabores in self.__sabor)
    return "Helado - Peso: {}, Precio: {}, Sabores: {}".format(self.__gramos, self.__precio, listaSabor)
    
    
  