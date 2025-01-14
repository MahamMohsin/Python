#SNAKE WATER GUN GAME
'''Rules:
Snake:
Drinks water (wins against Water).
Gets shot by the gun (loses to Gun).

Water:
Douses the gun (wins against Gun).
Gets drunk by the snake (loses to Snake).

Gun:
Shoots the snake (wins against Snake).
Gets doused by water (loses to Water)'''

import random #for generating random numbers as a choice for computer
from colorama import Fore,init #for colourful output
init(autoreset=True) #to reset the colour to normal after each print statement

gameDict={
    "snake":1,
    "water":2,
    "gun":3
}

DisplayDict={
    1:"Snake",
    2:"Water",
    3:"Gun"
}

computer=random.choice([1,2,3])

user=input("\t\tEnter your choice: ")
you=gameDict[user] #to get in number format
# By now we have computer's choice and user's choice

print(f"Computer's choice: {DisplayDict[computer]} \t\t Your choice: {DisplayDict[you]}")

if(computer==you):
    print(Fore.RED + "\t\t  IT'S A DRAW")
    
else: 
    if(computer==1 and you==2):
        print(Fore.YELLOW + "\t\t  COMPUTER WON!")#as snake drinks water
    
    elif(computer==2 and you==1):
       print(Fore.GREEN + "\t\t  YOU WIN!") 
    
    elif(computer==1 and you==3):
       print(Fore.GREEN + "\t\t  YOU WIN!")#as gun shoots snake   
        
    elif(computer==3 and you==1):
        print(Fore.YELLOW + "\t\t  COMPUTER WON!")
        
    elif(computer==2 and you==3):
        print(Fore.YELLOW + "\t\t  COMPUTER WON!")#as water douses gun
        
    elif(computer==3 and you==2):
       print(Fore.GREEN + "\t\t  YOU WIN!")
       
    else:
        print(Fore.RED + "\t\t  INVALID MOVE!")
        
        
print("\t\t  Thanks for playing!")