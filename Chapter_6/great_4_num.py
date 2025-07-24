# Input function
def Number(): 
    num =int(input("Enter a number: "))
    my_list.append(num)

#finding Maximum element
def find_max(my_list):
    max=my_list[0]
    print(max)
    
    print(my_list)


    #logic
    if(my_list[1]>=max):
        max=my_list[1]
    
    if(my_list[2]>=max):
        max=my_list[2]
    
    if(my_list[3]>=max):
        max=my_list[3]
        
    return max

#Finding minimum elemnt:
def find_min(my_list):
    min=my_list[0]
    print(min)
    
    print(my_list)


    #Finding maximum
    if(my_list[1]<=min):
        min=my_list[1]
    
    if(my_list[2]<=min):
        min=my_list[2]
    
    if(my_list[3]<=min):
        min=my_list[3]
        
        
    return min

###################################################


my_list=[]    
Number()
Number()
Number()
Number()
print(my_list)
maximum=find_max(my_list)
minimum=find_min(my_list)

print(f"Maximum : {maximum}\nMinimum: {minimum}")
    

