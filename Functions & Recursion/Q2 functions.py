#CONVERT DEGREE CELSIUS TO FAHRENHEIT
#C/5=(F-32)/9

def conversion(c):
    f=((c*9)/5)+32
    return f
    
c=int(input("Enter temperature in degree celcius: "))
print(f"Temperature in fahrenheit is: {conversion(c)}F")
