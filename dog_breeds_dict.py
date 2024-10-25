#1. Create a dictionary of 10 dog breeds and their sizes (small, medium, large).
dict = {
"Yorkshire Terrier": "Small",
"Shih Tzu": "Small",
"Chihuahua": "Small",
"English Bulldog": "Medium",
"Shetland Sheepdog": "Medium",
"Cocker Spaniel": "Medium",
"Lakeland Terrier": "Medium",
"Labrador Retriever": "Large",
"Saint Bernard": "Large",
"Great Dane": "Large",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the size of the 5th breed.
print("The size of the 5th breed is: ", dict["Shetland Sheepdog"])

#4. Update the size of the 8th breed.
dict["Labrador Retriever"] = "Big"
print(dict)

#5. Delete the 6th breed from the dictionary.
del dict["Cocker Spaniel"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)