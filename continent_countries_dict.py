#1. Create a dictionary of 6 continents and a list of 3 countries for each.
dict = {
"Asia": "Japan, Korean, and China",
"Europe": "Germany, Belgium, and France",
"Africa": "Algeria, Congo, and Sudan",
"North America": "Canada, Mexico, and Barbados",
"South America": "Argentina, Bolivia, and Chile",
"Australia": "Australia, New Zealand, and Papua New Guinea"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the countries of the 4th continent.
print("The countries of the 4th continent are: ", dict["North America"])

#4. Update the countries of the 5th continent.
dict["South America"] = "Colombia, Ecuador, and Mexico"
print(dict)

#5. Delete the 6th continent from the dictionary.
del dict["Australia"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)


