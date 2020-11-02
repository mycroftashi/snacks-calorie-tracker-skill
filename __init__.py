from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class SnacksCalorieTracker(MycroftSkill):

    @intent_handler(IntentBuilder('WhatIsPotato').require('What')
                    .require('Potato'))
    def handle_what_is(self, message):
        self.speak_dialog('potato.description')

    @intent_handler(IntentBuilder('DoYouLikePotato').require('Potato')
                    .require('Like').optionally('Type').one_of('You', 'I'))
    def handle_do_you_like(self, message):
        potato_type = message.data.get('Type')
        if potato_type is not None:
            self.speak_dialog('like.potato.type',
                              {'type': potato_type})
        else:
            self.speak_dialog('like.potato.generic')

def create_skill():
    return SnacksCalorieTracker()