#PROGRAM TO FIND IF A NUMBER IS PRIME OR NOT
#prime number is only divisible by itself and 1

n=int(input("Enter number: "))

#as every number is divisible by 1
for i in range(2,n):
    if(n%i==0):
        print("NOT PRIME!")
        break #if condition of not prime met once simply break out of loop
    
else:
    print(f"{n} is PRIME!")