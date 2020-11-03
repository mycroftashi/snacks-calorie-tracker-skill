from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import os.path
import json
import RPi.GPIO as GPIO
import time
import date

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
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        snack = "none"
        usr_message = message.data.get('utterance')

        with open(filename) as f:
            data = json.load(f)
        for data_set in data.get("Items", {}):
            _extract = data_set.get("name", None)

            if _extract.upper() in usr_message.upper():
                choice = data_set.get("choice", None)
                info = data_set.get("Info", None)
                calorie = data_set.get("Calorie", None)
                if choice == "bad":
                    self.speak("Ok Avyan " + info + " has "+ calorie + " bad calories and sugar in it, which will make you restless .")
                    self.speak_dialog("WarnCalorie", expect_response=True)
                    print("LED on Orange")
                    GPIO.output(23, GPIO.HIGH)
                    time.sleep(5)
                    print("LED off")
                    GPIO.output(23, GPIO.LOW)
                    break
                if choice == "good":
                    self.speak("Ok Avyan" + info + " has "+ calorie + " good calories in it, so it is a healthy choice .")
                    self.speak_dialog("WellDoneMessage")
                    tracker = os.path.expanduser("~/test/DailySnackTracker.json")
                    with open(tracker) as json_file:
                        dataw = json.load(json_file)
                        counter = dataw['Counter']
                        today = date.today()
                        counter["count_healthy"] = counter.get("count_healthy") + 1
                        counter["date and time"] = today
                        with open(tracker, 'w') as f:
                            json.dump(counter, f, indent=4)
                    print("LED on Green")
                    GPIO.output(18, GPIO.HIGH)
                    time.sleep(5)
                    print("LED off")
                    GPIO.output(18, GPIO.LOW)
                    break


    @intent_handler(IntentBuilder('DeclineAdviceIntent').require('DeclineKeyword'))
    def handle_decline_intent(self, message):

        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("TrackSnacksAdvice", expect_response=True)
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        with open(tracker) as json_file:
            dataw = json.load(json_file)

            item = dataw['Snacks']
            counter = dataw['Counter']
            today = date.today()
            usr_message = message.data.get('utterance')

            with open(filename) as f:
                data = json.load(f)

            for data_set in data.get("Items", {}):
                _extract = data_set.get("name", None)

                if _extract.upper() in usr_message.upper():
                    snack = _extract
                    # python object to be appended
                    y = {
                                "snack": snack,
                                "quantity": "1",
                                 "choice" : "bad",
                                "consumed": "95",
                                "date and time": today

                         }
                    item.append(y)
                    counter["count_unhealthy"] = counter.get("count_unhealthy") + 1
                    counter["date and time"] = today
                    with open(tracker, 'w') as f:
                        json.dump(dataw, f, indent=4)
                        json.dump(counter, f, indent=4)


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
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        with open(tracker) as json_file:

            dataw = json.load(json_file)
            counter = dataw['Counter']
            today = date.today()
            counter["count_healthy"] = counter.get("count_healthy") + 1
            counter["date and time"] = today
            with open(tracker, 'w') as f:
                json.dump(counter, f, indent=4)


def stop(self):
        pass

def create_skill():
    return SnacksCalorieTracker()