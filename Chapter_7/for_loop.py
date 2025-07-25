#For looping through list
my_list=[56,78,23,67,89]

for x in my_list:
    print(x)

else:
    print("Loop completed successfully!")
    

#For looping through tuple
my_tuple=(1,2,3,4,5)

for i in my_tuple:
    print(i)

else:
    print("Done!")
    

#for looping through strings
my_string="Umesh"

for i in my_string:
    print(i)

else:
    print("Finised!")
    

#for looping through dictionary's keys
my_dict={"Name":"Umesh","Age":25,"City":"Hyd"}

for key in my_dict:
    print(f"{key}: {my_dict[key]}")
    
else:
    print("Completed!")
    
    
#for looping using range() function
for i in range(0,5):
    print(i)

for i in range(5):
    print(i)

for i in range(0,10,2):
    print(i)
    
else:
    print("Finished!")
    

#For looping using enumerate() function - this is used when we want both index and element
for index,element in enumerate(my_list):
    print(f"Element at index {index} is {element}")

else:
    print("Interation completed")
    
