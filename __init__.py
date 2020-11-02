from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.skills.context import adds_context, removes_context
import os.path
import json

class SnacksCalorieTracker(MycroftSkill):
    def __init__(self):

        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('WhatIsPotato').require('What')
                    .require('Potato'))
    def handle_what_is(self, message):
        self.speak_dialog('potato.description')

        
    def stop(self):
        pass
def create_skill():
    return SnacksCalorieTracker()

