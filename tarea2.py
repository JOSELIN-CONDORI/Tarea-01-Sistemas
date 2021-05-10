def pagoSemanalBase40horas():
  #definir variables y otros
     sueldoPagarSemanal=0.0
  #Datos de entrada
     horasTrabajadas=int(input("Ingrese horas trabajadas a la semana:"))
     horasPago=int(input("Ingrese el pago por hora:")) 
  #Proceso 
      if: 
      horasTrabajadas>40:sueldoPagarSemanal=40*horasPago+(horasTrabajadas-40)*2*horasPago
     else:
    sueldoPagarSemanal=horasTrabajadas*horasPago
  #Datos de salida
     print("El sueldo a pagar al trabajador es:", sueldoPagarSemanal)

 pagoSemanalBase40horas() 