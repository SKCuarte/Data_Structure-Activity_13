#1. Create a dictionary of 10 car brands and their country of origin.
car_dict = {
"Volvo": "Sweden",
"Volkswagen": "Germany",
"Toyota": "Japan",
"Ford": "USA",
"Mercedes-Benz": "Germany",
"BMW": "Germany",
"Kia": "Korea",
"Audi": "Germany",
"Renault": "France",
"Peugeot": "France"
}

#2. Print the entire dictionary.
print(car_dict)

#3. Access and print the country of origin of the 3rd car brand.
print("The origin of 3rd car brand is: ", car_dict["Toyota"])

#4. Update the country of origin of the 7th car brand.
car_dict["Kia"] = "India"
print(car_dict)

#5. Delete the 8th car brand from the dictionary.
del car_dict["Audi"]
print(car_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(car_dict.keys())[-1]
last_value = list(car_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)
