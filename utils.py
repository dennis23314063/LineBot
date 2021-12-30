import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage
from linebot.models.send_messages import ImageSendMessage
import json

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api =LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def send_flex_message(reply_token,name):
    line_bot_api = LineBotApi(channel_access_token)
    FlexMessage = json.load(open(name+'.json','r',encoding = 'utf-8'))
    line_bot_api.reply_message(reply_token,FlexSendMessage(name,FlexMessage))

def send_image_url(id, img_url):
    line_bot_api =LineBotApi(channel_access_token)
    image_message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, image_message)
    pass

def send_button_message(id, text, buttons):
    pass
