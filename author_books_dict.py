#1. Create a dictionary of 8 authors and their famous books.
dict = {
"Philip Roth": "Letting Go",
"Erica Jong": "Fear of Flying",
"Donald J. Sobol": "Encyclopedia Brown, Boy Detective",
"Paul Kalanithi": "When Breath Becomes Air",
"Mark Twain": "The Adventures of Tom Sawyer",
"Nathaniel Philbrick": "In the Heart of the Sea",
"Louisa May Alcott": "Little Women",
"E.B. White": "Charlotte's Web",
}

#2. Print the entire dictionary.
print(dict)

#3. Access and print the book of the 5th author.
print("The book of the 5th author is: ", dict["Mark Twain"])

#4. Update the book of the 7th author.
dict["Louisa May Alcott"] = "Sherlock Holmes"
print(dict)

#5. Delete the 6th author from the dictionary.
del dict["Nathaniel Philbrick"]
print(dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(dict.keys())[-1]
last_value = list(dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value) 