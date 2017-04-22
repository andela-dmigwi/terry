from chatterbot import ChatBot
from chatterbot import storage
from config import DATABASE_URL


class utils():

    def __init__(self):
        storage.MongoDatabaseAdapter(database='terry-database',
                                     database_uri=DATABASE_URL)
        self.chatbot = ChatBot(
            "Terry Wanjiku",
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
        # chatbot.set_trainer(ListTrainer)
        self.chatbot.train("chatterbot.corpus.english")

    def get_response(self, statement):
        return self.chatbot.get_response(statement)
