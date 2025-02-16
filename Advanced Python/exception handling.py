#we dont want the program to crash when an error occurs

# try: written with except keyword
number =(int(input("Enter number: ")))
print(number)
    
number2=(int(input("Enter number2: ")))
print(number2)
    
division=number/number2
print(division)    
    
# except Exception as e:
#     print(e)

# except ZeroDivisionError:
#     print("Cannot divide by zero!")
if(number2==0):
    raise ZeroDivisionError("Zero divison error!")
else:
    print(division)
    
print("Program continues...")

#different types of exception includes:
ZeroDivisionError #when we try to divide a number by 0
TypeError #when we try to add string and integer 
ValueError #when we try to convert a string to integer but it is not a number
#we can handle multiple excceptions using exception as e
# or except: all other exceptions handled here
# except:

"""
try:
code that may raise an exception

except Exception as e:
code to handle the exception

else:
code to run if no exception raised

finally:
code that always runs (useful in functions)
"""