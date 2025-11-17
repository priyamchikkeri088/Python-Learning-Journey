# while loop

is_failed =True
i=1 #attempt

while is_failed :
    print(f"Try {i}")
    i=i+1
    if i>100:
        break

print("I gave up!")

#for even attempts

is_failed =True
i=1 #attempt

while is_failed :
    if i%2!=0:#is not even
        i=i+1
        continue
    print(f"attempt {i}")
    i=i+1
    
    if i>100:
        break

print("I gave up!")

#counting numbers

i=0

while i<=10:
    x=0
    while x<i:
        print("priya")
    print(i)
    i=i+1

    # user input

    pin="1234"
    trials =0

while trials<3:
    input_pin=input(f"trail_{trials}|PIN>>")
    trials=1
    if input_pin==pin:
        print("SUCCESS")
        break
    else:
        print("incorrect")