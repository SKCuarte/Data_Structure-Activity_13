#1. Create a dictionary of 7 sports events and their corresponding years.
dict = {
"The Miracle on Ice": "1980",
"The Fight of the Century": "1971",
"MJ's The Shot": "1989",
"Babe Ruth's Called Shot": "1932",
"Wilt Chamberlain's 100 Point Game": "1962",
"The Shot Heard Round the World": "1951",
"1987 NBA Finals - Game 4": "1987",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the year of the 3rd sports event.
print("The year of the 3rd sports event is: ", dict["MJ's The Shot"])

#4. Update the year of the 6th sports event.
dict["The Shot Heard Round the World"] = "1950s"
print(dict)

#5. Delete the 5th sports event from the dictionary.
del dict["Wilt Chamberlain's 100 Point Game"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)