#there are a number of logs in the system, each log is a string 
#Have to write a script that parses the logs and counts how many total actions each user took.
#final output should be a single dictionary looking like this: {'user_1': 3, 'user_2': 2, 'user_3': 1}
#concepts used:
# string manipulation, dictionaries, loops, conditionals

#these are the logs that we will be parsing
logs = [
    "user_1|2026-06-23 09:00:00|home_page",
    "user_2|2026-06-23 09:01:22|dashboard",
    "user_1|2026-06-23 09:05:00|checkout",
    "user_3|2026-06-23 09:10:11|home_page",
    "user_2|2026-06-23 09:15:00|logout",
    "user_1|2026-06-23 09:20:00|logout"
]

#these final output should be a single dictionary looking like this: {'user_1': 3, 'user_2': 2, 'user_3': 1}.final output should be a single dictionary 
# looking like this: {'user_1': 3, 'user_2': 2, 'user_3': 1}.

action_counts = {} #create an empty dictionary to store the counts 

for log in logs: #iterate through each log in the logs list
    user, timestamp, action = log.split('|') #split the log string into user, timestamp, and action 
    if user in action_counts: #check if the user is already in the dictionary
        action_counts[user] += 1 #if the user is already in the dictionary, increment their count by 1
    else:
        action_counts[user] = 1 #if the user is not in the dictionary, add them with a count of 1       
    
    print(action_counts) #print the final dictionary with user action count
