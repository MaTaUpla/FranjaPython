# Tarea 1
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

###Inicio Codigo###

#Tarea parte 1

#inicializo los pesos dados por el ejercicio.
Peso_Payaso = 112
Peso_Muñeca = 75
#se leen las cantidades de payaso y muñecas, se guardan en variables auxiliares.
Cantidad_Payaso = input("Ingrese cantidad de Payasos comprados: ")
Cantidad_Muñeca = input("Ingrese cantidad de Muñecas comprados: ")
#se realiza una validacion de si las cantidades ingresadas son mayor a 0

if(int(Cantidad_Payaso) == 0 and int(Cantidad_Muñeca) == 0):
  print("No tuvo ninguna venta de payasos ni muñecas")
elif(int(Cantidad_Payaso) > 0 and int(Cantidad_Muñeca) >= 0 or int(Cantidad_Payaso) >= 0 and int(Cantidad_Muñeca) > 0):
  totalPeso = ((int(Cantidad_Payaso) * Peso_Payaso) + (int(Cantidad_Muñeca) * Peso_Muñeca))
  totalPeso = str(totalPeso)
  print("se vendieron " + Cantidad_Payaso + " payaso(s) y " + Cantidad_Muñeca + " muñeca(s), con un total de " + totalPeso + " gramos en el paquete")
#si se ingresa un numero menor a 0 o algun caracter arroja el error
else:
  print("ingrese numero de ventas en positivo.")
  
###Fin Codigo###

# Tarea 2
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

###Inicio Codigo###

#Tarea parte 2

#se inician las variables auxialires, se tranforma a floar para permitir/conservar los datos decimales
Peso = float(input("Ingrese su peso en Kilogramos: "))
Altura = float(input("Ingrese su estatura en Metros: "))

#se valida que los datos sean positivos
if(Peso <= 0):
  print("Ingrese un peso adecuado")
elif(Altura <= 0):
  print("Ingrese una altura adecuada")
else:
  #se hace la ecuacion del IMC, se utiliza la funcion POW para hacer la potencia cuadrada de estatura, ademas del round para redondear los decimales.
  IMC = (Peso / pow(Altura,2))
  IMC = round(IMC, 2)
  #se escribe el mensaje deseado ademas se transforma a string para poder concatenar el resultado.
  print("Tu índice de masa corporal es " + str(IMC))
  
###Fin Codigo###
