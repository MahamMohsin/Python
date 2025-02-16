#walrus operator officially called assignment operator
#allows you to assign values to variables as part of expression
# :=

if(n := len([1,2,3,4,5])) >3:
    print(f"List is too long ({n} elements eventho <= 3 expected)")
    #n ko assign hojayega len 
    
#defining types
#n: int=10
#n: str="Maham"
""""
def sum(a: int,v: int) ->int:
   return a+v
"""
#union tells either

#match status same as switch case
def match_status(status):
    match status:
        case 0:
            return "invalid"
        case 1:
            return "valid"
        case _:
            return "default"
        
print(match_status(int(input("Enter status: "))))
