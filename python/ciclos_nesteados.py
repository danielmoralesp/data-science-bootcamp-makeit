project_teams = [
    ["Andrea", "Juan", "Pedro"],
    ["Julio", "Daniel", "Danilo"],
    ["Bernardo", "Juan", "Oscar"]
]

for team in project_teams:
    for student in team:
        print(student)


sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    for sale in location:
        scoops_sold += sale
    print(scoops_sold)
