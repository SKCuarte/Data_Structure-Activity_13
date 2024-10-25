#1. Create a dictionary of 10 car models and their engine specifications.
dict = {
"Tesla Model Y": "384 hp",
"Toyota Camry": "301 hp",
"Chevrolet Silverado": "285 hp",
"Suzuki Ertiga": "103 hp",
"Toyota Fortuner": "201 hp",
"Venom 1000 Ford Mustang GT500": "1000 hp",
"Hyundai Tucson": "187 hp",
"Chevrolet Equinox": "175 hp",
"GMC Sierra": "310 hp",
"Honda Civic": "200 hp",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the specifications of the 4th car model.
print("The specifications of the 4th car model is: ", dict["Suzuki Ertiga"])

#4. Update the specifications of the 9th car model.
dict["GMC Sierra"] = "300+ hp"
print(dict)

#5. Delete the 5th car model from the dictionary.
del dict["Toyota Fortuner"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)