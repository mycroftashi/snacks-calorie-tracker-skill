from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import os.path
import json
import RPi.GPIO as GPIO
import time

class SnacksCalorieTracker(MycroftSkill):

    @intent_handler(IntentBuilder('SnackingIntent')
                    .require('SnackKeyword'))
    def handle_snacking_intent(self, message):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        print("LED on Orange")
        GPIO.output(23, GPIO.HIGH)
        filename = os.path.expanduser("~/test/Calorie_Master.json")
        snack = "none"
        usr_message = message.data.get('utterance')

        with open(filename) as f:
            data = json.load(f)
        for data_set in data.get("Items", {}):
            _extract = data_set.get("name", None)

            if _extract.upper() in usr_message.upper():
                snack =  data_set.get("Calorie", None)
                self.speak("Ok Avyan" + _extract + "has"+ snack + "calories and a lot of sugar in it, which will make you restless. Are you sure you want to eat it ?")
                break
            else:
                self.speak_dialog("WarnCalorie")


        #self.speak_dialog("WarnCalorie" + snack, expect_response=True)
        time.sleep(5)
        print("LED off")
        GPIO.output(23, GPIO.LOW)

    @intent_handler(IntentBuilder('DeclineAdviceIntent').require('DeclineKeyword'))
    def handle_decline_intent(self, message):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        print("LED on Orange")
        GPIO.output(23, GPIO.HIGH)
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("TrackSnacksAdvice", expect_response=True)
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        with open(tracker) as json_file:
            dataw = json.load(json_file)

            temp = dataw['Snacks']

            # python object to be appended
            y = {"snack": 'Chewy Bar',
                 "quantity": "1",
                 "consumed": "900"
                 }


            temp.append(y)

            with open(tracker, 'w') as f:
                json.dump(dataw, f, indent=4)

            time.sleep(10)
            print("LED off")
            GPIO.output(23, GPIO.LOW)


    @intent_handler(IntentBuilder('ListeningIntent')
                    .require('ListenKeyword'))
    def handle_listen_to_advice_intent(self, message):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        print("LED on Green")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(10)
        print("LED off")
        GPIO.output(18, GPIO.LOW)


        self.speak_dialog("WellDoneMessage")


    def stop(self):
        pass

def create_skill():
    return SnacksCalorieTracker()