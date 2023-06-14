
class ManejaHelado:
  def __init__(self):
    self.__listaHelados= []
  
  def registraHelado(self, helado):
    self.__listaHelados.append(helado)

 
    
                
#C.    Definir una clase ManejaHelados que registre y gestione a través de una lista los helados vendidos.  
  def getlistaHelados(self):
    return self.__listaHelados

  def __str__ (self):
    return "LISTA : {}".format(self.__listaHelados)
    
          
      

      
    