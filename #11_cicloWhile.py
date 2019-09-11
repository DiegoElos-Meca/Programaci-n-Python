# ESTRUCTURAS DE CONTROL INTERACTIVAS (ciclo while)

respuesta = 'si'
numero = 0
while respuesta == 'si':
	numero = int (input('teclee un numero\n'))
	if numero > 0:
		print ('el numero es pocitivo\n')
	elif numero < 0:
		print ('el numero es negativo\n')
	else:
		print('el numero es igual a cero\n')
	respuesta = input('¿Quieres ingresar otro numero? <si - no>\n')