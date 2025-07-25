#Regular example
count=0
while count<=5:
    print(count)
    count+=1
else:
    print("Completed!")

#Looping through lists
my_list=[34,65,78,92,56]
size=len(my_list)
i=0
while i<size:
    print(my_list[i])
    i+=1
    
#Looping through tuple
my_tuple=(5,4,3,2,1)
size=len(my_tuple)
i=0
while i<size:
    print(my_tuple[i])
    i+=1

#Looping through dict -- Less popular , For loop is mostly used
my_dict = {"Name": "Umesh", "Age": 25, "City": "Hyd"}
keys = list(my_dict.keys())  # Get a list of the keys
size = len(keys)
key_index = 0

while key_index < size:
    key = keys[key_index]
    print(key, ":", my_dict[key])
    key_index += 1

#Looping through set
my_set={1,2,3,4,5}
convert_list=list(my_set)
size=len(convert_list)
i=0
while i<size:
    print(convert_list[i])
    i+=1
    
    
#looping while a specific input is received
user_input=""

while user_input!="quit":
    user_input=input("Enter something (or 'quit' to exit): ")
    print(f"You have entered: {user_input}")
    
else:
    print("Bye seen you again")