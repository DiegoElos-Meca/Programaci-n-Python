def numeroCubo():
	num = int(input('ingrese el numero: '))
	cantNum = 0
	while (num != 0):
		numCubo = num*num*num
		print('el numero ', num, 'elevado al cuboo es ', numeroCubo)
		cantNum = cantNum + 1
		num = int ( input ('ingrese un nuevo numero: (si el numero es "0" el programa terminara) '))

	print( 'la cantidad de numeros elevados al cubo fueron:', cantNum)

def procentaje():
	num_1 = int (input('ingresa el precio '))
	num_2 = int(input('ingresa el precio 2'))

	if num_1 < num_2:
		valor_ingresado = num_1 - num_2
		procentaje = valor_ingresado * 100/num_2
		print(' el precio es mayor por un %', procentaje)
	else:
		valor_ingresado = num_2 - num_1
		procentaje = valor_ingresado * 100 / num_1
		print(' el precio 2 es mayor por un %',procentaje)

def decision():
	eleccion = input ('desea elevar al cubo (a)\n desea sacar porcentaje (b)')
	if eleccion.lower() == 'a':
		numeroCubo()
	elif eleccion.lower() == 'b' :
		procentaje()
	else:
		print ( 'adios')
decision()
