import time
import shuffle_lists
import quiz_time

def start_game(question_list, answer_list, quiz_choice):

    # Copying list to give users a list of answers to choose from
    menu_choice = answer_list.copy()

    while True:
        question_list, answer_list = shuffle_lists.shuffle_quiz(question_list, answer_list)
        
        # start timer for the user
        time_start = time.time()
        correct_answers = 0

        # use enumerate to make it easier to keep track of current list count
        for count, question in enumerate(question_list):
            # ask the user a question and ask for their answer
            print(f"Question {count+1}/{len(question_list)}: {question}")
            
            # this is where answers will be checked based on quiz chosen by the user.
            # the memory quiz is where the user enters in a number without a list of numbers to choose from
            # whereas the menu quiz is where the user will have a list of choices to help them out.
            match quiz_choice:
                case 1:
                    correct_answers += memory_quiz(answer_list, count)
                case 3:
                   correct_answers += menu_quiz(menu_choice, answer_list, count)
                case 4:
                    correct_answers += menu_quiz(menu_choice, answer_list, count)
                case 5:
                    correct_answers += menu_quiz(menu_choice, answer_list, count)
                case 6:
                    correct_answers += menu_quiz(menu_choice, answer_list, count)
                case _:
                    break
            
            # get the end time to tell how long user took to answer questions
        end_time = time.time()
        
        # get the minutes, seconds, and milliseconds from time
        minutes, seconds, milliseconds = quiz_time.quiz_timer(time_start, end_time)
        
        # get user score percentage
        percent_score = (correct_answers/len(question_list))*100
        percent_score = int(percent_score)
        
        # number of correct and wrong answers
        print(f"Your score was {correct_answers}/{len(question_list)} or {percent_score}%")
        print(f"Time spent answering questions: {int(minutes)}:{seconds:02d}:{milliseconds}")
        # ask the user if they would like to quit or go again
        exit_prompt = input("Press q to exit. Enter to continue: ")
        
        if exit_prompt.lower() == "q":
            break

def memory_quiz(answer_list, count):
    # if user enters wrong value then just assign 0 and move on to next question
    print()
    try:
        answer = int(input("Enter port number: "))
    except ValueError as e:
        answer = 0
            
    # check if the current value in answer_list is of type list
    # if it is of type list, then simply check if answer is in that specific list,
    # otherwise check if value is equal to current list value
    if isinstance(answer_list[count], list):
        if answer in answer_list[count]:
            print(f"You are correct! The port numbers are: {answer_list[count]}")
            print()
            return 1
        else:
            print(f"Sorry, the real answer was {answer_list[count]}")
            print()
            return 0
    else:
        if answer == answer_list[count]:
            print(f"You are correct! The port numbers are: {answer_list[count]}")
            print()
            return 1
        else:
            print(f"Sorry, the real answer was {answer_list[count]}")
            print()
            return 0
                
def menu_quiz(menu_choice, answer_list, count):
    # give the user a list of choices
            for c, i in enumerate(menu_choice):
                print(f"#{c+1}: {i}")
            
            print()
             # if user enters wrong value then just assign 0 and move on to next question
            try:
                answer = int(input(f"Enter a number between 1 and {len(menu_choice)}: "))
                
                # check if answer is out of bounds
                if answer < 1 or answer > len(menu_choice):
                    answer = 0
            except ValueError as e:
                answer = 0
                
            # take their guess and subtract one for the right index
            if menu_choice[answer-1] == answer_list[count]:
                print(f"You are correct! The answer was: {answer_list[count]}")
                print()
                return 1
            else:
                print(f"Sorry, the real answer was: {answer_list[count]}")
                print()
                return 0
            