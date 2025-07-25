# finding prime numbers

def prime(num):
    if num==1:
        print(f"{num} is neither prime nor composite number")
    else:
        for i in range(2,num):
            if num%i==0:
                print(f"{num} not a prime number")
                break
            else:
                print(f"{num} is a prime number ")
                break
                
           
#main function:
number=int(input("Enter a number: "))
prime(number)
           
       
        
   
