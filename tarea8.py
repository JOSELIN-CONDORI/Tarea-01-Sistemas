def tarea8():
  #Defenir Variables
  bonoSueldo, bonoantiguedad, bonoMayor=0.0,0.0,0.0
  #Datos de entrada
  anhoAntiguadad=int(input("Ingrese Anho Antiguadad:"))
  salario=float(input("Ingrese el salario actual:"))
  #Proceso
  if anhoAntiguadad>2 and anhoAntiguadad<5:
    bonoantiguedad=salario*0.20
  elif anhoAntiguadad>=5:
    bonoantiguedad=salario*0.30
  if salario<1000:
    bonoSueldo=salario*0.25
  elif salario>=1000 and salario<=3500:
    bonoSueldo=salario*0.15
  else:
    bonoSueldo=salario*0.10
  if bonoantiguedad>bonoSueldo:
    bonoMayor=bonoantiguedad
  elif bonoSueldo>bonoantiguedad:
    bonoMayor=bonoSueldo
  #Datos de Salida
  print("El bono mayor es:", bonoMayor)
  
tarea8()