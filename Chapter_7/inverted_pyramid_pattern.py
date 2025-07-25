"""

*********
 *******
  *****
   ***
    *
     
"""
rows=int(input("Enter no.of rows: "))

for i in range(1,rows+1):
    print(" "*(i-1),end="")
    print("*"*(2*rows-(2*i-1)))

print("\n")

i=1    
while i<rows+1:
    print(" "*(i-1),end="")
    print("*"*(2*rows-(2*i-1)))
    i+=1
    
print("\n")

for i in range(rows, 0, -1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
