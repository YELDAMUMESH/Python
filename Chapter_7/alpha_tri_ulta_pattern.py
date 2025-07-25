
"""

A
BA
CBA
DCBA


"""



rows=int(input("Enter no.of rows: "))

#Using for loops:
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(chr(64+j),end="")
    print("")
    
    
print("\n")


#Using while loops:
i=1
while i<=rows:
    j=i
    while j<=i and j>0:
        print(chr(64+j),end="")
        j-=1
    i+=1
    print("")