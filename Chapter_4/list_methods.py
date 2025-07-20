#playing with names

names=["Umesh","Nani","Jyothi","Pandu Rangam","Umesh"]
print(names)
print(names[0])
print(names[1])

names.append("Balraj") # Adds the string at the end of the list
print(names)

names.insert(0,"Sushila") # Inserts the string at index 0
print(names)

names.sort()              # Sort the list in alphabetical order
print(names)

names.reverse()           # Reverse the list
print(names)

family=names.copy()       # Copies the list 
print(family)

count=names.count("Umesh") # Counts the number of occurences
print(count)

family.clear()             # clears the complete list
print(family)

print(names.index("Nani")) # gives the index of the fist occurence

print(names.pop(1))        # removes element form the provided index 

names.append("Umesh")      # Adds string at the end of the list
print(names)

print(names.remove("Umesh")) # Removes element form the provided string
print(names)

family=["Shekar","Giri","Padma"]
names.extend(family)         # Used to extend the list
print(names)

names.sort(key=len)          # Used to sort the list by len of the strings
print(names)


#playing with numbers
numbers=[1,4,6,3,7,9,2,4,4]
numbers.insert(6,0)         # insterts the num at the given index
print(numbers)

numbers.append(2)           # Stores the num(2) at the end of the list
print(numbers)

numbers.sort()              # Sorts the list
print(numbers)

numbers.reverse()           # Reverse sorts the list
print(numbers)

numbers.pop()               # Pops the last element in the list
print(numbers)

print(numbers.count(4))     # Counts the no.of occurences
print(numbers)

print(numbers.index(2))     # Returns the first occurence of the element
num=[10,12,11,13]

numbers.extend(num)         # Extends the existing list
print(numbers)

num.clear()                 # Clears the list
print(num)

