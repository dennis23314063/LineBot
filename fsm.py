from transitions.extensions import GraphMachine
from function import get_url
from utils import send_flex_message, send_image_url, send_text_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"
    def is_going_to_introduction(self, event):
        text = event.message.text
        return text.lower() == "how"
    def is_going_to_fsm(self,event):
        text = event.message.text
        return text.lower() == "fsm"
    def is_going_to_draw(self,event):
        text = event.message.text
        return text.lower() == "draw" or text == "抽"
    def on_enter_menu(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,'menu')
    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token,"https://github.com/dennis23314063/test/blob/master/fsm.png?raw=true")
        self.go_back()
    def on_enter_draw(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token,get_url())
        self.go_back()
    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入 menu 叫出主選單\n"+"輸入 fsm 看看本機器人的state圖\n"+"輸入 draw 或 抽 得到一隻可愛的動物")
        self.go_back()