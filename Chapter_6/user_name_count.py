def user_input():
    user_name=input("Enter your user name: ")
    return user_name

def count(profile_name):
    count=len(profile_name)
    
    if(count==10):
        print(f"User name have 10 chacters")
    
    elif(count>=10):
        print(f"User name have more than 10 chacters")
        
    else:
        print(f"User name does not have 10 chacters")
        
# Main profram

name=user_input()
count(name)