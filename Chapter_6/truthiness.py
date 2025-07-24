
#Truthiness : Python has a concept of truthiness. Certain values are considered to be falsey in a boolean context including
"""
1. False
2. None
3. 0(zero)
4. Empty strings("")
5. Empty lists([])
6. Empty tuples(())
7. Empty dictionary({})
8. Empty sets(set())

"""


#1. False: 
a=False
if(a):
    print("True")

else:
    print("False")

#2. None :
my_dir ={"Name":"Umesh","Age":25,"CTC":4.5}
ans=my_dir.get("status")

if(ans):
    print("key Present")
else:
    print("Key absent")    
    
#3. 0(Zero):
b=0
if(b):
    print("Non zero")
else:
    print("Zero")
    
#4. Empty strings("") 
my_str=""
if(my_str):
    print("Not empty")
else:
    print("Empty1")

#5. Empty lists([])
my_list=list([])
if(my_list):
    print("Not empty")
else:
    print("Empty2")

#6. Empty tuples(())
my_tuple=tuple(())
if(my_tuple):
    print("Not empty")
else:
    print("Empty3")

#7. Empty dictionary({})
my_dir.clear()
if(my_dir):
    print("Not empty")
else:
    print("Empty4")

#8. Empty sets(set())
my_set=set()
if(my_set):
    print("Not empty")
else:
    print("Empty5")
    
exit