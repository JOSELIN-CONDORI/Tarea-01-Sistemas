def estacionamiento1():
  #definir variable y otros
  estacionamiento=0
  #datos de entrada
  cantidadx=int(input("cuanto tiempo se quedara:"))
  #Proceso
  if cantidadx<=2:
     estacionamiento=5*cantidadx
  if cantidadx<=5:
     estacionamiento=(-4*(2-cantidadx))+10
  if cantidadx<=10:
     estacionamiento=(3*(cantidadx-5))+22
  if cantidadx>=11:
     estacionamiento=(2*(cantidadx-10))+37
  #Datos de Salida
  print("pagara en total:",estacionamiento)
estacionamiento1()