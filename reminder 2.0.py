import email, smtplib, ssl
import re
from email.message import EmailMessage
import time 
from datetime import datetime
#################################
#test I'll separate into the main classes
def email_alert(subject,body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "reminderbot975@gmail.com"
    msg['from'] = user
    password = "wnbpnfqsnhmgmahs"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

#will use this function to make sure the time the user inputs is valid, otherwise it'll have them type in a valid time. Will be checking for 'HH:MM:SS format:
def valid_input(reminder_time):
  if len(reminder_time) != 11:
    return " "
  else:
      if int(reminder_time[0:2]) > 12:  #checks initial length of statement incase user wrote too much, after it checks it'll go on to else
          return "Invalid HOUR input! please retype"
      elif int(reminder_time[3:5]) > 59:
          return "Invalid MINUTE input! please retype"
      elif int(reminder_time[6:8]) > 59:
          return "Invalid SECOND input! please retype"
      else:
          return "valid"
##################################
add = "yes"
reminderlist = []
print("What should I remind you: ")
text = str(input(""))
reminderlist.append(text)
reminder_time = (input("At what time enter in 'HH:MM:SS AM/PM' (ex: 12:20:13 PM) format: "))
add = input("Is there anything else you'd like to be reminded(yes/no)?: ")

while add == "yes":
    print("What should I remind you:")
    text = str(input(""))
    reminderlist.append(text)
    reminder_time = (input("At what time enter in 'HH:MM:SS AM/PM' (ex: 12:20:13 PM) format: "))
    valid = valid_input(reminder_time.lower())
    if valid != "valid":
      print(valid)
    else:
      print(f"Setting reminder at {reminder_time}...")
      break
    add = input("Is there anything else you'd like to be reminded(yes/no)?: ")

alarm_hour = reminder_time[0:2]
alarm_min = reminder_time[3:5]
alarm_sec = reminder_time[6:8]
alarm_cycle = reminder_time[9:].upper()

if add == "no":
    print("Ok got it!")
  
while True:
    present = datetime.now()
    current_hour = present.strftime("%I")
    current_min = present.strftime("%M")
    current_sec = present.strftime("%S")
    current_cycle = present.strftime("%p")

    if reminder_time == current_cycle:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Time for " + text)
    if __name__ == '__main__':   
      email_alert("Its reminder time", "It is time for: " + text, "6504507443@mms.cricketwireless.net")
      break
#this will slice and separate the time inputted


#next variable is to get current datetime to know when to send




#last part is where the message goes to,interchangeable with a email as well. 
##If you use a phone number follow with the carrier gateway domain.

