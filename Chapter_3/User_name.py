Name=input("Enter the name: ")
Date=input("Enter the date: ")
print("Hello,",Name,"Good afternoon")

#Using f string
print(f"Hello,{Name} Good morning")
print(f"Dear {Name},\nYou are selected!\n{Date}")

#Uisng replace function
Letter='''Dear <|Name|>,
You are selected!
<|Date|>'''
print((Letter.replace("<|Name|>",Name)).replace("<|Date|>",Date))
Example="Hello  World"
Position=Example.find("  ")
print(Position)
Example1=Example.replace("  "," ")
print(Example)
print(Example1)
