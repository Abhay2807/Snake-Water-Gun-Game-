# Snake,Water And Gun GAME  

import random

def swg_game(comp,player):
    if comp == player:
        return None

    elif comp == "s":
        if player=="w":
            return False
        elif player=="g":
            return True

    elif comp == 'w':
        if player=="s":
            return True
        elif player=="g":
            return False

    else:                   #We can also write elif comp=="g"
        if player=="w":
            return True
        elif player=="s":
            return False


print("Comp Turn: Snake(s) Water(w) or Gun(g) ?")
rand_no=random.randint(1,3)

if rand_no == 1:
    Comp="s"
elif rand_no == 2:
    Comp="w"
else:                  #We can also write elif rand_no==3
    Comp="g"

player=input("Player's(Your) Turn: Snake(s) Water(w) or Gun(g) ?")

print(f"Computer chose {Comp}")
print(f"Player (you) chose {player}")
result= swg_game(Comp,player)
print(result)

if result == None:
    print("The game is a tie !!")
elif result == True:
    print("The player (you) win!!")
else:                                   #We can also write elif result==False
    print("The player (you) lose!!")
