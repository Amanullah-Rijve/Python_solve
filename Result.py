# The provided code stub will read in a dictionary containing 
# key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name 
# provided, showing 2 places after the decimal.


mark_dict = {
"Rijve": [80,67,90,57],
"Aman": [50,89,29,48],
"Apon": [64,78.,98,36]
}

student_name = input("Enter Student's Name: ")

marks = mark_dict.get(student_name)

if marks:
    avarage = sum(marks) / len(marks)
    print(f" Student Name is {student_name} and Avarage Mark {avarage: .2f}")
else: print(f"Student Name {student_name} result not found")
