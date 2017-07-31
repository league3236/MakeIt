
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('pekBiKjiDMZRibx1G5wKBOhcdU9d1Bo2w2jbN6fvzhzI9QYitqmUe7TnPJJ+kI4A0+KF4ehYTp8DJnmz0D5BgyAjEp3Ru/sejA+hwp/8g+Pekog+EWobWgIKr/Ix6hgEVZt6r0bw5lE9Gh4tZsVnmgdB04t89/1O/w1cDnyilFU=')

try:
    line_bot_api.reply_message('<reply_token>', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
    ...
