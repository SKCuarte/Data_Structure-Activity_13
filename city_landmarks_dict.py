#1. Create a dictionary of 8 cities and their famous landmarks.
dict = {
"Eiffel Tower": "Paris",
"Big Ben": "London",
"Statue of Liberty": "New York",
"Colosseum": "Rome",
"Alcatraz": "San Francisco",
"Hollywood Sign": "Los Angeles",
"Taj Mahal": "Agra",
"Stonehenge": "Salisbury",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the landmark of the 6th city.
print("The landmark of the 6th city is: ", dict["Hollywood Sign"])

#4. Update the landmark of the 2nd city.
dict["Big Ben"] = "England"
print(dict)

#5. Delete the 7th city from the dictionary.
del dict["Taj Mahal"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)