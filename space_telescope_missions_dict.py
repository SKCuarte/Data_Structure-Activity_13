#1. Create a dictionary of 5 space telescopes and their missions.
dict = {
"Proton 1": "Gamma ray",
"Uhuru": "X-ray",
"OAO-2": "Ultraviolet",
"Hubble Space Telescope": "Visible light",
"Odin": "Microwave",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the mission of the 3rd telescope.
print("The mission of the 3rd telescope is: ", dict["OAO-2"])

#4. Update the mission of the 1st telescope.
dict["Proton 1"] = "Proton Series" 
print(dict)

#5. Delete the 4th telescope from the dictionary.
del dict["Hubble Space Telescope"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)