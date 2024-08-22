import datetime

def log_activity(activity):
    #to log an activity or operation
    with open('library.log', 'a') as file:
        file.write(f"{datetime.datetime.now()}: {activity}\n")
