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



def create_skill():
    return SnacksCalorieTracker()

