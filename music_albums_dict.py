#1. Create a dictionary of 10 music albums and their release years.
dict = {
"Lemonade": "2016",
"Nevermind": "1991",
"Back to Black": "2006",
"good kid, m.A.A.d city": "2012",
"Songs in the Key of Life": "1976",
"Blonde": "2016",
"Purple Rain": "1984",
"Abbey Road": "1969",
"Thriller": "1982",
"The Miseducation of Lauryn Hill": "1998",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the release year of the 3rd album.
print("The release year of the 3rd album is: ", dict["Back to Black"])

#4. Update the release year of the 8th album.
dict["Abbey Road"] = "1960s" 
print(dict)

#5. Delete the 5th album from the dictionary.
del dict["Songs in the Key of Life"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)