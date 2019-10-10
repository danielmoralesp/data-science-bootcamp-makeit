alturas = [1.9, 1.70, 1.6, 1.7]
nombres = ['Jenny', 'Alexis', 'Sam', 'Grace']

nombres_y_alturas = zip(alturas, nombres)
# print(nombres_y_alturas)

print(list(nombres_y_alturas))


valores_mixtos = ['Jenny', 61]

alturas2 = [
    ['Jenny', 61],
    ['Alex', 70],
    ['Sam', 67],
    ['Grace', 78]
]

tricky = [
    ['X', 'O', 'X'],
    ['0', ' ', 'X'],
    ['X', 'O', 'O']
]

for row in tricky:
    for column in row:
        print(column + " ", end='')
    print()

## Listas vacias
lista_vacia = []
print(lista_vacia)
lista_vacia.append(1)
print(lista_vacia)

lista_con_valores = [1, 2, 3]
lista_con_valores.append(5)
print(lista_con_valores)

otra_lista = [10, 11, 12]
nueva_lista = lista_con_valores + otra_lista
print(nueva_lista)

mi_rango = range(20)
print(mi_rango)
print(list(mi_rango))

mi_lista = range(2, 9)
print(list(mi_lista))

mi_lista2 = range(2, 9, 2)
print(list(mi_lista2))
