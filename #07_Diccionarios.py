# Diccionarios (matrices asociativas)


# Asignacion de una clave, dos puntos y el valor de dicha clave
mi_Diccionario = {
#	key    ->  value
	'clave_1': 'valor_1', 
	'clave_2': 2, 
	'clave_3': 3.33

	}  
print(mi_Diccionario)

print(mi_Diccionario['clave_2'])

mi_Diccionario['clave_3'] = 'NUEVO VALOR'  # Modificando el valor de la 'clave tres'.
print (mi_Diccionario['clave_3'])

del(mi_Diccionario['clave_1'])  # Eliminar la entrada que pertenece a 'clave_1' 
print (mi_Diccionario)

m