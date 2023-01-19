import flashcards

def banner():
    print("######################################################")
    print("             WELCOME TO THE PORT QUIZZER")
    print("######################################################")
    
def menu_choice():
    print("#1: Flashcards Quiz")
    print("#2: Ports And Services Information")
    print("#3: Scoreboard")
    print("#4: Exit Application")
    choice = int(input("Please enter a number: "))
    
    return choice   
    
# show the user the welcome banner and gameplay rules
banner()

while True:
    user_choice = menu_choice()
    print()
    
    match user_choice:
        case 1:
            flashcards.start_game()
        case 2:
            print("work on 2")
        case 3:
            print("work on 3")
        case 4:
            print("Thank you for using Port Quizzer!")
            break
        case _:
            print("Choose a number between 1 and 4")
    # add whitespace between answers
    print()
    
    
