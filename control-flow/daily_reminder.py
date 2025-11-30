# daily_reminder.py
# This program gives a personal reminder based on priority and time sensitivity.

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Print the customized reminder directly
if time_bound == "yes":
    print(f"Reminder: {base_message} that requires immediate attention today!")
else:
    print(f"Reminder: Note: {base_message}. Consider completing it when you have free time.")
