#User input
def user_input():
    name=input("Enter your name: ")
    return name

#Name checker
def name_checker(inbox,msg):
    if(inbox.count(msg)):
        print("Name already exist in the list")
        
    else:
        print("Name does not exist in the list ")


# Main program
names_coll=["Umesh","Nani","Bunny","Chintu","Yeshu"]
my_name=user_input()
name_checker(names_coll,my_name)