#1. Create a dictionary of 6 technologies and their inventors.
dict = {
"Electricity": "Benjamin Franklin",
"Watch": "Peter Henlein",
"Radio": "Guglielmo Marconi",
"Thermometer": "Gabriel Farenheit",
"Electric Bulb": "Thomas Edison",
"Calculator": "Blaise Pascal"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the inventor of the 4th technology.
print("The inventor of the 4th technology is: ", dict["Thermometer"])

#4. Update the inventor of the 2nd technology.
dict["Watch"] = "Kyan Cuarte"
print(dict)

#5. Delete the 6th technology from the dictionary.
del dict["Calculator"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)