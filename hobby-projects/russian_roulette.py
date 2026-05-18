import random

# one live bullet in a gun
chamber = [0, 0, 0, 0, 0, 1]

# spins the chamber once (will spin again if the program runs again)
random.shuffle(chamber)

while True:
    choice = input("🔫 Fire a bullet? yes/no: ").lower()
    print("")

    if choice in ["no", "n"]:
        print("Goodbye!\n")
        break

    elif choice in ["yes", "y"]:
        # picks a bullet from the chamber
        bullet = random.randrange(len(chamber))
    
        # store it in a variable to check if the bullet fired is real or not
        shot = chamber.pop(bullet)

        if shot == 1:
            print("💀 You are Dead 💀\n")
            break
        else:
            print("You survived the shot 😰")
            print(f"bullets remaining: {len(chamber)}\n")
            continue