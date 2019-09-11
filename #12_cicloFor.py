# ESTRUCTURAS DE CONTROL INTERATIVAS (bucle for)
# Mostrar cada item de la lista

MI_LISTA = ["Diego ", "Manuel ", "Elos ", "Gonzalez "]
n = 0
for miList in MI_LISTA:
	print(MI_LISTA[n])
	n = n + 1

#Uso de la funcion range()
for valor in range(1,11):
	print (valor)

#Crear una lista con la funcion range() y list()
numeros = list(range(1,11))
print(numeros)

#imprimir los numers pares de una lista
pares = list(range(1,11,3))
print(pares)

#Mostrar el cuadrado de los numeros de una lista
cuadrados = []
for valor in range(1,11):
	cuadrados.append(valor**2)
print(cuadrados)

# uso de las funciones min(), max(), sum(), 
milista = [1,2,3,4,5,0,6,7,8,9]
print(min(milista))
print(max(milista))
print(sum(milista))

#listas por comprension
cuadrados = [valor**2 for valor in range(1,11)]
print(cuadrados)