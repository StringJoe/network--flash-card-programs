import flashcards
import read_file

def banner():
    print("######################################################")
    print("             WELCOME TO THE PORT QUIZZER")
    print("######################################################")
    
def menu_choice():
    print("#1: Port Number Quiz")
    print("#2: Ports Number Information")
    print("#3: 802.11 Standards Quiz")
    print("#4 Cable Quiz")
    print("#5: Exit Application")
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
            read_file.service_info()
        case 3:
            print("working on wireless standard quiz")
        case 4:
            print("Working on cables quiz")
        case 5:
            print("Thank you for using Port Quizzer!")
            break
        case _:
            print("Choose a number between 1 and 4")
    # add whitespace between answers
    print()
    
    
