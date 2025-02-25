print("Welcome to Treasure Island \n"
      "Your mission is to find the treasure.")

direction = input("Where do you want to go? left or right? ").lower()

if direction == "left":
    nextstep = input("Do you want to swim or wait? ").lower()
    
    if nextstep == "wait":
        whichdoor = input("Which door? Red, Blue, or Yellow? ").lower()
        
        if whichdoor == "yellow":
            print("You Win!")
        elif whichdoor == "red":
            print("Burned by fire. Game Over!")
        elif whichdoor == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    elif nextstep == "swim":
        print("Attacked by trout. Game Over!")
    else:
        print("Invalid choice. Game Over!")

elif direction == "right":
    print("Fell into a hole. Game Over!")

else:
    print("Invalid choice. Game Over!")
