#1. Create a dictionary of 10 phone models and their manufacturers.
dict = {
"Acer Liquid Z630s": "Acer",
"iPhone 16 Pro Max": "Apple",
"Cherry Mobile One": "Cherry Mobile",
"HP Slate 6 VoiceTab II": "HP",
"Infinix GT 20 Pro": "Infinix",
"Lenovo K8 Plus": "Lenovo",
"LG G8X ThinQ": "LG",
"Microsoft Lumia 950 XL Dual SIM": "Microsoft",
"Nokia 7 Plus": "Nokia",
"Razer Phone 2": "Razer",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the manufacturer of the 2nd phone model.
print("The manufacturer of the 2nd phone model is: ", dict["iPhone 16 Pro Max"])


#4. Update the manufacturer of the 8th phone model.
dict["Microsoft Lumia 950 XL Dual SIM"] = "MS Company"
print(dict)

#5. Delete the 6th phone model from the dictionary.
del dict["Lenovo K8 Plus"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)