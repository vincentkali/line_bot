
from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, URIAction
import sys
from linebot import LineBotApi

channel_access_token = 'sTcy0mRQtYKW3r3XnlT80MqWC11JpLqQwdaQ6eRkWVGE9AMPhXvtSP1bMHqn66qmhNOMWdBse5+1zUcoftyJ5MP5AkJz16AJ+DzbGl7zyUBw9Nsoai8j0b9PiVv+G0iuPscvE8plDxDuxd15CmnTPAdB04t89/1O/w1cDnyilFU='

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#create_rich_menuself-rich_menu-timeoutnone
# Document: https://developers.line.biz/en/reference/messaging-api/#create-rich-menu

rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=1152, height=525),
    selected=False,
    name="Nice richmenu",
    chat_bar_text="Tap here",
    areas=[
    RichMenuArea(
        bounds=RichMenuBounds(x=0, y=0, width=575, height=524),
        action=URIAction(label='location', uri='https://dataportal.asia/dataset/203222207_covid-19-dcii/resource/c60dc5fd-a383-44e0-a357-e547355b1051')),
    RichMenuArea(
        bounds=RichMenuBounds(x=576, y=0, width=1151, height=524),
        action=URIAction(label='department', uri='https://data.zhupiter.com/oddt/11318383/%E8%87%BA%E5%8C%97%E5%B8%82%E5%85%AC%E7%A7%81%E7%AB%8B%E9%86%AB%E9%99%A2%E8%A8%BA%E7%99%82%E7%A7%91%E5%88%A5/'))
    ]
)
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
print(rich_menu_id)


