import random

# one live bullet in a gun
gun = 6
trigger = [0, 1]

while True:
    choice = input("Fire a bullet? yes/no: ").lower()
    print("")

    if choice in ["no", "n"]:
        print("Goodbye!")
        break

    elif choice in ["yes", "y"]:
        result = random.choice(trigger)

        # checks if there are still bullets inside the gun
        if gun == 0:
            print("You are now safe. The gun is empty")
            break

        # checks if the bullet fired is real
        elif result == 1:
            print("YOU ARE D E A D")
            break
    
        else:
            print("You are not dead")
            # subtract the remaining bullets
            gun -= 1
            print(f"gun now {gun}\n")