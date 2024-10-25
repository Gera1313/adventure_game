# start the game

def intro():
    print("Welcome to the Mystic Forest!")
    print("Your mission is to find the hidden treasure and escape safely.")
    print("Make your choices wisely as danger lurks at every turn!")
    print("Let's begin the adventure...\n")

def wizard_encounter():
    print("The wizard offers you a magical map to help guide you through the forest.")
    print("Do you accept the map? Type 'yes' or 'no'")
    choice = input("> ")
    if choice.lower() == "yes":
        print("You take the map and thank the wizard. It reveals a hidden path to the treasure!")
        # Add more logic here later for the hidden path encounter
    elif choice.lower() == "no":
        print("You politely decline. The wizard wishes you luck and disappears.")
        # Add more logic here later for the path without the map
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        wizard_encounter()  # Ask again

def first_choice():
    print("You see two paths. Do you go left or right?")
    choice = input("> ")
    if choice.lower() == "left":
        print("You encounter a friendly wizard who offers to help you.")
        # Add logic here for wizard encounter.
    elif choice.lower() == "right":
        print("A wild, ferocious bear blocks your path! Game Over.")
        # Add logic here for bear encounter.
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_choice() # Ask again

# calls the intro function to display messages
intro()
first_choice()