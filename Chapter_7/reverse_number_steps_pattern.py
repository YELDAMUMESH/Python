
""" 

1
21
321
4321
54321

"""

rows=int(input("Enter no.of rows: "))

#Using for loop:
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
print("\n")

#Using while loop:
i=1
while i<=rows:
    j=i
    while j<=i and j>0:
        print(j,end="")
        j-=1
    print()
    i+=1