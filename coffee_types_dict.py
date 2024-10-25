#1. Create a dictionary of 10 types of coffee and their descriptions.
dict = {
"Black": "Plain",
"Latte": "Espresso with Steamed Milk",
"Cappuccino": "Espresso with Steamed Milk and Foam",
"Americano": "Espresso with Hot Water",
"Espresso": "1oz Espresso",
"Doppio": "2oz Espresso",
"Cortado": "1oz Espresso and 1oz Steamed Milk",
"Red Eye": "Coffee with Espresso",
"Galao": "Espresso with Foamed Milk",
"Lungo": "Long pulled Espresso",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the description of the 4th type of coffee.
print("The description of the 4th type of coffee is: ", dict["Americano"])

#4. Update the description of the 8th type of coffee.
dict["Red Eye"] = "Coffee mixed with Espresso"
print(dict)

#5. Delete the 5th type of coffee from the dictionary.
del dict["Espresso"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)