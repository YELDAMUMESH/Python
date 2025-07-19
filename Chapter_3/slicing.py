a=("Umamaheshwar")
length=len(a)
print("Length of string is:",length)
print("Printing by index")
print(a[0:12])
print(a[0:3])
print(a[3:12])
print(a[0:])
print(a[:12])

#-ve index
print("Printing by -ve index")
print(a[-12:])
print(a[:-1])

#skipping
print("Printing by skipping")
print(a[0:12:1])
print(a[0:12:2])
print(a[0:12:3])