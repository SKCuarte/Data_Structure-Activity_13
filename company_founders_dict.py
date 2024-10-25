#1. Create a dictionary of 8 companies and their founders.
dict = {
"Open AI": "Altman, Sam",
"Amazon": "Bezos, Jeff",
"Virgin Group ": "Branson, Richard",
"Nvidia": "Huang, Jensen",
"Alibaba": "Ma, Jack",
"Space X": "Musk, Elan",
"Meta": "Zuckerberg, Mark",
"General Motors": "Durant, William",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the founder of the 6th company.
print("The founder of the 6th company is: ", dict["Space X"])

#4. Update the founder of the 2nd company.
dict["Amazon"] = "Jeff Bezos"
print(dict)

#5. Delete the 8th company from the dictionary.
del dict["General Motors"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)