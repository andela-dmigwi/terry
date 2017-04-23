""" Created by Migwi Ndung'u  @April 2017"""
from app import create_app
from flask import request, make_response
from app.utils import utils

app = create_app()
util = utils()


@app.route('/', methods=['GET'])
def verify():
    hub_challenge = request.args.get("hub.challenge")
    if (hub_challenge):
        return make_response(hub_challenge, 200)
    # Response tests successful deployment of the bot..
    return make_response("Hello world, I am Terry Wanjikoh your"
                         ", personal medical expert!!", 200)


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print('*******\n', data, '\n#######')
    if not data:
        return make_response("ok", 200)

    if data["object"] == "page":

        for entry in data["entry"]:
            if 'messaging' in entry:
                for messaging_event in entry["messaging"]:
                    sender_id = messaging_event["sender"]["id"]
                    # recipient_id = messaging_event["recipient"]["id"]

                    if messaging_event.get("message"):
                        event = messaging_event["message"]

                        if "text" in event:
                            message_text = event["text"]
                            util.match_response(sender_id, message_text)
                        else:
                            print('No Text Message sent')

                    # delivery confirmation
                    if messaging_event.get("delivery"):
                        pass

                    # optin confirmation
                    if messaging_event.get("optin"):
                        pass

                    # user clicked/tapped "postback" button in earlier message
                    if messaging_event.get("postback"):
                        pass
                        # postback = messaging_event["postback"]["payload"]
                        # util.postback(user_id=sender_id,
                        #                message_text=postback)
            else:
                print('Metadata file was sent')
                print('>>>>>>>::\n', entry, '::<<<<<<')
                # sender_id = messaging_event["sender"]["id"]
                # util.eliza_response(sender_id, 'computers')

    return make_response("ok", 200)
