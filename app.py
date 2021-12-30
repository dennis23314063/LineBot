import os
import sys
import io
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from werkzeug.wrappers import response
from function import get_url
from fsm import TocMachine
from machine import multiple_machine
from utils import send_text_message, send_image_url
from machine import multiple_machine
load_dotenv()

person_machine = {}
machine = TocMachine(
    states=["user", "menu", "introduction","draw","fsm"],
    transitions=[
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "introduction",
            "conditions": "is_going_to_introduction",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "go_back",
            "source":["introduction","fsm","draw",],
            "dest": "menu"
        },
        {
            "trigger": "advance",
            "source":"menu",
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source":"menu",
            "dest": "draw",
            "conditions": "is_going_to_draw",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
    )

app = Flask(__name__, static_url_path="")
# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


# @app.route("/callback", methods=["POST"])
# def callback():
#     signature = request.headers["X-Line-Signature"]
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # parse webhook body
#     try:
#         events = parser.parse(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     # if event is MessageEvent and message is TextMessage, then echo text
#     for event in events:
#         if not isinstance(event, MessageEvent):
#             continue
#         if not isinstance(event.message, TextMessage):
#             continue
#         if event.message.text.lower() == 'fsm':
#             send_image_url(event.reply_token, 'https://github.com/dennis23314063/test/blob/master/fsm.png?raw=true')
#         line_bot_api.reply_message(
#             event.reply_token, TextSendMessage(text=event.message.text)
#         )

#     return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        if event.source.user_id not in person_machine:
            person_machine[event.source.user_id]=multiple_machine()
        response = person_machine[event.source.user_id].advance(event)
        if response == False:
            send_text_message(event.reply_token,"我有點聽不懂欸，要不要打打看menu!")
            

    return "OK"


@app.route('/show-fsm', methods=["GET"])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return send_file('fsm.png',mimetype='image/png')

if __name__ == "__main__":
    # show_fsm()
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
    
    
