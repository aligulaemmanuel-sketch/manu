keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Combine using zip()
res_dict = dict(zip(keys, values))
print(res_dict)

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name.capitalize()} pays ${price}")
    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["GAP", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 1. Change number_stores to 2
brand["number_stores"] = 2

# 2. Print sentence about Zara's clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'][:-1])} and {brand['type_of_clothes'][-1]}.")

# 3. Add country_creation with Spain
brand["country_creation"] = "Spain"

# 4. Check for international_competitors and add Desigual
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 5. Delete creation_date
brand.pop("creation_date")

# 6. Print last international competitor
print(f"Last competitor: {brand['international_competitors'][-1]}")

# 7. Print major colors in the US
print(f"US major colors: {brand['major_color']['US']}")

# 8. Print number of keys
print(f"Number of keys: {len(brand)}")

# 9. Print all keys
print(f"Keys: {list(brand.keys())}")

# Bonus: Merge with more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(f"Updated number_stores: {brand['number_stores']}")

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Map characters to indices: {"Mickey": 0, "Minnie": 1, ...}
disney_users_A = {user: i for i, user in enumerate(users)}
print(disney_users_A)

# 2. Map indices to characters: {0: "Mickey", 1: "Minnie", ...}
disney_users_B = {i: user for i, user in enumerate(users)}
print(disney_users_B)

# 3. Alphabetically sorted: {"Ariel": 0, "Donald": 1, ...}
disney_users_C = {user: i for i, user in enumerate(sorted(users))}
print(disney_users_C)