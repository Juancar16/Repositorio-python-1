import sys
import os

# En este ejercicio se realizara una calculadora sencilla que tendra las siguinetes funciones:
# Suma - Resta - Multiplicación - Division - División entera - Residuo - Área del circulo, cuadrado y triangulo

print ("CALCULADORA SENCILLA")
print ("-----------------------------------")


def opcion():
	print ("Digite la operación que desea hacer")
	print ("1. Suma \n 2. Resta \n 3. Multiplicar \n 4. Dividir \n 5. División entera \n 6. Residuo \n 7. Exponenciar \n 8. Áreas \n 0. Salir")
	accion = int(input ("Digíte el número de la opción: "))
	return accion
#--------------------------------------------------------
def suma ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 + num2
	print ("El resultado es ", resultado)
	
def resta ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 - num2
	print ("El resultado es ", resultado)

def multiplicación ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 * num2
	print ("El resultado es ", resultado)
	

def division ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 / num2
	print ("El resultado es ", resultado)


def division_entera ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 // num2
	print ("El resultado es ", resultado)


def residuo ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 % num2
	print ("El resultado es ", resultado)


def exponenciar ():
	num1 = int(input("Digíte el número 1: "))
	num2 = int(input("Digíte el número 2: "))	
	resultado = num1 ** num2
	print ("El resultado es ", resultado)


def areas ():
	opcion_areas = int(input("Digite el número del área que desea hallar: \n1. Triangulo. \n 2. Cuadrado"))
	if opcion_areas == 1:
		base = int(input("Digite la base: "))
		altura = int(input("Digite la altura: "))
		resultado = (base*altura)/2
		print ("El área dek triangulo es: ", resultado)

def salir ():
	num1 = int(input("Segur@ que desea salir?\n 0. Si  1. No "))
	if num1 == 0:
		print ("FIN DEL fPROGRAMA")
	if num1 == 1:
		opcion()
opcion()




#--------------------------------------------------------

def direccion (accion):
	if accion == 1:	
		suma()	
	if accion == 2:	
		resta()	
	if accion == 3:	
		multiplicacion()
	if accion == 4:	
		division()	
	if accion == 5:	
		division_entera()	
	if accion == 6:	
		residuo()	
	if accion == 7:	
		exponenciar()	
	if accion == 8:	
		areas()	
	if accion == 0:	
		salir()	
	accion = 0	 

opcion()
direccion(accion())



