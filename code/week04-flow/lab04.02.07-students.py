# A Program that reads in students
# until the user enters a blank
# and then prints them all out again

students = []

firstname = input("enter firstname (blank to quit): ").strip()
while firstname != "":
    student = {}
    student["firstname"] = firstname
    lastname = input("enter lastname: ").strip()
    student["lastname"] = lastname
    students.append(student)
    # next student
    firstname = input("enter firstname of next (blank to quit): ").strip()

print ("here are the students you entered:")
for currentStudent in students:
    print ("{} {}".format(currentStudent["firstname"], currentStudent["lastname"]))


