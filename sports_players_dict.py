#1. Create a dictionary of 10 sports and their most famous players.
dict = {
"Soccer": "Christiano Ronaldo",
"Cricket": "Donald Bradman",
"Field Hockey": "Dhyan Chand",
"Tennis": "Jannik Sinner",
"Volleyball": "Maksim Mikhaylov",
"Table Tennis": "Ma Long",
"Baseball": "Barry Bonds",
"Golf": "Jack Nicklaus",
"Basketball": "Michael Jordan",
"NFL": "Patrick Mahomes",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the player of the 4th sport.
print("The player of the 4th sport is: ", dict["Tennis"])

#4. Update the player of the 6th sport.
dict["Table Tennis"] = "Kyan Cuarte"
print(dict)

#5. Delete the 10th sport from the dictionary.
del dict["NFL"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)