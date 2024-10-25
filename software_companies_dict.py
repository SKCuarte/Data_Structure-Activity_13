#1. Create a dictionary of 10 software companies and their headquarters.
comp_dict = {
"Microsoft": "Redmond, Washington",
"Google": "Mountain View, California",
"Oracle": "Austin, Texas",
"Salesforce": "San Francisco, California",
"SAP": "Walldorf",
"Adobe": "San Jose, California",
"Intuit": "Palo Alto, California",
"IBM": "Armonk, New York",
"ServiceNow": "Santa Clara, California",
"ADP": "Roseland, New Jersey"
}

#2. Print the entire dictionary.
print(comp_dict)

#3. Access and print the headquarters of the 3rd company.
print("The headquarters of the 3rd company is: ", comp_dict["Oracle"])

#4. Update the headquarters of the 8th company.
comp_dict["IBM"] = "Manila, Philippines"
print(comp_dict)

#5. Delete the 9th company from the dictionary.
del comp_dict["ServiceNow"]
print(comp_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(comp_dict.keys())[-1]
last_value = list(comp_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)


