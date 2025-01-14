#WRITE RECURSIVE FUNCTION TO PRINT SUM OF FIRST N NATURAL NUMBERS

#sum of 1 is 1
#sum(n-1)+n is the logic

def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
    

n=int(input("Enter the number: "))
print(sum(n))