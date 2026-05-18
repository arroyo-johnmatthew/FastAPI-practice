import random

# one live bullet in a gun
gun = 6
trigger = [0, 1]

while True:
    choice = input("🔫 Fire a bullet? yes/no: ").lower()
    print("")

    if choice in ["no", "n"]:
        print("Goodbye!")
        break

    elif choice in ["yes", "y"]:

        # checks if the gun that will be fired contains 1 bullet left 
        if gun == 1:
            print("🪦  You just killed yourself!")
            break

        result = random.choice(trigger)

        # checks if there are still bullets inside the gun
        if gun == 0:
            print("😁 You are now safe. The gun is empty")
            break

        # checks if the bullet fired is real
        elif result == 1:
            print("💀 YOU ARE DEAD 💀")
            break
    
        else:
            print("✅ You are not dead")
            # subtract the remaining bullets
            gun -= 1
            print(f"gun now {gun}\n")