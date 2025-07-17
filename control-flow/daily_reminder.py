task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f" '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f" '{task}' is a {priority} priority task that not requires immediate attention, but should be done today!")
        else:
            print('Sorry I can not handle your input')

    case 'medium':
        if time_bound == 'yes':
            print(f" '{task}' is a {priority} priority task that requires attention, but not required to be done today!")
        elif time_bound == 'no':
            print(f" '{task}' is a {priority} priority task that not requires immediate attention, but you can consider it anytime this week!")
        else:
            print('Sorry I can not handle your input')
    case 'low':
        if time_bound == 'yes':
            print(f" '{task}' is a {priority} priority task that requires attention, may be in free time this week !")
        elif time_bound == 'no':
            print(f" '{task}' is a {priority} priority task not requires attention, you can consider it any time you want!")
        else:
            print('Sorry I can not handle your input')
    case _ : 
        print('Sorry I can not handle your input')        

