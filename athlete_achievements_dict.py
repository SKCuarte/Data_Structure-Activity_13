#1. Create a dictionary of 8 athletes and their greatest achievements.
dict = {
"Joe Dimaggio": "Hitting Streak",
"Wilt Chamberlain": "100 Point Game",
"Bob Beamon": "Long Jump",
"Jesse Owen": "Four World Records in 70 Minutes",
"Nadia Comaneci": "Perfect score in Olympic Gymnastics",
"Usain Bolt": "Fastest Human",
"Babe Ruth": "1920s Career",
"Kurt Browning": "The first Quad",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the achievement of the 5th athlete.
print("The achievement of the 5th athlete is: ", dict["Nadia Comaneci"])

#4. Update the achievement of the 3rd athlete.
dict["Bob Beamon"] = "Jumping Competition"
print(dict)

#5. Delete the 7th athlete from the dictionary.
del dict["Babe Ruth"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)