#1. Create a dictionary of 8 movie genres and their corresponding example movies.
dict = {
"Fantasy": "Harry Potter",
"Action": "Fall Guy",
"Drama": "Titanic",
"Horror": "Smile", 
"Thriller": "Gone Girl",
"Romance": "La La Land",
"Comedy": "Central Intelligence",
"Mystery": "Knives Out"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the example movie of the 3rd genre.
print("The example movie of the 3rd genre is: ", dict["Drama"])

#4. Update the example movie of the 5th genre.
dict["Thriller"] = "Cold Pursuit"
print(dict)

#5. Delete the 7th genre from the dictionary.
del dict["Comedy"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)