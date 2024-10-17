population = {
    "China": 143,
    "Inida": 136,
    "USA": 32,
    "Pakistan": 21
}

def print_all():
    for country, n in population.items():
        print(f"{country}==>{n}")

def add_country():
    country = input("enter the name of new country: ")
    if country in population:
        print("country already exists")
    else:
        p = float(input("enter the population of the country: "))
    population[country] = 38
    print_all()

def remove():
    country = input("enter the name of country you want to delete: ")
    if country not in population:
        print("country doesnt exists")
    else:
        del population[country]
    print_all()

def query():
    country = input("enter the name of country you want to query: ")
    if country not in population:
        print("country doesnt exists")
    else:
        print(f"{country}==>{population[country]}")

print_all()
add_country()
remove()
query()