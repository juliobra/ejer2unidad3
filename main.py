from claseHelado import Helado
from ManejaSabores import ManejaSabor
from ManejaHelados import ManejaHelado

def test():
  manejaSabores= ManejaSabor()
  manejaSabores.cargaSabores()
  manejaHelado= ManejaHelado()
  while True:
    print("1. Registrar un helado vendido")
    print("2. Mostrar los 5 sabores de helado más pedidos")
    print("3. Estimar el total de gramos vendidos de un sabor")
    print("4. Mostrar los sabores vendidos en un tipo de helado")
    print("5. Calcular el importe total recaudado por tipo de helado")
    print("0. Salir")

    op = int(input("Ingrese una opción: "))
    if op==0:
      break

    if op==1:
      print ("ingrese el peso del helado")
      peso=float(input(""))
      print ("ingrese el precio del helado")
      precio=float(input(""))
      
      helado= Helado(peso,precio)
      
      cantSabores= int(input("ingrese la cantidad de sabores"))
      for _ in range(cantSabores):
        numSabor= int(input("ingrese el id del sabor"))
        sabor = manejaSabores.obtenerSabor(numSabor)
        if sabor is not None:
                helado.agregarSabor(sabor)
                
        else:
                print("Número de sabor inválido")

      manejaHelado.registraHelado(helado)
      if op == 1 and helado is not None:  # Verificar si helado tiene un valor asignado
        print(helado)
    


    if op == 2:
     sabores_vendidos = {}
     for helado in manejaHelado.getlistaHelados():
        for sabor in helado.getsabores():
            if sabor.getnombresabor() in sabores_vendidos:
                sabores_vendidos[sabor.getnombresabor()] += 1
            else:
                sabores_vendidos[sabor.getnombresabor()] = 1
    
     sabores_top = sorted(sabores_vendidos, key=sabores_vendidos.get, reverse=True)[:5]
    
     print("Los 5 sabores de helado más pedidos son:")
     for sabor in sabores_top:
        print(sabor)
  
    if op==3:
      Sab= int(input("ingrese el numero del sabor"))
      for sabor in helado.getsabores():
        if sabor.getid()== Sab:
          
      
  
  

if __name__=='__main__':
  test()