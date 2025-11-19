l=[1,23,43,543,32]
total=0

for num in l:
    print(total)
    total=total+num
  
print(total)

#for double number 
l=[1,23,43,534,32]
dl=[]

for num in l:
    dl.append(num*2)
    print(dl)

#looping through dictionaries

student_marks={"pri":90,"raks":85,"appu":90,"shreya":90}

for student ,marks in student_marks.items():
    print(f"{student} -{marks}")

# loop in range

students=["pri","raks","appu","shreya"]
marks=[90,80,60,66]

student_marks={}

for index,student in enumerate(students):
    student_marks[student] = marks[index]

print(student_marks)

# joining both marks and student

students=["pri","raks","appu","shreya"]
marks=[90,80,60,66]

student_marks={}

for i in range(4):   # we take range(len(students)):(when we dont know how much student)
    student_marks[students[i]]=marks[i]

    print(student_marks)
