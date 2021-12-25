import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models.send_messages import ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api =LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(id, img_url):
    line_bot_api =LineBotApi(channel_access_token)
    image_message = ImageSendMessage(
        original_content_url='https://github.com/dennis23314063/test/blob/master/fsm.png?raw=true',
        preview_image_url='https://github.com/dennis23314063/test/blob/master/fsm.png?raw=true'
    )
    line_bot_api.reply_message(id, image_message)
    pass

def send_button_message(id, text, buttons):
    pass
