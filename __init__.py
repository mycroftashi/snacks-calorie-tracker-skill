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
            y = {"snack": 'Chero',
                 "quantity": "1",
                 "consumed": "900"
                 }

            # appending data to emp_details
            temp.append(y)
            json.dump(dataw, json_file, indent=4)

def create_skill():
    return SnacksCalorieTracker()

