#UNLIKE LISTS TUPLES ARE NOT MUTUABLE(thats the only difference)
t=(1,2,3,4,True,"Ali","Sarah")
print(type(t)) 

#t=() //this is empty tuple
#SHOWING WE HAVE A TUPLE W ONLI ONE ELEMENT
a=(1,)
print(type(a))#elif only 1 written wuld print type as integer

cnt=t.count(2)
print(cnt)#prints number of occurances in tuple

ind=t.index("Ali")
print(ind)#tells index

#CONCATENATING 2 TUPLE
concat=a+t
print(concat)

#REPEATED VALUES
rep=a*3
print(rep)

#CHECKING IF ELEMENT EXIST IN TUPLE OR NOT
print(1 in a)#should return true

#LENGTH OF TUPLE
print(len(t))

#FINDING MAX and MIN
s=(78,22,3,34)
print(max(s))
print(min(s))