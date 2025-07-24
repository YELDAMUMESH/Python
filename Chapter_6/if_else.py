age=int(input("Enter the age: "))

if(age>=18 and age<=50):
    print("Age verification completed successfully.Please proceed further.")
    print("Have a great day!!!")

elif(age>18 and age>50):
    print("Sorry grandpa,go home and take rest.")
    
elif(age<0):
    print("Are you are child!.Please enter vaild age.")

elif(age==0):
    print("Oh! come on man grow up.Enter valid age.")

else:
    wait=18-age
    print(f"Sorry please wait for {wait} years and come back again. ")
    print("Have a great day!!!")

exit
