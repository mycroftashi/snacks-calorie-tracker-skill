from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.skills.context import adds_context, removes_context
import os.path
import json

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):

        MycroftSkill.__init__(self)

    @intent_handler('InformAboutEating').require('I am eating')
    def warn_about_snacks(self, message):
        self.speak_dialog('WarnCalorie')


    @intent_handler('IgnoreWarning').require('I am eating').require('Yes I do ')
    def track_snacks_eating(self, message):
        self.speak_dialog('TrackSnacksAdvice')
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        filename = os.path.expanduser("~/test/Calorie_Master.json")
        with open(filename) as f:
           data = json.load(f)

        # Output: {'name': 'Chewy Bar', 'Calorie': 500 }
        print(data)

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

    @intent_handler('ChangedMind').require('Ok I will not eat this')
    def good_choice(self, message):
        self.speak_dialog('WellDoneMessage')

    def stop(self):
        pass
def create_skill():
    return SnacksCalorieTracker()

