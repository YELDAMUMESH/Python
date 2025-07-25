"""

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    
"""


#Upper pyramid
rows=int(input("Enter no.of rows: "))
for i in range(rows,0,-1):
    print(" "*(i-1),end="")
    print("*"*(2*(rows-i)+1))

steps=rows
    
#Lower pyramid    
rows=rows-1
for i in range(rows,0,-1):
    print(" "*(rows-i+1),end="")
    print("*"*((2*i)-1))

#Using while loop
#higher pyramid
i=1
while i<steps+1:
    print(" "*(steps-i),end="")
    print("*"*((2*i)-1))
    i+=1
#lower pyramid
i=steps-1
while i>0:
    print(" "*(steps-i),end="")
    print("*"*((2*i)-1))
    i-=1