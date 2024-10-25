#1. Create a dictionary of 10 cities and their corresponding population.
popu_dict = {
"Tokyo": "37.5m",
"Delhi": "28.5m",
"Shanghai": "25.6m",
"Sao Paulo": "21.7m",
"Mexico City": "21.6m",
"Cairo": "20.1m",
"Mumbai": "20m",
"Beijing": "19.6m",
"Dhaka": "19.6m",
"Osaka": "19.3m"
}

#2. Print the entire dictionary.
print(popu_dict)

#3. Access and print the population of the 6th city.
print("The population of 6th city is: ", popu_dict["Cairo"])

#4. Update the population of the 3rd city.
popu_dict["Shanghai"] = "25m"
print(popu_dict)

#5. Delete the 9th city from the dictionary.
del popu_dict["Dhaka"] 
print(popu_dict)

#6 Print the last key-value pair in the dictionary.
last_key = list(popu_dict.keys())[-1]
last_value = list(popu_dict.values())[-1]
print("The last key-value is: ", last_key, ":", last_value)

