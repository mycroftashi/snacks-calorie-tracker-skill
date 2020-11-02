from mycroft import MycroftSkill, intent_file_handler
import Read_Write_Calories.py

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tracker.calorie.snacks.intent')
    def handle_tracker_calorie_snacks(self, message):
        self.speak_dialog('tracker.calorie.snacks')
        execfile('Read_Write_Calories.py')


def create_skill():
    return SnacksCalorieTracker()

