# Sort by key's name inside dictionaries
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

# def f(person):
    # return person["name"]

# people.sort(key=f)
people.sort(key=lambda person: person["name"])

print(people)