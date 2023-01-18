import time
import random

def banner():
    print("######################################################")
    print("             WELCOME TO THE PORT QUIZZER")
    print("######################################################")
    
def gameplay_rules():
    print()
    print("The goal is to memorize the common port numbers and services associated with those ports.")
    print("You can retake the quiz as many times as you want, but questions will not be in the same order each time.")
    print("After you finish the quiz you will be told how many answers you got right, and how fast you completed it in.")

question_list = ["FTP", "SSH", "SFTP", "Telnet", "SMTP", "DNS", "DHCP", "TFTP", "HTTP",
                 "POP3", "NTP", "NetBIOS", "IMAP", "SNMP", "LDAP", "HTTPS", "SMB", "Syslog",
                 "SMTP TLS", "LDAPS", "IMAP over SSL", "POP3 over SSL", "SQL Server Protocol",
                 "SQLnet Protocol", "MySQL", "RDP", "SIP"]

answer_list = [ [20, 21], 22, 22, 23, 25, 53, [67,68], 69, 80, 110, 123, 139, 143, 161, 389,
                443, 445, 514, 587, 636, 993, 995, 1433, 1521, 3306, 3389, [5060, 5061]]

banner()
gameplay_rules()

# create an infinite while loop in case user wants to 
# go through cards multiple times
while True:
    # shuffle the lists around after each round so it's not predictable
    temp = list(zip(question_list, answer_list))
    random.shuffle(temp)
    question_list, answer_list = zip(*temp)
    question_list, answer_list = list(question_list), list(answer_list)
    
    # start timer for the user
    time_start = time.time()
    correct_answers = 0
    print()
    # use enumerate to make it easier to keep track of current list count
    for count, question in enumerate(question_list):
        # ask the user a question and for their answer
        print(f"Question {count+1}/{len(question_list)}: {question}")
        
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
    total_time = end_time - time_start
    
    # get the time in minutes and seconds as integers
    time_in_minutes = total_time // 60
    time_in_seconds = int(total_time % 60)
    
    # get the time in milliseconds as a float 
    # convert the value to a string and then format it so only that leading numbers aren't showing
    time_in_milliseconds = (total_time % 60) % 1
    time_in_milliseconds = str(f"{time_in_milliseconds:.2f}")
    time_in_milliseconds = time_in_milliseconds[2:]
    
    # number of correct and wrong answers
    print(f"Your score was {correct_answers}/{len(question_list)} or {correct_answers/len(question_list):.2f}%")
    print(f"Time spent answering questions: {int(time_in_minutes)}:{time_in_seconds:02d}:{time_in_milliseconds}")
    # ask the user if they would like to quit or go again
    exit_prompt = input("Press q to exit. Enter to continue: ")
    
    if exit_prompt.lower() == "q":
        break
    
