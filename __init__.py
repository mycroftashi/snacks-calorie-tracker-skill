from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import os.path
import json

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_handler(IntentBuilder('InformAboutEatingIntent').require('SnackKeyword'))
    def handle_inform_about_eating_intent(self, message):
        self.speak_dialog("WarnCalorie")

def stop(self):
    pass

def create_skill():
    return SnacksCalorieTracker()

