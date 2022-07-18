from cProfile import run
from concurrent.futures import thread
from crypt import methods
import email, smtplib, ssl
from json.tool import main
from email.message import EmailMessage
import threading
import time 
from datetime import datetime
from tracemalloc import start 
import email, smtplib, ssl
from email.message import EmailMessage
import time 
from datetime import datetime

#################################

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



def look_up_gateway(gate_way):
    gate_way = {'AirFire Mobile': "@sms.airfiremobile.com", 'Aio Wireless': "@mms.aiowireless.net", 
    'Alaska Communications': "@msg.acsalaska.com", 'Alltel (Allied Wireless)' : "@mms.alltelwireless.com", 'Verizon': "@vzwpix.com.",
    "Assurance Wireless": "@vmobl.com", "AT&T": "@mms.att.net", "BellSouth": "@bellsouth.cl", "Bluegrass Cellular": "@mms.myblueworks.com",
    'Bluesky Communications': "@psms.bluesky.as", 'Boost mobile': "@myboostmobile.com", 'CellCom': "@cellcom.quiktxt.com", 'Cellular South':"@csouth1.com",
    'Centennial Wireless': "@cwemail.com", 'Chariton Valley Wireless': "@sms.cvalley.net", 'Chat Mobility': "@mail.msgsender.com",
    'Cincinnati Bell': "@mms.gocbw.com", 'Cleartalk': "@sms.cleartalk.us", 'Cricket': "@mms.cricketwireless.net", 'C Spire Wireless': "@cspire1.com", 
    'Edge Wireless': "@sms.edgewireless.com", 'Element Mobile': "@SMS.elementmobile.net", 'General Communications Inc.': "@mobile.gci.net", 
    'Golden State Cellular': "@gscsms.com", 'GreatCall': "@vtxt.com", 'MetroPCS': "@mymetropcs.com", 'Pocket Wireless': "@sms.pocket.com", 'Red Pocket Mobile':"@vtext.com"}   
    key = input('What carrier do you use: ')
    if key in gate_way:
      return gate_way[key]
    else:
      print("Sorry, carrier not found.")

#######################################
class Remind:
    def __init__(self, summary, full_text, chosen_time, reminder_sent):
        self.summary = summary
        self.full_text = full_text
        self.chosen_time = chosen_time
        self.reminder_sent = reminder_sent

    def summary(self):
        print("What do you want to be reminded of: ")

    def full_text(self):
        self.full_text = str(input("Enter your reminder: "))
   
    def chosen_time(self):
        self.chosen_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
        validate = valid_time(self.chosen_time.lower())
        if validate != "valid":
            print(validate)
        else:
            print(f"Setting reminder for {self.chosen_time}...")

    def reminder_sent(self):
        self.reminder_sent = False


##########################################

class User:
    def __init__(self, name, phone_number, phone_carrier, phone_gateway, data_list=None):
        self.name = name
        self.phone_number = phone_number
        self.phone_carrier = phone_carrier
        self.phone_gateway = phone_gateway
        if data_list is None:
            self.data_list = dict()
        else:
            self.data_list = data_list
   
    def user_greet(self):
        self.name = input("Hello, what is your name: ?")
        self.phone_number = input("What is your phone number: ")
        self.phone_carrier = input("What carrier do you use (ex. Cricket): ?") #to search and get correct gateway
        self.phone_gateway = look_up_gateway(self.phone_carrier)
        if self.phone_carrier in look_up_gateway:
         return look_up_gateway[self.phone_carrier]
        else:
            print("Sorry, carrier not found.")
        for key, value in dict().items(): 
            return('Number: {}, carrier: {}'.format(key+value)) 

    def user_info(self):
        #this is so the message goes to your phone number (could also use your email), and is associated with your name 
        self.data_list = input('Enter name followed by phone number separated by ":" ') 
        temp = self.data_list.split(':') 
        self.data_list[temp[0]] = int(temp[1]) 
        #Displays the dictionary:
        for key, value in self.data_list.items(): 
            return('Name: {}, Number: {}'.format(key, value)) 


#####################################
class RunReminderApp(User, Remind):
    def __init__(self, user, reminder_collector, reminder_monitor, main):
        self.user = user
        self.reminder_collector = reminder_collector
        self.reminder_monitor = reminder_monitor
        self.main = main
    
    def user_greet(self):
        self.user = User()
        self.user.user_greet()
        return self.user_greet
    add = "yes"
    

    def reminder_collector(self):
        
        self.reminder_collector = Remind 
        self.data_list = dict()
        while add == "yes":
            print(self.reminder_collector.summary())
            print(self.reminder_collector.full_text)
            reminder_time = (input("At what time enter in 'HH:MM:SS AM/PM' (ex: 12:20:13 PM) format: "))
            valid = valid_time(reminder_time.lower())
        if valid != "valid":     #used to ensure the time input works 
            print(valid)
        else:
            print(f"Setting reminder at {reminder_time}...")
            temp = self.data_list.split(':') 
            self.data_list[temp[0]] = int(temp[1])  
            for key, value in self.data_list.items(): 
                return('Reminder: {}, time: {}'.format(key, value)) 
            add = input("Is there anything else you'd like to be reminded(yes/no)?: ")
            #self.data_list = {self.reminder_collector : reminder_time}
        
        if add == "no":
            print("Ok got it!")
            return self.reminder_collector


    def reminder_monitor(self):
        alarm_hour = reminder_time[0:2]
        alarm_min = reminder_time[3:5]
        alarm_sec = reminder_time[6:8]
        alarm_period = reminder_time[9:].upper()

        for reminder_time in self.user.data_list:

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
                            if __name__ == '__main__':   
                             email_alert("Its reminder time", "It is time for: " + self.reminder_collector.full_text, self.phone_number + self.phone_carrier)
                            if email_alert == True:
                                    return email_alert

    def main(self):

        if __name__ == '__main__':
            Thread1= threading.Thread(target=self.user_greet)
            Thread2= threading.Thread(target=self.reminder_collector)
            Thread3= threading.Thread(target=email_alert)

            Thread1.start()
            Thread2.start()
            Thread3.start()

            Thread1.join()
            Thread2.join()
            Thread3.join()
        main(self)

        #methods(staticmethod)
        #RunReminderApp.user_greet(self.user_greet)
       # RunReminderApp.reminder_collector(self.reminder_collector)
        #RunReminderApp.reminder_monitor(email_alert)
        #if __name__ == '__main__':
       #     main(self)
