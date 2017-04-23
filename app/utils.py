from chatterbot import ChatBot
from config import DATABASE_URL


class utils():

    def __init__(self):
        self.chatbot = ChatBot(
            "Terry Wanjiku",
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            database_uri=DATABASE_URL,
            database='heroku_dgskmqsp'
        )
        # chatbot.set_trainer(ListTrainer)
        self.chatbot.train("chatterbot.corpus.english")

    def get_response(self, statement):
        return self.chatbot.get_response(statement)
