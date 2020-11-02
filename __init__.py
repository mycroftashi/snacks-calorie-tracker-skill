from mycroft import MycroftSkill, intent_file_handler
import json

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tracker.calorie.snacks.intent')
    def handle_tracker_calorie_snacks(self, message):
        self.speak_dialog('tracker.calorie.snacks')

    with open('test/Calorie_Master.json') as f:
        data = json.load(f)

        # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    print(data)

    def write_json(data, filename='test/DailySnackTracker.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    with open('test/DailySnackTracker.json') as json_file:
        data = json.load(json_file)

        temp = data['Snacks']

        # python object to be appended
        y = {"snack": 'Cheerios',
             "quantity": "1",
             "consumed": "900"
             }

        # appending data to emp_details
        temp.append(y)

    write_json(data)


def create_skill():
    return SnacksCalorieTracker()

