def numeroCubo():
	num = int ( input("Ingrese el numero")) 
	cantNum = 0
	while num != 0:
		numeroCubo = num * num * num
		print("El numero ", num, "elevado al cubo es ", numeroCubo)
		cantNum = cantNum + 1
		num = int(input("Ingrese un nuevo numero: (si el numero es '0' el programa termina) "))

	print("La cantidad de numeros elevados al cubo fueron: ", cantNum)

def porcentaje():
	num_1 = int(input("Ingresa el precio \n"))
	num_2 = int(input("Ingresa el precio 2 \n"))

	if num_1 < num_2:
		valor_ingresado = num_1 - num_2
		porcentaje = valor_ingresado * 100 / num_2
		print( "El precio es mayor por un %", porcentaje)
	else:
		valor_ingresado = num_2 - num_1
		porcentaje = valor_ingresado * 100 / num_1
		print("El precio 2 es mayor por un %",porcentaje)

def decision():
	eleccion = input("Desea elevar al cubo (a)\nDesea sacar un porcentaje (b)\n")
	if eleccion == 'a':
		numeroCubo()
	elif eleccion == 'b':
		porcentaje()

	else:
		print("Adios")

decision() 