rows=int(input("Enter no.of rows: "))

#Using for loop:
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

print("\n")

#Using while loop:
i=1
while i<=rows:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
        