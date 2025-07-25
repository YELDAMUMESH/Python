#Using while loop
rows=5
while rows>0:
    print("*"*rows)
    rows-=1

print("\n")

#Using for loop
r=5
for i in range(0,r):
    print("*"*(r-i))
print("\n")

#For loop
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)
