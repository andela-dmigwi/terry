from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from app.kb import conversation
from config import DATABASE_URL


class utils():

    def __init__(self):
        self.chatbot = ChatBot(
            "Terry Wanjiku",
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            database_uri=DATABASE_URL,
            database='heroku_dgskmqsp'
        )
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(conversation)

    def get_response(self, statement):
        return self.chatbot.get_response(statement)
