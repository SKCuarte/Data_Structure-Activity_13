#1. Create a dictionary of 8 festivals and their locations.
dict = {
"Ati-Atihan Festival": "Kalibo, Aklan, Panay",
"Sinulog Festival": "Cebu City",
"Kaamulan Festival": "Malaybalay City, Bukidnon",
"Moriones Festival": "Island of Marinduque",
"Panagbenga Festival": "Baguio City",
"Giant Lantern Festival": "San Fernando City",
"Dinagyang Festiva": "Iloilo City",
"Pahiyas Festival": "Lucban, Quezon",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the location of the 4th festival.
print("The location of the 4th festival is: ", dict["Moriones Festival"])

#4. Update the location of the 6th festival.
dict["Giant Lantern Festival"] = "SF City"
print(dict)

#5. Delete the 2nd festival from the dictionary.
del dict["Sinulog Festival"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)