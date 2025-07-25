#General break statment - If condition is satisfied immediately exits the loop
for x in range(1,10):
    if x==5:
        break
    print(x)

#General continue statment - if condition is satisfied skips the current iteration and moves back to the next interation
for x in range(1,10):
    if x==5:
        continue
    print(x)
    

#Break statement using list
my_list=[1,2,3,3,4]
for num in my_list:
    if num==3:
        break
    print(num)
    
#Continue statement using list
my_list=[1,2,3,3,4,5]
for num in my_list:
    if num==3:
        continue
    print(num)
    
    
#Break statement using tuple
my_tuple=(1,2,3,3,4,5)
for x in my_tuple:
    if x==4:
        break
    print(x)
    

#Break statement using tuple
my_tuple=(1,2,3,3,4,5)
for x in my_tuple:
    if x==4:
        continue
    print(x)
    
    
#Break statement using dict
my_dict = {"Name": "Umesh", "Age": 25, "City": "Hyd"}
keys=list(my_dict.keys())
print(keys)
for x in keys:
    if x=='Age':
        break
    print(f"{x}: {my_dict[x]}")
    

#continue statement using dict
my_dict = {"Name": "Umesh", "Age": 25, "City": "Hyd"}
keys=list(my_dict.keys())
print(keys)
for x in keys:
    if x=='Age':
        continue
    print(f"{x}: {my_dict[x]}")
    
    
# Break statement using set
my_set={1,2,3,4,5}
my_list1=list(my_set)

for x in my_list1:
    if x==3:
        break
    print(x)
    
    
# Continue statement using set
my_set={1,2,3,4,5}
my_list1=list(my_set)

for x in my_list1:
    if x==3:
        continue
    print(x)