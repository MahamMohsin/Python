#FIND GREATEST OF 3 NUMBERS USING FUNCTIONS

def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))

print(f"The greatest number is {greatest(a,b,c)}")

