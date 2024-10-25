#1. Create a dictionary of 10 apps and their user ratings.
dict = {
"Canva": "4.9/5",
"Messenger": "2.9/5",
"Netflix": "2.4/5",
"WhatsApp": "3.7/5",
"Roblox": "4.2/5",
"Minecraft": "4.5/5",
"Candy Crush Sage": "4.7/5",
"Candy Crush Soda Saga": "4.6/5",
"Adobe Photoshop": "3.5/5",
"Adobe Lightroom": "4.3/5"
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the rating of the 6th app.
print("The rating of the 6th app is: ", dict["Minecraft"])

#4. Update the rating of the 8th app.
dict["Candy Crush Soda Saga"] = "4.0/5"
print(dict)

#5. Delete the 9th app from the dictionary.
del dict["Adobe Photoshop"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)