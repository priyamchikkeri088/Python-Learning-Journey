# if-elif-else

x = 13
if x%2 == 0:
     print("yes x is even")
else:
     print("yes x is old")


#signal example
signal =input("What the colour of the signal:")

if signal=="red":
     print("STOP")
elif signal=="yellow":
     print("READY")
elif signal=="Green":
     print("GO")
else:
    print("Nothing")

# comparision operation

age = 54
 
if age >=18:
     print("your are eligible to vote")
else:
     print("Not eligible")

#logical operations

age=16
has_student_id=True
 
if age<18 and has_student_id:
     print("you are eligible for the student discount!")
else:
     print("you are not eligible")

#bus ticket ex
gender=input("gender:")
age = input("age:")

if gender=="female":
    print("Ticket is free")
else:
    if age <=5:
     print("Ticket is free.")
    elif age <= 12:
        print("You get a child discount.")
    elif age >= 60:
        print("You get a senior citizen discount.")
    else:
         print("You pay the full fare .")