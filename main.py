#Enxhi Merkaj 20/10/2023
#Team Assignment

#This program will prompt the user to choose between 9 options until the user chooses option 0.

#Create a lists of 10 different options
lists = [
    {"value": 1, "description": "Watch a movie!"},
    {"value": 2, "description": "Go to sleep."},
    {"value": 3, "description": "You should study."},
    {"value": 4, "description": "Go learn Python."},
    {"value": 5, "description": "Go out!"},
    {"value": 6, "description": "Maybe cook something."},
    {"value": 7, "description": "Choose another number."},
    {"value": 8, "description": "Call your friend."},
    {"value": 9, "description": "Learn Java"},
    {"value": 0, "description": "Exit the program"},
]

#Create a loop that will run until the user chooses 0
while True:

    # Get user input
    user_input = input("Select a choice from 1 - 9: ")
#Conver the input to integer
    try:
        choice = int(user_input)

#Execute if-else statement
        if choice in [option['value'] for option in lists]:
            if choice == 0:
                print("Exiting the program.")
                break
            else:
                print(f"You selected {choice}: {lists[choice-1]['description']}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# End of the program
