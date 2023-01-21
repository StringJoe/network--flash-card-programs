import time
import shuffle_lists
import quiz_time

def start_game():
    question_list =["Frequency 5 Ghz, Bandwidth 54 Mbps", "Frequency 2.4 Ghz, Bandwidth 11Mbps",
                "Frequency 2.4Ghz, Bandwidth 54Mbps", "Frequency 2.4 and 5GHz, Bandwidth 150/600Mbps (MIMO)",
                "Frequency 5GHz, Bandwidth 3Gbps (MU-MIMO)", "Frequency 2.4, 5 and 6 GHz, Bandwidth 9.6Gbps (MU-MIMO)"]

    answer_list = ["a", "b", "g", "n", "ac", "ax"]

    menu_choice = answer_list.copy()

    while True:
        question_list, answer_list = shuffle_lists.shuffle_quiz(question_list, answer_list)
        
        # start timer for the user
        time_start = time.time()
        correct_answers = 0
        print()
        # use enumerate to make it easier to keep track of current list count
        for count, question in enumerate(question_list):
            # ask the user a question and ask for their answer
            print(f"Question {count+1}/{len(question_list)}: {question}")
            
            # give the user a list of choices
            for c, i in enumerate(menu_choice):
                print(f"#{c+1}: 802.11{i}")
            
             # if user enters wrong value then just assign 0 and move on to next question
            try:
                answer = int(input("Enter a number between 1 and 6: "))
            except ValueError as e:
                answer = 0
                
            # take their guess and subtract one for the right index
            if menu_choice[answer-1] == answer_list[count]:
                    print(f"You are correct! The standard was: 802.11{answer_list[count]}")
                    correct_answers += 1
            else:
                print(f"Sorry, the real answer was 802.11{answer_list[count]}")
            print()
            
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
#start_game()
