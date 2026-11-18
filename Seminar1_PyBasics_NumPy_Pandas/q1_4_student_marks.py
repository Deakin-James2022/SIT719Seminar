# Please declare a dictionary with student final marks and print the dictionary items using keys and for loop. Example: student-names = [john, eve, alice, bob, mercy] and grades = [80, 50, 60, 65, 82].

student_names = ["john", "eve", "alice", "bob", "mercy"]
grades = [80, 50, 60, 65, 82]
# Create dictionary
student_marks = dict(zip(student_names, grades))
# Print dictionary
for key in student_marks.keys():
    print(key, ":", student_marks[key])
