"""

ABCDE
BCD
CD
D
 
"""

rows=int(input("Enter no.of rows: "))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print("")
    
    
    
print("\n")


""" 

ABCD
ABC
AB
A

"""

for i in range(1,rows+1):
    for j in range(1,rows-i+2):
        print(chr(64+j),end="")
    print("")
    