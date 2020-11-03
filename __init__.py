from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import os.path
import json
import RPi.GPIO as GPIO
import time
from datetime import datetime

class SnacksCalorieTracker(MycroftSkill):

    @intent_handler(IntentBuilder('SnackingIntent')
                    .require('SnackKeyword'))

    def handle_snacking_intent(self, message):

        filename = os.path.expanduser("~/test/Calorie_Master.json")
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        counter= os.path.expanduser("~/test/Counter.json")
        usr_message = message.data.get('utterance')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

        with open(filename) as f:
            data = json.load(f)
        for data_set in data.get("Items", {}):
            _extract = data_set.get("name", None)

            if _extract.upper() in usr_message.upper():
                choice = data_set.get("choice", None)
                info = data_set.get("Info", None)
                calorie = data_set.get("Calorie", None)
                if choice == "bad":
                    print("LED on Orange")
                    GPIO.output(23, GPIO.HIGH)
                    time.sleep(5)
                    print("LED off")
                    GPIO.output(23, GPIO.LOW)
                    self.speak("Ok Avyan " + info + " has "+ calorie + " bad calories and sugar in it, which will make you restless .")
                    self.speak_dialog("WarnCalorie", expect_response=True)

                    break

                if choice == "good":

                    print("LED on Green")
                    GPIO.output(18, GPIO.HIGH)
                    time.sleep(2)
                    print("LED off")
                    GPIO.output(18, GPIO.LOW)
                    self.speak("Ok Avyan" + info + " has "+ calorie + " good calories in it, so")
                    self.speak_dialog("WellDoneMessage")

                    with open(counter) as json_file:
                        data = json.load(json_file)
                        data['counter_healthy'] = int(data['counter_healthy']) + int("1")
                        data['last_updated'] = today = datetime.today().__str__()
                        with open(counter, 'w') as f:
                            json.dump(data, f, indent=4)

                       # python object to be appended
                    with open(tracker) as tracker_file:
                            dataw = json.load(tracker_file)
                            item = data['Snacks']
                            today = datetime.today().__str__()
                            y = {
                                "snack": _extract.upper(),
                                "quantity": "1",
                                "choice": "good",
                                "consumed": calorie,
                                "date and time": today

                            }
                            item.append(y)

                    with open(tracker, 'w') as f:
                            json.dump(dataw, f, indent=4)

                    break


    @intent_handler(IntentBuilder('DeclineAdviceIntent').require('DeclineKeyword'))
    def handle_decline_intent(self, message):

        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("TrackSnacksAdvice", expect_response=True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        filename = os.path.expanduser("~/test/Calorie_Master.json")
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        counter = os.path.expanduser("~/test/Counter.json")
        usr_message = message.data.get('utterance')

        with open(filename) as f:
            data = json.load(f)

            for data_set in data.get("Items", {}):
                _extract = data_set.get("name", None)

                if _extract.upper() in usr_message.upper():
                    with open(counter) as tracker_file:
                        data = json.load(tracker_file)
                        data['counter_unhealthy'] = int(data['counter_unhealthy']) + int("1")
                        data['last_updated'] = today = datetime.today().__str__()
                        with open(counter, 'w') as f:
                            json.dump(data, f, indent=4)

                    # python object to be appended
                    with open(tracker) as json_file:
                        dataw = json.load(json_file)
                        item = data['Snacks']
                        today = datetime.today().__str__()
                        y = {
                            "snack": _extract.upper(),
                            "quantity": "1",
                            "choice": "bad",
                            "consumed": calorie,
                            "date and time": today

                        }
                        item.append(y)

                    with open(tracker, 'w') as f:
                        json.dump(dataw, f, indent=4)

                    break




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


def stop(self):
        pass

def create_skill():
    return SnacksCalorieTracker()