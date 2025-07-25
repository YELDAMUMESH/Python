def factorial1(number):
    num=number
    fact=1
    while number>0:
        fact=fact*number
        number-=1
        
    print(f"Factorial of {num}! using while loop = {fact}")
    
    
def factorial2(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    print(f"Factorial of {number}! using for loop : {fact}")
    
    
#Main function
num=int(input("Enter any number: "))
factorial1(num)
factorial2(num)