#1. Create a dictionary of 10 jobs and their average salaries.
dict = {
"Cardiology": "240,000 Dollars",
"Anesthesiologist": "370,000 Dollars",
"Orthodontist": "294,000 Dollars",
"Psychiatrist": "255,000 Dollars",
"Surgeon": "297,000 Dollars",
"Periodontist": "209,000 Dollars",
"Physician": "214,000 Dollars",
"Dentist": "223,000 Dollars",
"Internal Medicine Physician": "278,000 Dollars",
"Obstetrician": "200,000 Dollars",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the salary of the 3rd job.
print("The salary of the 3rd job is ", dict["Orthodontist"])

#4. Update the salary of the 7th job.
dict["Physician"] = "200,000+ Dollars"
print(dict)

#5. Delete the 9th job from the dictionary.
del dict["Internal Medicine Physician"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)