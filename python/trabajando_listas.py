my_list = [1, 2, 3, 4, 5]
print(len(my_list))

example = ['red', 'green', 'blue', 'orange']
print(len(example))

for color in range(len(example)):
    print(example[color])

print(example[2])
print(example[3])
print(example[-1])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#### letters[start:end]
sublist = letters[1:6]
print(sublist)

primeros_tres = letters[:3]
print(primeros_tres)

fruits = ['apple', 'banana', 'cherry', 'orange']
print(fruits[-2:])
print(fruits[:-2])

repeated = ["a", "b", "i", "z", "i", "a", "i"]
num_i = repeated.count('i')
print(num_i)

repeated.sort()
print(repeated)
