razas_de_perros = ['bulldog', 'dalmata', 'pitbull', 'collie']

# print(razas_de_perros[0])
# print(razas_de_perros[1])
# print(razas_de_perros[2])
# print(razas_de_perros[3])

# for <variable temporal> in <variable de la lista>:
#     <action>

for i in razas_de_perros:
    print(i)

for dog in razas_de_perros:
    print(dog)

for i in range(3):
    print("Warning")

# for numbers in mis_numeros_favoritos:
#     mis_numeros_favoritos.append(1)

# print(mis_numeros_favoritos)

print("Checkeando las razas")

for item in razas_de_perros:
    print(item)
    if item == "dalmata":
        print("Encontre el dalamata")
        break

print("Busqueda finalizada")

mis_numeros_favoritos = [2, 4, 8, -1, 15, -5, 20, 35, -7]

for i in mis_numeros_favoritos:
    if i < 0:
        continue
    print(i)
