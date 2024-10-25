#1. Create a dictionary of 6 rivers and their lengths in kilometers.
dict = {
"Yellow River": "5,464km",
"Lena River": "4,400km",
"Mekong River": "4,350km",
"Niger River": "4,200km",
"Yukon River": "3,185km",
"Rio Grande River": "2,057km"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the length of the 2nd river.
print("The length of the 2nd river is: ", dict["Lena River"])

#4. Update the length of the 5th river.
dict["Yukon River"] = "3,200km"
print(dict)

#5. Delete the 4th river from the dictionary.
del dict["Niger River"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)
