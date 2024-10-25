#1. Create a dictionary of 6 software programs and their latest versions.
dict = {
"Messenger": "	431.1.0.35.116",
"Netflix": "Version 8.135.1 build 7 50902",
"WhatsApp": "2.24.21.75",
"Mobile Legends": "21.9.22.10104",
"Clash of Clans": "16.517.17",
"Candy Crush": "1.288.3.1",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the version of the 4th software.
print("The version of the 4th software: ", dict["Mobile Legends"])

#4. Update the version of the 2nd software.
dict["Netflix"] = "Version 8.135.1"
print(dict)

#5. Delete the 5th software from the dictionary.
del dict["Clash of Clans"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)