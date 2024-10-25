#1. Create a dictionary of 8 video games and their platforms.
dict = {
"Clash of Clans": "Android",
"Fortnite": "PS5",
"God of War: Ragnarok": "PS4",
"Tekken 6": "PSP",
"Fallout 4": "Xbox", 
"Pokemon Emerald": "Gameboy",
"Hogwarts Legacy": "Nintendo Switch",
"Mario Kart 7": "Nintendo 3ds"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the platform of the 2nd video game.
print("The platform of the 2nd video game is: ", dict["Fortnite"])

#4. Update the platform of the 6th video game.
dict["Pokemon Emerald"] = "Android"
print(dict)

#5. Delete the 4th video game from the dictionary.
del dict["Tekken 6"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)