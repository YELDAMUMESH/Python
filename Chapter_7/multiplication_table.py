#multiplication function
def multiplication1(num):
    x=1
    while x<=10:
        print(f"{num} x {x} = {num*x}")
        x+=1
    
def multiplication2(num):
    
    for x in range(1,11):
        print(f"{num} x {x} = {num*x}")
        

def multi_reverse(num):
    i=10
    while i>0:
        print(f"{num} x {i} = {num*i}")
        i-=1

#main function
number=int(input("Enter a number: "))
print("\nUsing while loop: \n")
multiplication1(number)
print("\nUsing for loop: \n")
multiplication2(number)
print("Multiplication in reverse order: ")
multi_reverse(number)