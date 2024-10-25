#1. Create a dictionary of 8 beaches and the countries they are located in.
dict = {
"Praia da Falésia in Olhos de Agua": "Portugal",
"Spiaggia dei Conigli": "Italy",
"La Concha Beach": "Spain",
"Ka'anapali Beach": "Hawaii",
"Grace Bay Beach": "Turks and Caicos",
"Anse Lazio": "Seychelles",
"Manly Beach": "Australia",
"Eagle Beach": "Aruba",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the country of the 3rd beach.
print("The country of the 3rd beach is: ", dict["La Concha Beach"])

#4. Update the country of the 6th beach.
dict["Anse Lazio"] = "East Africa"
print(dict)

#5. Delete the 5th beach from the dictionary.
del dict["Grace Bay Beach"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value is: ", last_key, ":", last_value)