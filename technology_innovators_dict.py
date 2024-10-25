#1. Create a dictionary of 8 technologies and their innovators.
dict = {
"Light Bulbs": "Thomas Edison",
"Apple": "Steve Jobs",
"AC EDS": "Nikola Tesla",
"Microsoft": "Bill Gates",
"Electricity": "Benjamin Franklin",
"Paintings": "Leonardo Da Vinci",
"Telephone": "Alexander Graham Bell",
"Airplanes": "The Wright brothers",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the innovator of the 4th technology.
print("The innovator of the 4th technology is: ", dict["Microsoft"])

#4. Update the innovator of the 2nd technology.
dict["Apple"] = "S. Jobs"
print(dict)

#5. Delete the 6th technology from the dictionary.
del dict["Paintings"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)