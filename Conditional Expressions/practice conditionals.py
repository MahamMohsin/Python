#Write a program to find greatest of 4 nums entered by user

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
d=int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("The greatest num is",a)
elif(b>a and b>c and b>d):
    print("The greatest num is",b)
elif(c>a and c>b and c>d):
    print("The greatest num is",c)
else:
    print("The greatest num is",d)