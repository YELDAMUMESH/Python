"""
1
22
333
4444
55555    
    
    
"""

rows=int(input("Enter no.of rows: "))


#Using for loops:
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end="")
    print("")
    

print("\n")


#Using while loops:
i=1
while i<=rows:
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    i+=1
    print("")