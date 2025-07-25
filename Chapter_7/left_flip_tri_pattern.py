"""
    A
   AB
  ABC
 ABCD
ABCDE

"""

rows=int(input("Enter no.of rows: "))

#Using 2 for loops:
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print("")
    
print("\n")


#Using 2 while loops:
i=1
while i<=rows:
    print(" "*(rows-i),end="")
    j=1
    while j<=i:
        print(chr(64+j),end="")
        j+=1
    i+=1
    print("")
    

print("\n")