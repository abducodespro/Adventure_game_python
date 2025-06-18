import time

# Introduction
print("Welcome to the Adventure Quest!")
name = input("What is your name, brave traveler? ")
print(f"Greetings, {name}! Your journey begins now...\n")
time.sleep(1)

health = 100

want_to_play = input("Do you want to start your quest? (yes/no): ").lower()

if want_to_play in ['yes', 'y']:
    print("Great! Let's begin your adventure...")
    time.sleep(1)

    direction = input("You find yourself at a crossroad. Do you go left or right? (left/right): ").lower()

    if direction == "left":
        print("You head left into a dark forest.")
        time.sleep(1)
        action = input("A wild wolf appears! Do you fight or run? (fight/run): ").lower()

        if action == "fight":
            print("You bravely fight the wolf and win, but you're injured.")
            health -= 30
            print(f"Your health is now {health}.")
        elif action == "run":
            print("You escape safely but fall into a thorn bush.")
            health -= 20
            print(f"Your health is now {health}.")
        else:
            print("You hesitate... the wolf attacks! You lose 50 health.")
            health -= 50
            print(f"Your health is now {health}.")

        if health <= 0:
            print("You have died from your injuries. Game over!")
        else:
            print("You continue and find a lake ahead.")
            choice = input("Do you swim across or look for a bridge? (swim/bridge): ").lower()

            if choice == "swim":
                print("You try to swim but are eaten by crocodiles. Game over!")
            elif choice == "bridge":
                print("You cross the bridge safely and find a treasure chest. You win!")
            else:
                print("Indecision costs you dearly. A snake bites you. Game over.")

    elif direction == "right":
        print("You head right and enter a mysterious cave.")
        time.sleep(1)
        torch = input("Do you pick up a torch before entering? (yes/no): ").lower()

        if torch == "yes":
            print("Good move. You can see the path clearly.")
        else:
            print("It's too dark! You fall into a pit. Lose 40 health.")
            health -= 40
            if health <= 0:
                print("You died from the fall. Game over!")
                exit()

        print("Inside the cave, you see two tunnels: one glows red, the other blue.")
        tunnel = input("Which tunnel do you take? (red/blue): ").lower()

        if tunnel == "red":
            print("You walk into a dragon's lair. Burned to ashes. Game over!")
        elif tunnel == "blue":
            print("You find ancient ruins with magical artifacts. You win!")
        else:
            print("You get lost and never come out... Game over.")
    else:
        print("Wrong direction. You fall into a trap. Game over.")

else:
    print("Maybe next time. Goodbye!")
