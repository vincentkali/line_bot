import sys
from linebot import LineBotApi

channel_access_token = 'sTcy0mRQtYKW3r3XnlT80MqWC11JpLqQwdaQ6eRkWVGE9AMPhXvtSP1bMHqn66qmhNOMWdBse5+1zUcoftyJ5MP5AkJz16AJ+DzbGl7zyUBw9Nsoai8j0b9PiVv+G0iuPscvE8plDxDuxd15CmnTPAdB04t89/1O/w1cDnyilFU='

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

line_bot_api.delete_rich_menu("richmenu-c829e7064176941ca5229af05596e54b")