#1. Create a dictionary of 10 states and their capitals.
dict = {
"Alabama": "Montgomery",
"California": "Sacramento",
"Delaware": "Dover",
"Florida": "Tallahassee",
"Hawaii": "Honolulu",
"Iowa": "Des Moines",
"Kentucky": "Frankfort",
"Maine": "Augusta",
"Nebraska": "Lincoln",
"New York": "Albany",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the capital of the 4th state.
print("The capital of the 4th state is: ", dict["Florida"])

#4. Update the capital of the 9th state.
dict["Nebraska"] = "Scranton"
print(dict)

#5. Delete the 7th state from the dictionary.
del dict["Kentucky"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)