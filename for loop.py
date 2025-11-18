# for loop

cities=["bengluru","mysuru","hubbali"]
for city in cities:
    print(city)

#example
i=1
while i<=10:
    print(i,end= " " )
    i+= 1

print("")

for i in range(1,11):
    print(i,end= " " )
for i in range(1, 11, 2):
    print(i,end= " ")

# bag example

bag=["red","green","blue"]

for ball in bag:
    print(ball)

    # loop over string
    name="priya"
    for letter in name:
        print(letter)

# enumerate which letter should repate how much 

l=[12,1323,14,122]
for  index ,num in enumerate(l):

    print(f"{num} is in {index}th index")

# continue in for loop 

cities=["dvg","hkr","SMG","hubballi"]
for city in cities:
    if city =="SMG":
        continue
    print(city)

    #using else with for loop

    l=[12,1323,14,122]

    for num in l:
        print(num)
        if num==14:
            break
    else:
        print("all printed")

# dictnary
d={"name":"priya","age":22,"income":1}

for key,value in d.items():
    print(key, " ", value)

# nested for loop(multiplication)

for i in range (1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        print()
