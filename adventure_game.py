# start the game
import random
inventory = []

def check_ending():
    if "Treasure Chest" in inventory:
        print("Congratulations, you found the hidden treasure and escaped safely with riches beyond your wildest dreams!")
    elif "Map" in inventory:
        print("Although you didn not find the treasure, you made it out of the forest safely thanks to the wizard’s map.")
    else:
        print("Lost in the forest with no map or treasure, you wander endlessly. Game Over.")
    
    # Ask if the player wants to restart
    choice = input("Would you like to play again? Type 'yes' or 'no' > ")
    if choice.lower() == 'yes':
        inventory.clear()  # Clear the inventory for a fresh start
        restart_game()  # Restart the game from the beginning
    else:
        print("Thanks for playing! Goodbye.")

def random_event():
    event = random.choice(["find_potion", "meet_ally", "nothing_happens"])
    if event == "find_potion":
        print("You find a healing potion on the ground and pick it up.")
        inventory.append("Potion")  # Add potion to inventory
    elif event == "meet_ally":
        print("A friendly creature appears and offers to guide you for a while.")
    else:
        print("Nothing unusual happens on your path.")

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
    if 'Map' in inventory:
        print("Using the map, you find a shortcut to the treasure!")
        print("After a short journey, you arrive at a treasure chest in a clearing.")
        
        # Adding a choice at the treasure
        choice = input("Do you open the chest or leave it? Type 'open' or 'leave' > ")
        if choice.lower() == "open":
            print("You open the chest and discover it's filled with gold and gems!")
            inventory.append("Treasure Chest")  # Add the treasure to the inventory
        elif choice.lower() == "leave":
            print("You decide to leave the chest and walk away, content with your journey.")
        else:
            print("Invalid choice. Please type 'open' or 'leave'.")
            hidden_path()  # Loop back for a valid choice

    else:
        print("Without a map, you wander aimlessly and eventually get lost.")

def wizard_encounter():
    print("The wizard offers you a magical map to help guide you through the forest.")
    choice = input("Do you accept the map? Type 'yes' or 'no' > ")
    if choice.lower() == "yes":
        print("You take the map and thank the wizard.")
        inventory.append('Map')  # Add map to inventory
    elif choice.lower() == "no":
        print("You politely decline. The wizard wishes you luck and disappears.")
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        wizard_encounter()  # Ask again if the input was invalid

def first_choice():
    print("You see two paths. Do you go left or right?")
    choice = input("> ")
    if choice.lower() == "left":
        wizard_encounter()  # Go to wizard encounter if player chooses left
        random_event()  # Trigger a random event after the wizard encounter
        hidden_path()  # Continue to hidden path after meeting the wizard
    elif choice.lower() == "right":
        print("A wild bear blocks your path! Game Over.")
        restart_game()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_choice()  # Ask again if the input was invalid

def intro():
    print("Welcome to the Mystic Forest!")
    print("Your mission is to find the hidden treasure and escape safely.")
    print("Make your choices wisely as danger lurks at every turn!")
    print("Let's begin the adventure...\n")


# calls the intro function to display messages
intro()
first_choice()