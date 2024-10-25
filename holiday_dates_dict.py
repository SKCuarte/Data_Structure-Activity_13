#1. Create a dictionary of 10 holidays and their corresponding dates.
dict = {
"New Year’s Day": "January 1",
"Valentine’s Day": "February 14",
"St. Patrick’s Day": "March 17",
"April Fool’s Day": "April 01",
"Independence Day": "July 04",
"Liberation Day": "August 15",
"Halloween": "October 31",
"All Saints’ Day": "November 01",
"Christmas Day": "December 25",
"New Year’s Eve": "December 31",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the date of the 4th holiday.
print("The date of the 4th holiday is: ", dict["April Fool’s Day"])

#4. Update the date of the 9th holiday.
dict["Christmas Day"] = "December"
print(dict)

#5. Delete the 2nd holiday from the dictionary.
del dict["Valentine’s Day"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)