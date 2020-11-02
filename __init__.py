from mycroft import MycroftSkill, intent_file_handler
import os.path
import json

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tracker.calorie.snacks.intent')
    def handle_tracker_calorie_snacks(self, message):
        self.speak_dialog('tracker.calorie.snacks')
        tracker = os.path.expanduser("~/test/DailySnackTracker.json")
        filename = os.path.expanduser("~/test/Calorie_Master.json")
        with open(filename) as f:
           data = json.load(f)

        # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
        print(data)


        with open(tracker) as json_file:
            dataw = json.load(json_file)

            temp = dataw['Snacks']

            # python object to be appended
            y = {"snack": 'kitkat',
                 "quantity": "1",
                 "consumed": "900"
                 }


            temp.append(y)

            with open(tracker, 'w') as f:
                json.dump(dataw, f, indent=4)

    @intent_file_handler('changed.mind.intent')
    def handle_tracker_calorie_snacks(self, message):
        self.speak_dialog('WellDoneMessage')


    @intent_file_handler('inform.about.eating,intent')
    def handle_tracker_calorie_snacks(self, message):
        self.speak_dialog('WarnCalorie')

    @intent_file_handler('ignore.warning.intent')
    def handle_tracker_calorie_snacks(self, message):
        self.speak_dialog('TrackSnacksAdvice')


def create_skill():
    return SnacksCalorieTracker()

