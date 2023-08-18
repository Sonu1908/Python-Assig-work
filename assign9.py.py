'''
studno=int(input("No of student:"))
stud=(input("Student name: "))
sub1=int(input("English: "))
sub2=int(input("Physics: "))
sub3=int(input("Chemistry: "))
sub4=int(input("Math: "))
sub5=int(input("Computer science: "))
total=sub1+sub2+sub3+sub4+sub5
#print({"total mask: ", total})

x={}
x.update({"stud no": studno, "Student name":stud,"English":sub1,"Physics:":sub2,"Chemistry":sub3,"Math":sub4,"Computer science":sub5})
print(x)
percentage=(total/500)*100
print("percentage:",percentage,"%")
'''




#empty dictionary to store student marks
students_marks = {}

num_students = int(input("Enter the number of students: "))

# Input marks for each student
for i in range(num_students):
    name = input("Enter student name: ")
    marks = []
    for j in range(5):
        marks.append(float(input("Enter marks for subject " + str(j+1) + ": ")))
    students_marks[name] = marks

#Calculate percentage for each student
for name in students_marks:
    marks = students_marks[name]
    total_marks = sum(marks)
    percentage = (total_marks/500) * 100
    students_marks[name] = [marks, percentage]

# Print student marks and percentage
for name in students_marks:
    print(name, students_marks[name])
