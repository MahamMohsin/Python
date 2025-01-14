#factorial(n)=n*factorial(n-1)

def fact(n):
    if(n==0 or n==1):
        return 1 #since factorial of 1 and 0 both 1
    
    else:
        return n*fact(n-1)
    

num=int(input("Enter number: "))
#result=fact(num)
# print(f"Factorial of {num} is {result}")
print(f"Factorial of {num} is {fact(num)}")

