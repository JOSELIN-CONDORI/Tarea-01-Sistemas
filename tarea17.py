def paquetesJDQC():
  #Definir Variables
  resultPaqueteDmp=""
  #Datos de entrada
  montoRvDiDmpc=float(input("Ingrese el monto que recibe en diciembre:"))
  #Proceso
  if montoRvDiDmpc>=50000:
    resultPaqueteDmp="Paquete A"
  elif montoRvDiDmpc>=20000 and resultPaqueteDmp<50000:
    resultPaqueteDmp="Paquete B"
  elif montoRvDiDmpc>=10000 and montoRvDiDmpc<20000:
    resultPaqueteDmp="Paquete C"
  else:
    resultPaqueteDmp="Paquete D"
  #Datos de salida
  print("La persona comprara el: ", resultPaqueteDmp)

paquetesJDQC()