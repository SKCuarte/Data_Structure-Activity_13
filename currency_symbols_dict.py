#1. Create a dictionary of 10 currencies and their symbols.
dict = {
"Dollar": "$",
"Euro": "€",
"Pound Sterling": "£",
"Yen": "¥",
"Franc": "₣",
"Rupee":  "₹",
"Dinar": "د.ك",
"Dirham": "د.إ",
"Riyal": "﷼‎",
"Mark": "₻"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the symbol of the 5th currency.
print("The symbol of the 5th currency is: ", dict["Franc"])

#4. Update the symbol of the 9th currency.
dict["Riyal"] = "Ä"
print(dict)

#5. Delete the 3rd currency from the dictionary.
del dict["Pound Sterling"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)