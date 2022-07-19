import email, smtplib, ssl
from email.message import EmailMessage
import time 
from datetime import datetime

################################################################################
def look_up_gateway():
    gate_way = {'AirFire Mobile': "number@sms.airfiremobile.com", 'Aio Wireless': "number@mms.aiowireless.net", 
    'Alaska Communications': "number@msg.acsalaska.com", 'Alltel (Allied Wireless)' : "number@mms.alltelwireless.com", 'Verizon': "number@vzwpix.com.",
    "Assurance Wireless": "number@vmobl.com", "AT&T": "number@mms.att.net", "BellSouth": "number@bellsouth.cl", "Bluegrass Cellular": "number@mms.myblueworks.com",
    'Bluesky Communications': "number@psms.bluesky.as", 'Boost mobile': "number@myboostmobile.com", 'CellCom': "number@cellcom.quiktxt.com", 'Cellular South':"number@csouth1.com",
    'Centennial Wireless': "number@cwemail.com", 'Chariton Valley Wireless': "number@sms.cvalley.net", 'Chat Mobility': "number@mail.msgsender.com",
    'Cincinnati Bell': "number@mms.gocbw.com", 'Cleartalk': "number@sms.cleartalk.us", 'Cricket': "number@mms.cricketwireless.net", 'C Spire Wireless': "number@cspire1.com", 
    'Edge Wireless': "number@sms.edgewireless.com", 'Element Mobile': "number@SMS.elementmobile.net", 'General Communications Inc.': "number@mobile.gci.net", 
    'Golden State Cellular': "number@gscsms.com", 'GreatCall': "number@vtxt.com", 'MetroPCS': "number@mymetropcs.com", 'Pocket Wireless': "number@sms.pocket.com", 'Red Pocket Mobile':"number@vtext.com"}   
    key = input('What carrier do you use: ')
    if key in gate_way:
      return gate_way[key]
    else:
      print("Sorry, carrier not found.")

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

#used to ensure a working value is entered, when setting the time wanted for reminder
def valid_time(reminder_time):
    if len(reminder_time) != 11:
        return "Invalid time! Please try again..."
    else:
        if int(reminder_time[0:2]) > 12:
            return "Invalid HOUR! Please try again..."
        elif int(reminder_time[3:5]) > 59:
            return "Invalid MINUTE! Please try again..."
        elif int(reminder_time[6:8]) > 59:
            return "Invalid SECOND! Please try again..."
        else:
            return "valid"
    
##############################################################################################################
class Remind:
    def __init__(self, summary, full_text, chosen_time, reminder_sent):
        self.summary = summary
        self.full_text = full_text
        self.chosen_time = chosen_time
        self.reminder_sent = reminder_sent

    def summary(self):
        print("Hello, welcome to your reminder bot.\nHow it works:\nYou will be asked your phone number, followed by what phone carrier you use, which we'll use to assign the corresponding carrier gateway.\nAfter you'll be asked reminders you'd like to set, followed by what time you'd like them, you can set as many as you'd like.\nFinally sit back, and a message will be sent to your phone at the time you set your reminder at.  ")

    def full_text(self):
        self.full_text = str(input("What would you like to be reminded: "))
        email_alert("Its reminder time", "It is time for: " + self.full_text, "6504507443@mms.cricketwireless.net")
   
    def chosen_time(self):
        reminder_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
        validate = valid_time(reminder_time.lower())
        if validate != "valid":
            print(validate)
        else:
            print(f"Setting alarm for {reminder_time}...")

    def reminder_sent(self):
        self.reminder_sent = False
