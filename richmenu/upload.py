import sys
from linebot import LineBotApi

channel_access_token = 'sTcy0mRQtYKW3r3XnlT80MqWC11JpLqQwdaQ6eRkWVGE9AMPhXvtSP1bMHqn66qmhNOMWdBse5+1zUcoftyJ5MP5AkJz16AJ+DzbGl7zyUBw9Nsoai8j0b9PiVv+G0iuPscvE8plDxDuxd15CmnTPAdB04t89/1O/w1cDnyilFU='

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#set_rich_menu_imageself-rich_menu_id-content_type-content-timeoutnone
# Document https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image

content_type = 'image/png'  # Just support JPEG or PNG, check your image type

try:
    with open('./myTemplate.png', 'rb') as f:
        line_bot_api.set_rich_menu_image('richmenu-1dd62ecffdeddd85d5f0e18fece6cc95', content_type, f)
except Exception as e:
    print(e)

print('Set default success.')
