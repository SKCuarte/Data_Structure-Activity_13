#1. Create a dictionary of 12 books and their authors.
book_dict = {
"The Hunger Games": "Suzanne Collins",
"Dune": "Frank Herbert",
"The Fault in Our Stars": "John Green",
"One Hundred Years of Solitude": "Gabriel Garcia",
"To Kill a Mockingbird": "Harper Lee",
"The Lord of the Rings": "J.R.R Tolkein",
"Anna Karenina": "Leo Tolstoy",
"The Brothers Karamazov": "Fyodor Dostoevsky",
"Ulysses" : "James Joyce",
"I'm Not Scared": "Niccolo Ammaniti",
"Lolita": "Vladimir Nabokov",
"The Way of Kings": "Brandon Sanderson"
}

#2. Print the entire dictionary.
print(book_dict)

#3. Access and print the author of the 9th book.
print("The author of the 9th book is: ", book_dict["Ulysses"])

#4. Update the author of the 5th book.
book_dict["To Kill a Mockingbird"] = "Kyan Cuarte"
print(book_dict)

#5. Delete the 3rd book from the dictionary.
del book_dict["The Fault in Our Stars"]
print(book_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(book_dict.keys())[-1]
last_value = list(book_dict.values())[-1]
print("The last key-value is: ", last_key, ":", last_value)





