first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []

age.append(42)

all_ages = age + [32, 41, 29]


name_and_age = zip(first_names, all_ages)
print(list(name_and_age))

ids = range(4)
print(list(ids))
