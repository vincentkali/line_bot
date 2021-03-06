# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import csv
import os
import sys
import json

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('sTcy0mRQtYKW3r3XnlT80MqWC11JpLqQwdaQ6eRkWVGE9AMPhXvtSP1bMHqn66qmhNOMWdBse5+1zUcoftyJ5MP5AkJz16AJ+DzbGl7zyUBw9Nsoai8j0b9PiVv+G0iuPscvE8plDxDuxd15CmnTPAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e6ca7ad4597415ed5bcd58e01d02e909')

LINE_FRIEND = dict(
    BROWN="https://stickershop.line-scdn.net/stickershop/v1/sticker/52002734/iPhone/sticker_key@2x.png",
    CONY="https://stickershop.line-scdn.net/stickershop/v1/sticker/52002735/iPhone/sticker_key@2x.png",
    SALLY="https://stickershop.line-scdn.net/stickershop/v1/sticker/52002736/iPhone/sticker_key@2x.png"
)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global LINE_FRIEND
    global FLEX_template
    print(event.message)
    if event.message.text == "sticker":
        message = StickerSendMessage(
            package_id='446',
            sticker_id='1988'
        )
    elif event.message.text == "image":
        message = ImageSendMessage(
            original_content_url='https://imgur.com/di9CAJV.png',
            preview_image_url='https://imgur.com/di9CAJV.png'
        )
    elif event.message.text == "video":
        message = TextSendMessage(text="https://www.youtube.com/watch?v=X2lIovmNsUY")
    elif event.message.text == "audio":
        pass
    elif event.message.text == "template":
        pass
    elif event.message.text == "confirm":
        confirm_template = ConfirmTemplate(text='Do it?', actions=
            [MessageAction(label='Yes', text='Yes!'),
            MessageAction(label='No', text='No!')])
        message = TemplateSendMessage(alt_text='Confirm alt text', template=confirm_template)
        
    elif event.message.text == "reply":
        message = TextSendMessage(
                text='Quick reply',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="label1", data="data1")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="label2", text="text2")
                        ),
                        QuickReplyButton(
                            action=DatetimePickerAction(label="label3",
                                                        data="data3",
                                                        mode="date")
                        ),
                        QuickReplyButton(
                            action=CameraAction(label="label4")
                        ),
                        QuickReplyButton(
                            action=CameraRollAction(label="label5")
                        ),
                        QuickReplyButton(
                            action=LocationAction(label="label6")
                        ),
                    ]))
    elif event.message.text == "profile":
        user = line_bot_api.get_profile(user_id=event.source.user_id)
        message = TextSendMessage(text='Congrats '+user.display_name)

    elif event.message.text.upper() in LINE_FRIEND:
        name = event.message.text.upper()
        icon = LINE_FRIEND[name]
        message = TextSendMessage(
            text=message,
            sender=Sender(
                name=name,
                icon_url=icon))
    elif event.message.text <= "10" and event.message.text >= "1":
        number = int(event.message.text)
        rows_list = []
        with open(os.path.abspath("maskdata.csv"), newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                rows_list.append(row)
        message = TextSendMessage(text=str(rows_list[number]))
        
    else:
        message = TextSendMessage(text="You say "+event.message.text)
    
    line_bot_api.reply_message(event.reply_token, message)
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)