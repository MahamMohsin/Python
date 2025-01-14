#s={}//would create empty dictionary

#FOR MAKING EMPTY SET
s=set()

s={1,4,3,6,7,"Maham"}#in set repeatition doesnt matter
print(s)

print(s,type(s))
s.add("Mohsin")
print(s)

s.remove(4)
print(s)

#SETS ARE UNORDERED
#NO WAY TO CHANGE ITEMS N SETS
#SETS CANT HAVE DUP VALUES
#YOU CANNOT ACCESS ELEMENTS VIA INDEX

#methods
#LENGTH
u={1,2,3}
print(len(u))

#clear empties a set
s.clear()
print(s)#would display set()

#UNION IN SETS
s1={1,2,3,4}
s2={3,4,5,6,7,8}
print(s1.union(s2))

#INTERSECTION IN SETS
print(s1.intersection(s2))