
# Tupples are immutable(cannot be changed as list). So we have to create new tupple if we want to do changes in the tupple

my_tupple1=(1,2,3,4,5)
my_tupple2=(6,7,8,9,10)

collection=my_tupple1+my_tupple2   # "+"-- concatinates two tupples
print(collection)

print(my_tupple1.index(3))         # index("element") --prints the first occurence of the 3 form the tupple 1

a,b,c,d,e=my_tupple1               # tupples can we be unpacked into individual variables
print(a,b)
print(c,d)
print(e)

print(len(my_tupple1))             # len(tupple) -- Used to find the length of the tupple

print(min(my_tupple1),max(my_tupple1))   #min(),max() -- Used to find the max and min form the tupple 

print(2 in my_tupple1)             # "in"-- used to check if element is present inside the tupple or not

my_tupple3=my_tupple1*3            # "*"-- Used to repeated the tupple
print(my_tupple3)