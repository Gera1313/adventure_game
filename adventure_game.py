# start the game

def intro():
    print("Welcome to the Mystic Forest!")
    print("Your mission is to find the hidden treasure and escape safely.")
    print("Make your choices wisely as danger lurks at every turn!")
    print("Let's begin the adventure...\n")

def restart_game():
    print("\nWould you like to play again? Type 'yes' or 'no'")
    choice = input("> ")
    if choice.lower() == "yes":
        print("\nStarting a new adventure!\n")
        intro()
        first_choice()
    elif choice.lower() == "no":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        restart_game()  # Ask again

def hidden_path():
    print("You follow the hidden path revealed by the magical map.")
    print("After a while, you arrive at a mysterious cave. Do you enter the cave or continue along the path?")
    choice = input("> ")
    if choice.lower() == "enter":
        print("Inside the cave, you discover a treasure chest filled with gold! Congratulations, you found the treasure!")
        print("You win!")
        restart_game()
    elif choice.lower() == "continue":
        print("You continue along the path, but it leads to a cliff with no way down. Game Over.")
        restart_game()
    else:
        print("Invalid choice. Please type 'enter' or 'continue'.")
        hidden_path()  # Ask again

def wizard_encounter():
    print("The wizard offers you a magical map to help guide you through the forest.")
    print("Do you accept the map? Type 'yes' or 'no'")
    choice = input("> ")
    if choice.lower() == "yes":
        print("You take the map and thank the wizard. It reveals a hidden path to the treasure!")
        hidden_path()
    elif choice.lower() == "no":
        print("You politely decline. The wizard wishes you luck and disappears.")
        print("You continue your journey but quickly find yourself lost. Game Over.")
        restart_game()
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        wizard_encounter()  # Ask again

def first_choice():
    print("You see two paths. Do you go left or right?")
    choice = input("> ")
    if choice.lower() == "left":
        wizard_encounter() # Goes to wizard encounter if "left"
    elif choice.lower() == "right":
        print("A wild, ferocious bear blocks your path! Game Over.")
        restart_game()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_choice() # Ask again

# calls the intro function to display messages
intro()
first_choice()