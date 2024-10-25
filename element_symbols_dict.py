#1. Create a dictionary of 10 elements and their chemical symbols.
dict = {
"Hydrogen": "H",
"Helium": "He",
"Lithium": "Li",
"Beryllium": "Be",
"Boron": "B",
"Carbon": "C",
"Nitrogen": "N",
"Oxygen": "O",
"Fluorine": "F",
"Neon": "Ne"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the symbol of the 6th element.
print("The symbol of the 6th element is: ", dict["Carbon"])

#4. Update the symbol of the 8th element.
dict["Oxygen"] = "Ox"
print(dict)

#5. Delete the 9th element from the dictionary.
del dict["Fluorine"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)


