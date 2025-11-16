# tuples and sets

genders =("male","female","others")
print(genders[2])

tuple1=(1,2,3,4)
tuple2=(4,5,6,7)
combined_tuple =tuple1+tuple2
print(combined_tuple)

#checking membership
Fruits =("apple", "papaya","grape")
print("apple" in Fruits)
print(Fruits.index("grape"))

#sets

s ={50,26,30} # set is unorder
s2= {(1,2,3)}
print(type(s2))

#set operation
S1={1,2,3}
S2={3,4,5}
print(S1-S2)
print(S2-S1) #difference
print(S1|S2) #union
print(S1&S2) #intersection
print(S1^S2)#symmetric diff


#difference b/w lists ,tuples,sets
l=[1,7,8]
t=(2,4,6)
s={1,7,9}
print(l)
print(s)
print(t)



