# Dictionary: Are collection of key: value pairs. 
# Where keyes are immutable however values associated with the keys are mutable
# created as dic_name={key: value,....}

my_dict={"Name":"Umesh","Age":24,"City":"Hyd"}

print(my_dict.keys())                     # keys()-Displays keys 
print(my_dict.values())                   # values()-Display values of the keys

print(my_dict.items())                    # items()- Displays complete dictionary

version1={"Occupation": "Engineer"}             
my_dict.update(version1)                  # update()- Updates the already existing dic with new key: value pairs
print(my_dict)
my_dict.update({"Pay":4.0})
print(my_dict)
my_dict.update({"Pay":5.0})               # Can be also used to over write the already existing values of the keys
print(my_dict)
my_dict["Age"]=25
my_dict["Gender"]="Male"
print(my_dict)

my_copy=my_dict.copy()                    # copy()- Returns a shallow copy of the dict
print(my_copy)

my_dict.setdefault("Status","Single")     # setdefault(key,value)- Set's default value if the key is present if not add's
print(my_dict)                            # both key and value to the dict

my_basket= dict({"Mangoes": 2,"Apples":4,"Banana":6}) # dict({key: value,...}) - We can also create dit using this approach
print(my_basket)

print(my_basket["Mangoes"])                           # We can access values by using key names - dict_name[Key]

print(my_basket.get("Apples"))                        # get(key) - Used to access the value of the key

del my_copy["Pay"]                                    # del dict_name[Key] - Used to delete the key: value pair
print(my_copy)

my_copy.update({"Pay":5.0})
print(my_copy)

print(my_copy.pop("Pay"))                             # pop(key)- Used to remove key: value pair this also returns
print(my_copy)                                        # value of the key poped

print(my_copy.popitem())                              # popitem()- used to remove the last added key: value pair 
print(my_copy)                                        # returns the key: value pair which is removed

my_copy.clear()                                       # clear()- Clears complete dict
print(my_copy)