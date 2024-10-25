#1. Create a dictionary of 10 companies and their current CEOs.
dict = {
"Amazon": "Andy Jassy",
"Intel": "Patrick P. Gelsinger",
"Rolex": "Jean-Frederic Dufour",
"MediaTek": "Rick Tsai",
"Twitter": "Elon Musk",
"MasterCard": "Michael Meibach",
"Adidas": "Kasper Rørsted",
"Nike": "John Donahoe",
"HSBC": "Noel Quinn",
"Walt Disney": "Bob Chapek"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the CEO of the 6th company.
print("The CEO of the 6th company is:", dict["MasterCard"])

#4. Update the CEO of the 3rd company.
dict["Rolex"] = "Kyan Cuarte"
print(dict)

#5. Delete the 9th company from the dictionary.
del dict["HSBC"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)