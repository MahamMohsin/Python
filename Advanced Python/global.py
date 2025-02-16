#CHANGING GLOBAL VAR WITHIN FUNCTION

a=10

def test():
    global a
    a=1
    print(a)
    

print(a)#bec fuction is not run yet to change global ki value 
test()
print(a)