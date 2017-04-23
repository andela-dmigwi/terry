""" Created by Migwi Ndung'u  @April 2017"""
from app import create_app
from flask import request, make_response
from app.utils import utils
from config import page_access_token
from fbmq import Page


app = create_app()
page = Page(page_access_token)
util = utils()


@app.route('/', methods=['GET'])
def verify():
    hub_challenge = request.args.get("hub.challenge")
    if (hub_challenge):
        return make_response(hub_challenge, 200)
    # Response tests successful deployment of the bot..
    return make_response("Hello world, this is a Facebook"
                         " Video and Chat Bot. Enjoy!!", 200)


@app.route('/', methods=['POST'])
def webhook():
    page.handle_webhook(request.get_data(as_text=True))
    return "ok"


@page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text

    page.send(sender_id, util.get_response(message))


@page.after_send
def after_send(payload, response):
    """:type payload: fbmq.Payload"""
    print("complete")
