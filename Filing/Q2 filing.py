#MAKE A GAME FUNCTION FOR A GAME IN WHICH IF HIGH SCORE IS LESS THAN CURRENT SCORE THAN UPDATE YOUR SCORE IN FILE
import random

def game():
    print("Welcome to the game")
    score=random.randint(1,100) 
    #FETCHING HIGHSCORE FROM FILE
    with open("highscore.txt") as f:
        hscore=f.read()
        if (hscore!=""):
            hscore=int(hscore)#getting highscore in int
        else:
            hscore=0
        print(f"Your current score is {score}")
        print(f"High score is {hscore}")
        if(score>hscore):
            with open("highscore.txt","w") as f:
                f.write(str(score))
                
game()
                