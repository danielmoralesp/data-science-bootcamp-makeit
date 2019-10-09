## 1
def average(num1, num2):
    avg = (num1 + num2) / 2
    return avg

print(average(1, -1))


## 2
def tenth_power(num):
    tenth = num ** 10
    return tenth

print(tenth_power(2))


## 3
def introduction(first_name, last_name):
    str = last_name + ", " + first_name + " " + last_name
    return str

print(introduction("Daniel", "Morales"))

## 4
def square_root(num):
    sqr = num ** 0.5
    return sqr

print(square_root(100))

## 5
def tip(total, percentage):
    tip_amount = (total * percentage) / 100
    return tip_amount

print(tip(10, 25))

## 6
def win_percentage(wins, losses):
    total_games = wins + losses
    ratio_ganancias = wins/total_games
    total = ratio_ganancias * 100
    return total

print(win_percentage(0, 10))

## 7
def first_three_multiples(num):
    print(num)
    print(num*2)
    print(num*3)
    ultimo = num * 3
    return ultimo

print(first_three_multiples(7))

## 8
def dog_years(name, age):
    dyear = age * 7
    cadena = name + " tu tienes " + str(dyear) + " años en años de perro."
    return cadena

print(dog_years("Lola", 16))
