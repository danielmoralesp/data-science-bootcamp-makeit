my_info = ('Daniel', 'Medellin', 'Programmer', 4)
print(my_info)

print(my_info[0])
print(my_info[-1])

# my_info[0] = 'Danny'

## Unpacking tuple
nombre, ciudad, ocupacion, experience = my_info

print(my_info)

## One element tuple
one_element_tuple = (4,)
print(type(one_element_tuple))

lista = [1, 2, 3]
print(tuple(lista))
