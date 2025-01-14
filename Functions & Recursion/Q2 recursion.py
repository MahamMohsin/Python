#PRINT INVERTED RIGHT ANGLED TRIANGLE

def pattern(n):
    if(n==0):
        return
    else:
        print("*" * n)
        pattern(n-1)#ek decrement krke print krtay jao
    
    
n=int(input("Enter the number of rows: "))
pattern(n)