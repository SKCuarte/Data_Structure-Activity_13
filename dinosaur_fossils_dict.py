#1. Create a dictionary of 7 dinosaurs and where their fossils were found.
dict = {
"Spinosaurus": "North Africa",
"Velociraptor": "Mongolia",
"Diplodocus": "North America",
"Carnotaurus": "Argentina",
"Brontosaurus": "North America",
"Giganotosaurus": "South America",
"Tyrannosaurus rex": "North America",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the location of the 4th dinosaur's fossils.
print("The location of the 4th dinosaur's fossils is: ", dict["Carnotaurus"])

#4. Update the location of the 2nd dinosaur's fossils.
dict["Velociraptor"] = "East Asia"
print(dict)

#5. Delete the 6th dinosaur from the dictionary.
del dict["Giganotosaurus"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)