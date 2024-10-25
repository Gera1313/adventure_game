# start the game

def intro():
    print("Welcome to the Mystic Forest!")
    print("Your mission is to find the hidden treasure and escape safely.")
    print("Make your choices wisely as danger lurks at every turn!")
    print("Let's begin the adventure...\n")

def wizard_encounter():

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
        first_choice()

# calls the intro function to display messages
intro()
first_choice()