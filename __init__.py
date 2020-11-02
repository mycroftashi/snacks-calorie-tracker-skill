from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.skills.context import adds_context, removes_context
import os.path
import json

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):

        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('IAmEatingChewyBar').require('Eating').require('chewy').require('bar'))
    def handle_i_am_eating(self, message):
        self.speak_dialog('WarnCalorie')

    @intent_handler(IntentBuilder('IAmEatingKitKat').require('Eating').require('Kit').require('Kat'))
    def handle_i_am_eating_kitkat(self, message):
        self.speak_dialog('TrackSnacksAdvice')

    def stop(self):
        pass
def create_skill():
    return SnacksCalorieTracker()

