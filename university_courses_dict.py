#1. Create a dictionary of 8 universities and their popular courses.
dict = {
"Stanford": "Computer Science",
"Oxford": "Anthropology",
"California Berkeley": "Bioengineering",
"Cambridge": "Engineering",
"London": "Architecture",
"Washington Seattle": "Social Science",
"Columbia": "Electrical Engineering",
"Yale": "Psychology"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the course of the 3rd university.
print("The course of the 3rd university is: ", dict["California Berkeley"])

#4. Update the course of the 5th university.
dict["London"] = "Mathematics"
print(dict)

#5. Delete the 7th university from the dictionary.
del dict["Columbia"] 
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)

