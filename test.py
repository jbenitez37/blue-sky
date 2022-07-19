from datetime import datetime   #To set date and time
def validate_time(reminder_time):
    if len(reminder_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(reminder_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(reminder_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(reminder_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"

while True:
    reminder_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
    validate = validate_time(reminder_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {reminder_time}...")
        break

alarm_hour = reminder_time[0:2]
alarm_min = reminder_time[3:5]
alarm_sec = reminder_time[6:8]
alarm_period = reminder_time[9:].upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Reminder time")
                    break
