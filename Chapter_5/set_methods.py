# sets : Sets are unordered collections of unique elements this means that a set cannot contain duplicate values
# 1. Unordered: Elements in sets have no specific order you cannot access elements using indexes
# 2. Unique: Duplicate elements are automatically removed
# 3. Mutable: We can add and remove the elements
# 4. Hasable elements: The elements in a set must be immutable data types such as strings,numbers,tuples
#    lists and dictionaries cannot be elements of set


my_set={1,2,3,4}

name_set=set("Umesh") # Set creation using set()
print(name_set)

empty=set()           # Empty set creation 
print(empty)

#Membership Testing
print(1 in my_set)    # checks whether 1 is present in set or not
print(6 in my_set)

#Basic set operations

#1. add(element)- Adds element to the set
my_set.add(5)         
print(my_set)

#2. remove(element)- Removes element form the set. Raises key error if element is not present in the set
my_set.remove(5)
print(my_set)

#3. discard(element)- Removes element form the set. Does not raise key error if element is not present in the set
my_set.discard(1)
print(my_set)
print(my_set.discard(5)) # No error

my_set={1,2,3,4,5,6} #Updating the set elements

#4. pop()- Removes random element from the set
print(my_set.pop())
print(my_set)

#5. copy()- returns a shallow copy of the set
copy_set=my_set.copy()
print(copy_set)

#6. union(other_set) or | - Returns a new set containing all the elements form the set1 and set2
set1={1,2,3}
set2={3,4,5}
union1=set1.union(set2)
print(union1)

union2=set1 | set2
print(union2)

#7. intersection(other_set) or & - Returns a new set containing common elements
intersection1=set1.intersection(set2)
print(intersection1)

intersection2=set1 & set2
print(intersection2)

#8. difference(other_set) or - operator: Returns a new set containing the elements that are in the set
# but not in the other set
differnce=set1.difference(set2)
print(differnce)

#9. symemetric_difference() or ^ operator: Returns a new set containing elements 
# that are in either the set or other set but not in both
symmetric=set1.symmetric_difference(set2)
print(symmetric)

#10. isdisjoint(): Returns true if the set has no common elements with other set,false otherwise
print(set1.isdisjoint(set2))

#11. issubset() or <= operator: Returns true if all elements of the set are also present in the other set,false otherwise
print(set1.issubset(set2))

#12. issuperset() or >= operator: Return true if the set contains all elements of the other set,false otherwise
print(set1.issuperset(set2))

#13. clear()- completely clears or empties the set
set1.clear()
set2.clear()
print(set1,set2)


#UPDATE METHODS: (Modifies the original set)

#1. update() or |= : Adds element form other sets to the set, similar to union but modifies the original set
old={1,2,3,4,5,5,5,5}
new={6,7,8,9,10,10,10,1,2}
old.update(new)
print(old)

#2. intersection_update() or &= : Keeps only the common elements form the sets
old.intersection_update(new)
print(old)

#3. differnce_update() or -= : Removes elements form the set that are also in other sets
old.difference_update(new)
print(old)

#4. symmetric_difference_update() or ^= :Keeps elements that are in either the set or the other set but not both
old.symmetric_difference_update(new)
print(old)

