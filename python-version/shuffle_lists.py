import random

def shuffle_quiz(questions, answers):
    # zip the two lists together
    temp = list(zip(questions, answers))
    
    # shuffle the combined version of the lists
    # so that each index is shuffled with each other
    random.shuffle(temp)
    
    # unzip the shuffled lists into two tuples
    question_list, answer_list = zip(*temp)
    
    # convert each tuple back to a list when returning values
    return list(question_list), list(answer_list)