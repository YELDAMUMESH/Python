#length of the string

a="hello World"
length=len(a)
print("Length of the string is: ",length)

#Ends with function: This function returns true if the string ends with the specified value.
print(a.endswith("d"))

#starts with function: This function returns true if the string starts with the specified value.
print(a.startswith("H"))

#Replace: returns a copy of the string with all occurrences of a substring replaced with another substring
print(a.replace("World", "Universe"))

#Find: returns the index of the first occurrence of the specified value
print(a.find("World"))

#count: counts the number of occurrences of a substring in the string
print(a.count("o"))

#Capiatalize: returns a copy of the string with the first character capitalized
print(a.capitalize())