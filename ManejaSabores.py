from claseSabor import Sabores
import csv
class ManejaSabor:
  def __init__(self):
    self.__listaSabores= []
   #Definir una clase ManejaSabores que permita manejar los n sabores que la heladería presenta a la venta.
  def cargaSabores (self):
    archivo= open('sabores.csv')
    reader= csv.reader(archivo, delimiter=',')
    for fila in reader:
      idSabor= int(fila[0])
      ingredientes= fila[1]
      nombreSabor= fila[2]
      unSabor= Sabores(idSabor,ingredientes,nombreSabor)
      self.__listaSabores.append(unSabor)
  
  def getlistasabores(self):
    return self.__listaSabores
  
  def obtenerSabor(self, numSabor):
    i=0
    while i < len(self.__listaSabores):
      if numSabor==self.__listaSabores[i].getid():
        return self.__listaSabores[i]
      i+=1
  
        
        
                  
  
    