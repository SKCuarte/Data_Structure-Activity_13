#1. Create a dictionary of 7 programming languages and their developers.
prog_dict = {
"Java": "James Gosling",
"C": "Dennis Ritchie",
"JavaScript": "Brendan Eich",
"Python": "Guido van Rossum",
"C++": "Bjarne Stroustrup",
"PHP": "Rasmus Lerdorf",
"Perl": "Larry Wall"
}


#2. Print the entire dictionary.
print(prog_dict)

#3. Access and print the developer of the 4th programming language.
print("The developer of the 4th programming language is: ", prog_dict["Python"])

#4. Update the developer of the 6th programming language.
prog_dict["PHP"] = "Kyan Cuarte"
print(prog_dict)

#5. Delete the 2nd programming language from the dictionary.
del prog_dict["C"]
print(prog_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(prog_dict.keys())[-1]
last_value = list(prog_dict.values())[-1]
print("The last key-value is: ", last_key, ":", last_value)