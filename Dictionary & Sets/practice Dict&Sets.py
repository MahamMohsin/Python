#create a dict of urdu words w their eng translation
words={"Waqt":"Time",
       "Insaan":"Human",
       "Cheez":"Thing",
       "Zaroori":"Important"}

word=input("Enter the word you want meaning of: ")
print(words[word])

#input 5 numbers from user and display all unique nums
s=set()
n=int(input("Enter number: "))
s.add(n)

n=int(input("Enter number: "))
s.add(n)

n=int(input("Enter number: "))
s.add(n)

n=int(input("Enter number: "))
s.add(n)

n=int(input("Enter number: "))
s.add(n)
print(s)

#A NUMBER CAN BE WRITTEN AS A STRING AND AN INTEGER BOTH
s.add(18)
s.add("18")
print(s)

print(len(s))
s.add(18.0)
print(len(s))#would display the same length as above as in python same val so len not counted 18==18.0

#CREATE AN EMPTY DICT AND ALLOW 2 USERS TO ENTER THEIR FAV PROGRAMMING LANGUAGE
d={}

name=input("Enter name: ")
lang=input("Enter language: ")
d.update({name:lang})

name=input("Enter name: ")
lang=input("Enter language: ")
d.update({name:lang})

print(d)
#if the name of 2 ppl same the update key would jus update prev value corresponding to the key
#as dups not allowed in dict

#VALUES INSIDE A LIST CANNOT BE CHANGED WHICH IS IN A SET
#as list cant be included in a set firstly
#secondly you cant change values thro indexing in sets

