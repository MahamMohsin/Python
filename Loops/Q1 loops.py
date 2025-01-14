#print multiplication table of a number using for loop
n=int(input("Enter number: "))

for i in range(1,11):
    #f strring allows usage of variables within
    print(f"{n} x {i} = {n*i}")