# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('sTcy0mRQtYKW3r3XnlT80MqWC11JpLqQwdaQ6eRkWVGE9AMPhXvtSP1bMHqn66qmhNOMWdBse5+1zUcoftyJ5MP5AkJz16AJ+DzbGl7zyUBw9Nsoai8j0b9PiVv+G0iuPscvE8plDxDuxd15CmnTPAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e6ca7ad4597415ed5bcd58e01d02e909')

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
        pass
    elif event.message.text == "audio":
        pass
    else:
        message = TextSendMessage(text="You say "+event.message.text+"\nhttps://www.youtube.com/watch?v=X2lIovmNsUY\nhttps://imgur.com/di9CAJV.png")
    
    line_bot_api.reply_message(event.reply_token, message)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
