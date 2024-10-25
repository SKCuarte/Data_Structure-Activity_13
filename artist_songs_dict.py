#1. Create a dictionary of 8 artists and their top songs.
dict = {
"Jason Derulo": "In My Head",
"OneRepublic": "Counting Stars",
"Adele": "Someone Like You",
"Lady Gaga": "Bad Romance",
"Maroon 5": "This Love",
"Olly Murs": "Troublemaker",
"Sabrina Carpenter": "Espresso",
"Travis Scott": "FE!N",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the top song of the 3rd artist.
print("The top song of the 3rd artist: ", dict["Adele"])

#4. Update the top song of the 6th artist.
dict["Olly Murs"] = "Dance With Me Tonight"
print(dict)

#5. Delete the 7th artist from the dictionary.
del dict["Sabrina Carpenter"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)