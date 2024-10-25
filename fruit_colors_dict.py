#1. Create a dictionary of 8 fruits and their corresponding colors.
fruit_dict = {
"Banana": "Yellow",
"Apple": "Red",
"Orange": "Orange",
"Kiwi": "Brown",
"Dragon Fruit": "Red",
"Pear": "Yellow",
"Coconut": "Green",
"Grapes": "Black"
}

#2. Print the entire dictionary.
print(fruit_dict)

#3. Access and print the color of the 6th fruit.
print("The color of the 6th fruit is: ", fruit_dict["Pear"])

#4. Update the color of the 4th fruit.
fruit_dict["Kiwi"] = "Green"
print(fruit_dict)

#5. Delete the 7th fruit from the dictionary.
del fruit_dict["Coconut"]
print(fruit_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(fruit_dict.keys()) [-1]
last_value = list(fruit_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)



