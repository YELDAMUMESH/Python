"""

  *
 ***
*****

   
"""



#using for loop:
number=int(input("Enter size of the pyramid: "))
for i in range(1,number+1):
    print(" "*(number-i),end="")
    print("*"*((2*i)-1),end="")
    print("")

print("\n")

#Uisng for loop:
rows = number
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print("\n")

#Uisng while loop:
size=number
i=1
while i<size+1:
    print(" "*(size-i),end="")
    print("*"*(2*i-1))
    i+=1