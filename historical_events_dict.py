#1. Create a dictionary of 8 historical events and their years.
dict = {
"Declaration of Independence": "1776",
"The Atomic Bombing of Hiroshima and Nagasaki": "1945",
"Assassination of Martin Luther King, Jr.": "1968",
"September 11 Attacks": "2001",
"Stock Market Crash": "1929",
"Constitution of the United States of America": "1787",
"Election of Donald Trump": "2016",
"COVID-19 Pandemic": "2020",
}

#2. Print the entire dictionary.
print(dict)


#3. Access and print the year of the 2nd event.
print("The year of the 2nd event is: ", dict["The Atomic Bombing of Hiroshima and Nagasaki"])


#4. Update the year of the 7th event.
dict["Election of Donald Trump"] = "2010s"
print(dict)

#5. Delete the 5th event from the dictionary.
del dict["Stock Market Crash"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)