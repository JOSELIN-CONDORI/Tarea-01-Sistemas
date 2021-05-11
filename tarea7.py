def becasmensuales():
  #Definir variables y otros
  print("becas")
  becasmensuales=0
  #Datos de entrada
  añosX=int(input("Ingrese su edad :"))
  promedio=float(input("Ingrese su promedio:"))
  #Proceso
  if añosX>18:
      becasmensuales="2500"
  if promedio<10:
      becasmensuales="2000"
  if promedio<9:
      becasmensuales="1000"
  if promedio<7.5:
      becasmensuales="500"
  if promedio<6:
      becasmensuales="Estudia mas el proximo ciclo escolar."
  if promedio<10:
      becasmensuales="3000"
  if promedio<9:
      becasmensuales="2000"
  if promedio<8:
      becasmensuales="100"
  if promedio<6:
      becasmensuales="Le invito a estudiar mas el proximo ciclo escolar."
  #Datos de salida
  print("La beca de usted es :", becasmensuales)

becasmensuales()