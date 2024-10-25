#1. Create a dictionary of 8 plants and their types (e.g., shrub, tree, herb).
dict = {
"Wheat": "Herbs",
"Rose": "Shrubs",
"Mango": "Trees",
"Beans": "Climbers",
"Watermelon": "Creepers",
"Horsetails": "Ferns",
"Water Lilies": "Aquatic",
"Funaria": "Moss",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the type of the 5th plant.
print("The type of the 5th plant is: ", dict["Watermelon"])

#4. Update the type of the 2nd plant.
dict["Rose"] = "Flowers"
print(dict)

#5. Delete the 6th plant from the dictionary.
del dict["Horsetails"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)