studentList = list()
gradesList = list()
info=dict()
averages = list()
for i in range(5):
    minigradeList = list()
    name = input("Enter a student name")
    surname = input("Enter a student surname")
    miniList = [name, surname]
    studentList.append(miniList)
    homework =input("Enter a homework grade")
    midterm = input("Enter a midterm grade")
    final = input("Enter a final grade")
    a = int(homework)+int(midterm)+int(final)
    averages.append(a/3)
    gpa=str(a/3)
    minigradeList = [homework, midterm, final]
    gradesList.append(minigradeList)
    info[(name+" "+surname)] = homework,midterm, final,gpa
averages.sort()
print("Printing the dictionary:\n",info)
b=averages[4]
print("Congratulations to ",[k for k, v in info.items() if str(b) in v[3]], "for being the student who has the highest score: ")

