task = input("Enter your task: ")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:",task,"is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(task,"is a high priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time_bound aspect")
    case "medium":
        if time_bound == "yes":
            print("Reminder:",task,"is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(task,"is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Invalid time_bound aspect")
        
    case "low":
        print("Note:",task,"is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Please enter a valid priority (high/medium/low).")
