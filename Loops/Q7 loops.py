#Print multiplication table in reverse
n=int(input("Enter number: "))

for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")