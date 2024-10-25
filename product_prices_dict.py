#1. Create a dictionary of 10 products and their prices.
dict = {
"Facial Cleanser": "378.00",
"Toner": "314.00",
"Hairband": "10.00",
"Body soap": "160.00",
"Umbrella": "349.00",
"Bag": "529.00",
"Eye Glass": "149.00",
"Serum": "248.00",
"Deodorant": "199.00",
"Slippers": "99.00"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the price of the 4th product.
print("The price of the 4th product is: ", dict["Body soap"])

#4. Update the price of the 9th product.
dict["Deodorant"] = "200.00"
print(dict)

#5. Delete the 6th product from the dictionary.
del dict["Bag"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)