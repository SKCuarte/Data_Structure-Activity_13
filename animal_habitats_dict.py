#1. Create a dictionary of 8 animals and their natural habitats.
dict = {
"Koala": "Forest",
"Monkey": "Jungle",
"Cow": "Farm",
"Shark": "Ocean",
"Elephant": "Savannah",
"Penguin": "Arctic",
"Dog": "House",
"Camel": "Dessert"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the habitat of the 3rd animal.
print("The habitat of the 3rd animal is: ", dict["Cow"])

#4. Update the habitat of the 5th animal.
dict["Elephant"] = "Zoo"
print(dict)

#5. Delete the 7th animal from the dictionary.
del dict["Dog"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)
