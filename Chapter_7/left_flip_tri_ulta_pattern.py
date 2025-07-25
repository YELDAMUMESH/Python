
"""
    A
   BA
  CBA
 DCBA
EDCBA

"""


rows=int(input("Enter no.of rows: "))

#Uisng 2 for loops:
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(i,0,-1):
        print(chr(64+j),end="")
    print("")
    
print("\n")

#Uisng 2 while loops:
i=1
while i<=rows:
    j=i
    print(" "*(rows-i),end="")
    while j>0:
        print(chr(64+j),end="")
        j-=1
    i+=1
    print("")
    
print("\n")