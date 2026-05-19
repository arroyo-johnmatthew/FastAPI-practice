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
        pygame.mixer.music.load('hobby-projects/russian_roulette/gun_spins.mp3')
        pygame.mixer.music.play()
        shot = random.choice(chamber)

        # wait for a few seconds before firing the gun
        time.sleep(1)

        if shot == 1:
            # plays a sound effect of a gun firing
            pygame.mixer.music.load('hobby-projects/russian_roulette/gun_fires.mp3')
            pygame.mixer.music.play()

            print("💀 You are Dead 💀\n")
            # wait for 1 second before ending the program to make sure the sound is heard
            time.sleep(1)
            break

        else:
            pygame.mixer.music.load('hobby-projects/russian_roulette/gun_clicks.mp3')
            pygame.mixer.music.play()
            
            print("You survived the shot 😰\n")
            continue