import random
import time
import pygame

pygame.mixer.init()

# one live bullet in a gun
chamber = [0, 0, 0, 0, 0, 1]

while True:
    choice = input("🔫 Fire a bullet? yes/no: ").lower()
    print("")
    
    if choice in ["no", "n"]:
        print("Goodbye!\n")
        break

    elif choice in ["yes", "y"]:
        # spins the chamber before getting a bullet
        shot = random.choice(chamber)

        if shot == 1:
            # plays a sound effect of a gun firing
            pygame.mixer.music.load('hobby-projects/russian_roulette/gun_fires.mp3')
            pygame.mixer.music.play()

            print("💀 You are Dead 💀\n")
            continue
        else:
            print("You survived the shot 😰\n")
            continue