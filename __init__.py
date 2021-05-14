from mycroft import MycroftSkill, intent_file_handler


class MummyMovieFacts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('facts.movie.mummy.intent')
    def handle_facts_movie_mummy(self, message):
        self.speak_dialog('facts.movie.mummy')


def create_skill():
    return MummyMovieFacts()

