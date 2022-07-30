# Harold Williams
# May 31, 2022
# This program presents a option with 4 possible states
# then tells the capital of their choice

from time import sleep



# Define the main function
def main():
    # Declare and initialize variables
    # Strings for name and menu choice
    userName = menuChoice= ""

    
    # Display Intro
    #print("Welcome To My State Selection Program")
    print("Wlecome To My State Selection Program".center(80,"*"))
    #print("*" *80)
    #print(f"{'Welcome To My State Selection Program':^80}")
    #print("*" *80)

    # Prompt for name
    userName = input("\nHello, what is your name?: ").capitalize()
    
    # Greet user name by name
    print(f"\nHello {userName}, lets play a game!")
    sleep(.5)
    
    # Display state options
    print("\n Please choose from the following menu: ")
    print("A) PA \nB) SC \nC) GA \nD) FL")
    
    # Prompt user for menuchoice
    menuChoice = input("\n Enter your choice here: ").upper()
    if menuChoice == "A":
        print("The capital of Pennsylvania is Harrisburg")
    elif menuChoice == "B":
        print("The capital of South Carolina is Columbia")
    elif menuChoice == "C":
        print("The capital of Georgia is Atlanta")
    elif menuChoice == "D":
        print("The capital of Florida is Tallahassee")
    else:
        print("Sorry, you must choose A, B, C, or D. Thank you!")
    sleep(.75)
    
    # Selection structure to determine which capital to display to user
    # Display outro
    print(f"Thank you {userName} for playing my game. See you again soon!")


# Call main function
main()
