from typing import ItemsView


print("Hello World")

print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)

print((5 + 2) * 3 )
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / 2 - 4))
print(5 + (9 * 3 / (2 - 4)))

# list structure
counties = ["Arapahoe", "Denver", "Jefferson"]
# lists in Python are mutable (one object in a list can be replaced)

# empty lists can also be declared
newList = []
# or
NewList = list()

print(counties[1:])

counties.insert(2, "El Paso")
counties.remove("Arapahoe")
print(counties)
counties[2] = "Denver"
counties[1] = "Jefferson"
counties[0] = "El Paso"
counties.append("Arapahoe")
print(counties)
counties_dict = {}
#add county "Arapahoe" to the dictionary as the key and the # registered voters as the value
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
