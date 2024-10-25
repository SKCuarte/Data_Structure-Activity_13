#1. Create a dictionary of 10 movies and their directors.
direct_dict = {
"Inception": "Christopher Nolan",
"Gravity": "Alfonso Cuaron",
"The Lord of the Rings": "Peter Jackson",
"Airplane!": "David Zucker", 
"Pulp Fiction": "Quentin Tarantino",
"Network": "Sidney Lumet",
"Casino Royale": "Martin Campbell",
"Fargo": "Joel Coen",
"Seven": "David Fincher",
"Terminator": "James Cameron",
}

#2. Print the entire dictionary.
print(direct_dict)

#3. Access and print the director of the 5th movie.
print("The director of the 5th movie is: ", direct_dict["Pulp Fiction"])

#4. Update the director of the 9th movie.
direct_dict["Seven"] = "Kyan Cuarte"
print(direct_dict)

#5. Delete the 7th movie from the dictionary.
del direct_dict["Casino Royale"]
print(direct_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(direct_dict.keys())[-1]
last_value = list(direct_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)

