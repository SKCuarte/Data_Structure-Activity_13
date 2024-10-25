#1. Create a dictionary of 12 countries and their capitals.
cap_dict = {
"Russia": "Moscow",
"United Kingdom": "London",
"Germany": "Berlin",
"Spain": "Madrid",
"Ukraine": "Kiev",
"Italy": "Rome",
"France": "Paris",
"Belarus": "Minsk",
"Austria": "Vienna",
"Romania": "Bucharest",
"Poland": "Warsaw",
"Hungary": "Budapest"
}

#2. Print the entire dictionary.
print(cap_dict)

#3. Access and print the capital of the 5th country.
print("The capital of the 5th country is: ", cap_dict["Ukraine"])

#4. Update the capital of the 8th country.
cap_dict["Belarus"] = "Quezon"
print(cap_dict)

#5. Delete the 11th country from the dictionary.
del cap_dict["Poland"]
print(cap_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(cap_dict.keys())[-1]
last_value = list(cap_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)

