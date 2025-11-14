name =("enter your name")
age= int(input("enter your age: "))
print(age)


boy_name = input("boy_name: ")
boy_age = int(input("boy age: "))
girl_name = (input("girl name: "))
girl_age= int(input("girl age: "))
# using abs beacuse sometimes boy might be younger
age_diff = abs(boy_age - girl_age)
print(boy_name)
print(girl_name)
print (boy_name + " loves " + girl_name +". Age difference is "+ str(age_diff))

print(f"{boy_name} loves {girl_name} .Age Difference")



first_name = "chandan"
last_name = "gowda"
full_name = first_name + " " + last_name
print(full_name)

# Repetition
message = " Warning !"
print(message*10)
print(message.upper())
print(message.lower())
print(message.strip()*2)