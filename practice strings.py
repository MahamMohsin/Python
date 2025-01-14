#print a user entered name followed by god afternoon
name=input("Enter your name: ")
# print("Good afternoon")
# print(name)
#using f string
print(f"Good Afternoon {name}")
#or
print("Good afternoon "+name+" ")


#replacing name with you name and date with original date
letter="""Dear name,
you are selected!
date"""

print(letter.replace("name","Maham").replace("date","8 January 2027"))


#detecting double space in a string
strr="  gotta workk"
print(strr.find("  "))

