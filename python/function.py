def saludar_usuario(nombre_tienda, item_especial = "guarapo"):
    print("Bienvenido a " + nombre_tienda)
    print("Nuestro cafe especial es " + str(item_especial))
    print("Disfruta tu compra!")



 ####
 ####

saludar_usuario("My Coffee", "Capucchino")

# def mult(number, x, y):
#     resultado = (number * x) + y
#     print(resultado)
#
# mult(1, 3, 1)

def dividido_por_cuatro(numero_ingresado):
    return numero_ingresado/4

resultado = dividido_por_cuatro(16)


print("16 dividido por 4 es " + str(resultado) + "!")

resultado2 = dividido_por_cuatro(resultado)

print(str(resultado) + " dividido por 4 es " + str(resultado2) + "!")

### Retornar multiples variables

def square_point(x_value, y_value):
    x_2 = x_value * x_value
    y_2 = y_value * y_value
    return x_2, y_2

x_al_cuadrado, y_al_cuadrado = square_point(1, 3)
print(x_al_cuadrado)
print(y_al_cuadrado)

### Scope de las variables
encabezado = "Nuestro string especial es "

def crear_un_string_especial(string_especial):
    encabezado = "String dentro del metodo/funcion"
    return encabezado + string_especial + "."

print(encabezado)
print(crear_un_string_especial("grapas"))
