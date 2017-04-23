""" Created by Migwi Ndung'u  @April 2017"""
import json
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from app.templates import user_not_found  # , welcome_text, something_wrong
from config import fb_url, params, json_headers
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
        response = self.chatbot.get_response(statement)
        print('You want some>>>>>', response)
        return str(response).lstrip('<Statement text:').rstrip('>')

    def send_message(self, recipient_id, message_text=None, template=None):
        data = {
            "recipient": {"id": '{}'.format(recipient_id)},
            "message": {"text": '{}'.format(message_text)}
        }

        if template:
            data['message'] = template
        print('Data >>>>', data)
        data = json.dumps(data)
        url = "{}/me/messages".format(fb_url)
        response = requests.post(url, params=params,
                                 headers=json_headers, data=data)
        if response.status_code != 200:
            print('Error Code 1:', response.json(),
                  '\n User_id: ', recipient_id)

    # def get_user_details(self, user_id):
    #     url = "{}/{}".format(fb_url, user_id)
    #     response = requests.get(url, params=params)
    #     if 'error' in response:
    #         print('Error Code 2:', response.json())
    #         return user_not_found
    #     return response.json()

    # def postback(self, user_id, message_text):
    #     g.sender_id = user_id
    #     text = ''
    #     if message_text == 'SIGN_UP':
    #         text = self.user_registration(user_id)
    #     else:
    #         text = self.match_response(message_text)
    #     self.send_message(user_id, message_text=text)

    # def user_registration(self, user_id):
    #     user = self.get_user_details(user_id)
    #     if user is user_not_found:
    #         return user_not_found
    #     else:
    #         try:
    #             name = "{} {}".format(user['first_name'], user['last_name'])
    #             Users(name=name, fb_id=user_id).save()
    #             return welcome_text
    #         except Exception:
    #             return self.match_response('Hello')

    def match_response(self, sender_id, text_message):
        response = self.get_response(text_message)
        self.send_message(sender_id, message_text=response)
