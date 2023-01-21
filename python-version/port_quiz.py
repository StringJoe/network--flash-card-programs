import time
import shuffle_lists
import quiz_time

def start_game():
    
    question_list = ["FTP", "SSH", "SFTP", "Telnet", "SMTP", "DNS", "DHCP", "TFTP", "HTTP",
                 "POP3", "NTP", "NetBIOS", "IMAP", "SNMP", "LDAP", "HTTPS", "SMB", "Syslog",
                 "SMTP TLS", "LDAPS", "IMAP over SSL", "POP3 over SSL", "SQL Server Protocol",
                 "SQLnet Protocol", "MySQL", "RDP", "SIP"]

    answer_list = [ [20, 21], 22, 22, 23, 25, 53, [67,68], 69, 80, 110, 123, 139, 143, 161, 389,
                    443, 445, 514, 587, 636, 993, 995, 1433, 1521, 3306, 3389, [5060, 5061]]
    
    # create an infinite while loop in case user wants to 
    # go through cards multiple times
    while True:
        # shuffle the lists around after each round so it's not predictable
        question_list, answer_list = shuffle_lists.shuffle_quiz(question_list, answer_list)
        
        # start timer for the user
        time_start = time.time()
        correct_answers = 0
        print()
        # use enumerate to make it easier to keep track of current list count
        for count, question in enumerate(question_list):
            # ask the user a question and for their answer
            print(f"Question {count+1}/{len(question_list)}: {question}")
            
            # if user enters wrong value then just assign 0 and move on to next question
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
                    correct_answers += 1
                else:
                    print(f"Sorry, the real answer was {answer_list[count]}")
                print()
            else:
                if answer == answer_list[count]:
                    print(f"You are correct! The port numbers are: {answer_list[count]}")
                    correct_answers += 1
                else:
                    print(f"Sorry, the real answer was {answer_list[count]}")
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