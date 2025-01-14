#CREATING A FUNCTION FOR TAKING OUT AVG OF 3 NUMS

#function defination
def avg():
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    c=int(input("Enter number 3: "))
    
    average=(a+b+c)/3
    print(f"{average:.2f}")#will print to 2 decimal place
    print(round(average,2))#same as above
    

#calling function
avg()

#end=" " will print the output in same line 
print("KEEP GOING",end=" ")
print("Maham!")