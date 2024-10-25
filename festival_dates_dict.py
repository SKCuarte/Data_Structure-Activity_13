#1. Create a dictionary of 10 festivals and their celebration dates.
dict = {
"Zamboanga Hermosa Festival": "12 October",
"Fiesta Tsinoy": "January 26",
"Kuyamis Festival": "January 6-11",
"Diyandi Festival": "3rd Monday of January",
"Feast of the Black Nazarene": "January 9",
"Pasalamat Festival": "3rd Week of January",
"Sinulog Festival": "15 January or every second Sunday of January",
"Ati–Atihan Festival": "3rd Sunday of January",
"The Dinagyang Festival": "4th Sunday of January",
"Karanowan Fish-Tival": "February 15",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the date of the 3rd festival.
print("The date of the 3rd festival is: ", dict["Kuyamis Festival"])

#4. Update the date of the 7th festival.
dict["Sinulog Festival"] = "Jan 15"
print(dict)

#5. Delete the 5th festival from the dictionary.
del dict["Feast of the Black Nazarene"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)