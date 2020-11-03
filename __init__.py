from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class SnacksCalorieTracker(MycroftSkill):

    @intent_handler(IntentBuilder('SnackingIntent')
                    .require('SnackKeyword'))
    def handle_snacking_intent(self, message):
        self.speak_dialog("WarnCalorie", expect_response=True)
       

    @intent_handler(IntentBuilder('DeclineAdviceIntent').require('DeclineKeyword'))
    def handle_decline_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("TrackSnacksAdvice", expect_response=True)



    @intent_handler(IntentBuilder('ListeningIntent')
                    .require('ListenKeyword'))
    def handle_listen_to_advice_intent(self, message):
        self.speak_dialog("WellDoneMessage")


    def stop(self):
        pass

def create_skill():
    return SnacksCalorieTracker()