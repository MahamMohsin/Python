#WRITE A FUNCTION TO REMOVE A GIVEN WORD FROM LIST AND STRIP IT AT SAME TIME

def remover(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["Maham","Rohan","Harry","Sarah","Manaal"]

print(remover(l,"Ma"))
