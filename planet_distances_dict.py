#1. Create a dictionary of 8 planets and their distances from the sun (in million kilometers).
dict = {
"Mercury": "57.9m km",
"Venus": "108.2m km",
"Earth": "149.6m km",
"Mars": "227.9m km",
"Jupiter": "778.6m km",
"Saturn": "1,433.5m km",
"Uranus": "2,872.5m km",
"Neptune": "4,495.1 km"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the distance of the 3rd planet.
print("The distance of the 3rd planet is: ", dict["Earth"])


#4. Update the distance of the 5th planet.
dict["Jupiter"] = "779m km"
print(dict)

#5. Delete the 7th planet from the dictionary.
del dict["Uranus"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)