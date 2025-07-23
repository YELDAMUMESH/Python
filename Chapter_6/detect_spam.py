#Input function
def user_input():
    message=input("Enter the msg you want to check: ")
    return message

#Spam checker
def check(inbox,msg):
    if(inbox.get(msg)):
       print("Spam dectected!!!")
    
    else:
       print("Not a spam")  
       

# Main program:
my_spam={"Make a lot of money": True,"Buy now": True,"Subscribe this": True,"Click this": True}
msg=user_input()
check(my_spam,msg)







    