#1. Create a dictionary of 5 students and their corresponding grades.
grade_dict = {
"Student1": "A+", 
"Student2": "C+", 
"Student3": "B", 
"Student4": "D", 
"Student5": "F"
}

#2. Print the entire dictionary.
print(grade_dict)

#3. Access and print the grade of the 3rd student.
print("Grade of third student: ", grade_dict["Student3"])        

#4. Update the grade of the 2nd student.
grade_dict["Student2"] = "A"
print(grade_dict)

#5. Delete the entry of the 5th student.
del grade_dict["Student5"]      
print(grade_dict)

#6. Print the last key-value pair in the dictionary.
last_key = list(grade_dict.keys())[-1]
last_value = list(grade_dict.values())[-1]
print("The last key-value pair is: ", last_key, ":", last_value)