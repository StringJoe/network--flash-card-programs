def quiz_timer(start, stop):
    total_time = stop - start
        
    # get the time in minutes and seconds as integers
    time_in_minutes = total_time // 60
    time_in_seconds = int(total_time % 60)
        
    # get the time in milliseconds as a float 
    # convert the value to a string and then format it so only that leading numbers aren't showing
    time_in_milliseconds = (total_time % 60) % 1
    time_in_milliseconds = str(f"{time_in_milliseconds:.2f}")
    time_in_milliseconds = time_in_milliseconds[2:]
    
    return time_in_minutes, time_in_seconds, time_in_milliseconds