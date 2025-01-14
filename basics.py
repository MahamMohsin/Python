a=1
b=3
print("Sum:",a+b)

e=None #nothing (none type variable)

#rules of variables
#can start with @ or digit

#comparison operators always boolean
d=5<4
print(d)

#assignment
b+=3
print(b)

e=True or False
print(e)

print(not(True))

#type casting
g=31
g=type(g)
print(g)

f=31.5
f=type(f)
print(f)#<class float>

m="maham"
m=type(m)
print(m)#<class str>

r="34.5"
s=float(r) #r but the type should be float
j=type(s)
print(j)

#taking input in python
#setting type as int else would consider it as string and conctenate it when summing
v = int(input("Enter num: "))
print("Number is: ",v)

w=int(input("Enter num2: "))
print("Sum: ",v+w)

#escape sequence
strr="My name is maham\nI study in FAST\tNU"
print(strr)

print("Maham\t\"mohsin\"")