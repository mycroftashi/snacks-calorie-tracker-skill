from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class SnacksCalorieTracker(MycroftSkill):

    @intent_handler(IntentBuilder('ThankYouIntent').require('ThankYouKeyword'))
    def handle_thank_you_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("welcome")

    @intent_handler('DeclineAdvice.intent')
    def handle_decline_advice(self, message):
        """ This is a Padatious intent handler.
		It is triggered using a list of sample phrases."""
        self.speak_dialog("TrackSnacksAdvice")

    @intent_handler(IntentBuilder('SnackingIntent')
                    .require('SnackKeyword'))
    def handle_snacking_intent(self, message):
        self.speak_dialog("WarnCalorie")

    def stop(self):
        pass

def create_skill():
    return SnacksCalorieTracker()