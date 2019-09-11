# SWITCH no existe como tal en Python, pero podemos usar listas
argumento = int(input('dime un mes\n'))

switcher = {
    1: "Enero",
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
}
print(switcher.get(argumento, 'mes invalido'))