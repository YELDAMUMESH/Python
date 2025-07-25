"""

A
AB
ABC
ABCD


"""

rows=int(input("Enter no.of rows: "))


#Using for loops
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
    
    
print("\n")
#Using while loops
i=1
while i<=rows:
    j=1
    while j<=i:
        print(chr(64+j),end="")
        j+=1
    i+=1
    print("")