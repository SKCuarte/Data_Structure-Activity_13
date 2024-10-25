#1. Create a dictionary of 8 animals and their corresponding sounds.
sound_dict = {
"Dog": "Woof",
"Cat": "Meow",
"Frog": "Ribbit",
"Cow": "Moo",
"Goat": "Meh",
"Owl": "Hoot",
"Bird": "Twit",
"Bat": "Eek"
}

#2. Print the entire dictionary.
print(sound_dict)

#3. Access and print the sound of the 4th animal.
print("The sound of the 4th animal is: ", sound_dict["Cow"])

#4. Update the sound of the 7th animal.
sound_dict["Bird"] = "Chirp"
print(sound_dict) 

#5. Delete the 5th animal from the dictionary.
del sound_dict["Goat"]
print(sound_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(sound_dict.keys())[-1]
last_value = list(sound_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)
