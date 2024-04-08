import random

def start():
    print("Welcome to this game!")
    print("You are on a deserted island. Choose what to do:")
    print("1. Find a shelter to live")
    print("2. Search for food")
    print("3. Attempt to swim to another island")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        find_shelter()
    elif choice == '2':
        find_food()
    elif choice == '3':
        try_to_swim()
    elif choice == '4':
        print("Goodbye! Thanks for trying.")
        exit()
    else:
        print("Invalid choice. Please try again.")
        start()

def find_shelter():
    print("You decided to find a shelter.")
    print("You come across a cave and a treehouse.")
    print("1. Explore the cave")
    print("2. Climb up to the treehouse")
    print("3. Go back")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        explore_cave()
    elif choice == '2':
        climb_treehouse()
    elif choice == '3':
        start()
    else:
        print("Invalid choice. Please try again.")
        find_shelter()

def explore_cave():
    print("You enter the cave and find it dark and damp.")
    print("You see some faint light ahead.")
    print("1. Keep going towards the light")
    print("2. Go back to find another shelter")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        print("You find a hidden chamber with a stash of supplies!")
        print("Congratulations! You have found shelter and supplies.")
        print("You survive and win the game!")
        exit()
    elif choice == '2':
        find_shelter()
    else:
        print("Invalid choice. Please try again.")
        explore_cave()

def climb_treehouse():
    print("You climb up to the treehouse.")
    print("It seems sturdy and safe.")
    print("You decide to stay there for the night.")
    print("The next morning, you feel rested and ready to explore further.")
    start()

def find_food():
    print("You decided to search for food.")
    print("You see a forest and a beach nearby.")
    print("1. Explore the forest for fruits and nuts")
    print("2. Go fishing at the beach")
    print("3. Go back")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        explore_forest()
    elif choice == '2':
        go_fishing()
    elif choice == '3':
        start()
    else:
        print("Invalid choice. Please try again.")
        find_food()

def explore_forest():
    print("You explore the forest and find some berries and nuts.")
    print("But you also encounter a wild animal!")
    print("1. Try to fight the animal")
    print("2. Run away")
    print("3. Try to befriend the animal")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print("You manage to defeat the animal and collect more food.")
            start()
        else:
            print("The animal overpowers you. Game over!")
            exit()
    elif choice == '2':
        print("You manage to escape from the animal.")
        start()
    elif choice == '3':
        print("You try to befriend the animal, but it doesn't work.")
        explore_forest()
    else:
        print("Invalid choice. Please try again.")
        explore_forest()

def go_fishing():
    print("You go fishing at the beach.")
    print("After some time, you catch some fish.")
    print("You cook them and have a delicious meal.")
    start()

def try_to_swim():
    print("You decided to attempt to swim to another island.")
    print("It's a risky move, as the currents are strong.")
    print("1. Go for it!")
    print("2. Reconsider")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        outcome = random.choice(["success", "fail"])
        if outcome == "success":
            print("You reach another island and find rescue!")
            print("Congratulations! You survived and won the game!")
            exit()
        else:
            print("The currents are too strong. You drown. Game over!")
            exit()
    elif choice == '2':
        start()
    else:
        print("Invalid choice. Please try again.")
        try_to_swim()

start()
