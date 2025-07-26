from datetime import datetime,timedelta

def display_current_datetime():
    return datetime.now()

current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

number_of_days = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date():
    return current_date + timedelta(days=number_of_days)

future_date = calculate_future_date()

print(f"Future date: {future_date}")
