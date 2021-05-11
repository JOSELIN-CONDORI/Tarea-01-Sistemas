def articulodescuento():
  #Definir variables y otros
  print("¿Cual es el costo de su articulo?")
  enunciadox=0
  #Datos de entrada
  cantidady=int(input("Ingrese el costo para hacerle su descuento :"))
  #Proceso
  if cantidady>=200:
   enunciadox=cantidady-(cantidady*15/100)
  if cantidady<=199:
   enunciadox=cantidady-(cantidady*12/100)
  if cantidady<=99:
   enunciadox=cantidady-(cantidady*10/100)
  #Datos de salida
  print("Usted debera pagar el monto de:", enunciadox)

articulodescuento()