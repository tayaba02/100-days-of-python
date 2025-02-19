print("Welcome to Treasure Island \n"
      "Your mission is to find the treasure ")
direction = input("Where do you want to go? left or right ")
if direction == "left":
    nextstep = input("Do you want to swim or wait? ")
    if nextstep == "wait" or not "SWIM":
        whichdoor = input("which door? ")
        if whichdoor == "Yellow":
            print("You win!")
        elif whichdoor =="Red":
            print("Burned by fire, Gameover!")
        elif whichdoor == "Blue":
            print("Eaten by beast game over")
        else:
            print("Game over!")
    elif nextstep == "swim" or not "wait":
        print("Attack by trout Gameover!")
elif direction == "Right":
    print("Fall into hole, Gameover")
else:
    print("Game over")
