from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import os.path
import json
import RPi.GPIO as GPIO
import time
from mycroft.util import play_wav
from datetime import datetime
from twilio.rest import Client
from mycroft.audio import wait_while_speaking
import smtplib

class SnacksCalorieTracker(MycroftSkill):

    @intent_handler(IntentBuilder('SnackingIntent')
                    .require('SnackKeyword'))

    def handle_snacking_intent(self, message):

     #Set Json files to read
        filename = os.path.expanduser("~/test/Calorie_Master.json")
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        counter= os.path.expanduser("~/test/Counter.json")
    #Set GPIO Pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

        #Get the user message
        usr_message = message.data.get('utterance')
        # search for a snack name in user message
        with open(filename) as f:
            data = json.load(f)

            for data_set in data.get("Items", {}):
                _extract = data_set.get("name", None)
                print("executing for loop")
                choice = ""
                info =""
                calorie=""
                print("choice" + choice)

                if _extract.upper() in usr_message.upper():
                 # find out details about the snack
                    choice = data_set.get("choice", None)
                    info = data_set.get("Info", None)
                    calorie = data_set.get("Calorie", None)
                    print("choice" + choice)


                    # if snack choice is unhealthy
                    if choice == "bad":
                            print("Signal unhealthy snack")
                            #Lit Red LED
                            GPIO.output(23, GPIO.HIGH)
                            #Give more info about unhealthy snack to reconsider choice
                            self.speak("Ok Avyan, Let me warn you " + info + calorie + " bad calories and sugar in it, which will make you restless .")
                            self.speak_dialog("WarnCalorie", expect_response=True, wait=True)
                            # Wait for response to see if choice is changed
                            #reconsider_choice = self.ask_yesno("WarnCalorie")
                            # Update unhealthy counter by 1
                            with open(counter) as json_file:
                               data = json.load(json_file)
                               current_unhealthy_counter = str(data['counter_unhealthy'])
                            #Update unhealthy counter
                            if int(current_unhealthy_counter) >= 4:
                                # the following line needs your Twilio Account SID and Auth Token
                                client = Client("AC429a4c06f04eb36287f1c2a682c90a2a", "2d7e4dc79393ccbbd8d4827d076fa24c")
                                # change the "from_" number to your Twilio number and the "to" number
                                # to the phone number you signed up for Twilio with, or upgrade your
                                # account to send SMS to any phone number
                                client.messages.create(to="+12012400693", from_ = "+16267095806", body = "Alert - Avyan is eating way too much unhealthy snack today!")
                                # start - finish sms

                            # Add entry in Daily snack tracker for unhealthy snack intent
                            with open(tracker) as tracker_file:
                               dataw = json.load(tracker_file)
                               item = dataw['Snacks']
                               today = datetime.today().__str__()

                               y = {
                                                    "snack": _extract.upper(),
                                                    "quantity": "1",
                                                    "choice": "bad",
                                                    "consumed": calorie,
                                                    "date and time": today

                                    }
                               item.append(y)

                            with open(tracker, 'w') as trackerf:
                                    json.dump(dataw, trackerf, indent=4)
                                    print("Made an unhealthy food entry for " +_extract + " in the tracker" )

                        # if snack choice is healthy
                    if choice == "good":
                             #Lit the green signal for healthy snacking
                            print("Lit the green signal and switch off red signal for healthy snacking")
                            GPIO.output(23, GPIO.LOW)
                            GPIO.output(18, GPIO.HIGH)
                            #Encourage good choice
                            self.speak("Ok Avyan " + info + calorie + " good calories in it, so you have made a healthy choice, Let me mark it")
                            #Update counter of healthy snacking
                            with open(counter) as json_file:
                                data = json.load(json_file)
                                data['counter_healthy'] = int(data['counter_healthy']) + int("1")

                            with open(counter, 'w') as cf:
                                json.dump(data, cf, indent=4)
                                print("Increased the healthy counter by 1 ")

                            # Add new entry for  healthy snacking
                            with open(tracker) as tracker_file:
                                dataw = json.load(tracker_file)
                                item = dataw['Snacks']
                                today = datetime.today().__str__()
                                y = {
                                                    "snack": _extract.upper(),
                                                    "quantity": "1",
                                                    "choice": "good",
                                                    "consumed": calorie,
                                                    "date and time": today

                                    }
                                item.append(y)

                            with open(tracker, 'w') as tf:
                                json.dump(dataw, tf, indent=4)
                                self.speak("All done")
                                print("Made an healthy food entry for " + _extract + "in the tracker")

                            break

    @intent_handler(IntentBuilder('DeclineAdviceIntent').require('DeclineKeyword'))
    def handle_decline_intent(self, message):

        counter= os.path.expanduser("~/test/Counter.json")

        self.speak("Ok, not a great choice, but let me make an entry")
        with open(counter) as json_file:
            data = json.load(json_file)
            data['counter_unhealthy'] = int(data['counter_unhealthy']) + int("1")
            current_unhealthy_counter = str(data['counter_unhealthy'])
            # Update unhealthy counter
        with open(counter, 'w') as counterf:
            json.dump(data, counterf, indent=4)
            print("Increased the unhealthy counter by 1 ")
            self.speak("Today you have eaten " + current_unhealthy_counter + "unhealthy snacks")

    @intent_handler(IntentBuilder('ListeningIntent')
                    .require('ListenKeyword'))
    def handle_listen_to_advice_intent(self, message):
        GPIO.output(23, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        wavfile = os.path.expanduser("~/hello.wav")
        play_wav(wavfile)

    @intent_handler(IntentBuilder('HappyBirthdayIntent')
                        .require('HappyBirthdayKeyword'))
    def handle_happy_birthday_intent(self, message):
            self.speak("A very very happy birthday to Avyan")
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18, GPIO.OUT)
            GPIO.setup(23, GPIO.OUT)
            GPIO.output(23, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(18, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)

    @intent_handler(IntentBuilder('SendEmailIntent')
                    .require('SendEmailKeyword'))
    def handle_send_email_intent(self, message):
        # Email Variables
        SMTP_SERVER = 'smtp.gmail.com'  # Email Server (don't change!)
        SMTP_PORT = 587  # Server Port (don't change!)
        GMAIL_USERNAME = 'mycroftashi@gmail.com'  # change this to match your gmail account
        GMAIL_PASSWORD = 'mycroft1983'  # change this to match your gmail password

        #Getting counter to send Summary
        counter = os.path.expanduser("~/test/Counter.json")
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        with open(counter) as json_file:
            data = json.load(json_file)
            healthysnack = data['counter_healthy']
            unhealthysnack = data['counter_unhealthy']

        with open(tracker) as tracker_file:
                dataw = json.load(tracker_file)
                item = dataw['Snacks']


        print("sending email now")
       
        sendTo = 'mycroftashi@gmail.com'
        emailSubject = "Avyan's Snack Report, Healthy Snack:" + healthysnack + " Unhealthy Snack:" + unhealthysnack
        emailContent = "This is the summary of Avyan's snack history today" + item


            # Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + emailSubject, "To: " + sendTo,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        # Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        # Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        self.speak("Sending an email now with today's snacking report for Avyan")
        # Send Email & Exit
        session.sendmail(GMAIL_USERNAME, sendTo, headers + "\r\n\r\n" + emailContent)
        session.quit



def stop(self):
        pass

def create_skill():
    return SnacksCalorieTracker()