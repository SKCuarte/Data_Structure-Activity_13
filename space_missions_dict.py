#1. Create a dictionary of 5 space missions and their corresponding years.
dict = {
"Mercury program": 1958,
"Gemini program": 1961,
"Apollo program": 1960,
"Skylab": 1964,
"Space Shuttle program": 1972
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the year of the 3rd mission.
print("The year of the 3rd mission is: ", dict["Apollo program"])

#4. Update the year of the 2nd mission.
dict["Gemini program"] = 1965
print(dict)

#5. Delete the 4th mission from the dictionary.
del dict["Skylab"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)