
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('pekBiKjiDMZRibx1G5wKBOhcdU9d1Bo2w2jbN6fvzhzI9QYitqmUe7TnPJJ+kI4A0+KF4ehYTp8DJnmz0D5BgyAjEp3Ru/sejA+hwp/8g+Pekog+EWobWgIKr/Ix6hgEVZt6r0bw5lE9Gh4tZsVnmgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7a044e892ad8c98f50664ea1ddbf0aa1')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
