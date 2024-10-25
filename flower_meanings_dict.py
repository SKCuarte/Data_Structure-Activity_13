#1. Create a dictionary of 8 flowers and their symbolic meanings.
dict = {
"Acanthus": "Artifice",
"Amaryllis": "Pride",
"Anemone": "Foresaken",
"Bay tree": "Glory",
"Lavender": "Distrust",
"Mint": "Virtue",
"Willow": "Sadness",
"Thyme": "Courage"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the meaning of the 5th flower.
print("The meaning of the 5th flower is: ", dict["Lavender"])

#4. Update the meaning of the 7th flower.
dict["Willow"] = "Unhappiness"
print(dict)

#5. Delete the 6th flower from the dictionary.
del dict["Mint"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)