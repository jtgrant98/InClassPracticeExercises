import Student_Class as sc

studentid = 1001
name = 'John'
dob = '10/15/2001'
classification = 'Junior'

john = sc.Student(studentid, name, dob, classification)

john.calc_age()

john.register()

print("Student age is:",john.return_age())

print("Student can register between:",john.return_registration())


