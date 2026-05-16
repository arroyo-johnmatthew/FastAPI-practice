import random

# one live bullet in a gun
gun = 6
trigger = [0, 1]

while True:
    choice = input("Fire a bullet? yes/no: ").lower()

    if choice in ["no", "n"]:
        print("Goodbye!")
        break

    elif choice in ["yes", "y"]:
        result = random.choice(trigger)

        # checks if the bullet fired is real
        if result == 1:
            print("YOU ARE D E A D")
            break
    
        else:
            pass