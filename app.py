# lineSDK-python
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

#Flask
from flask import Flask, request, abort
from secret import MAMORU_CHANNEL_ACCESS_TOKEN,MAMORU_CHANNEL_SECRET

#OpenAI
from openAI import message_return


app = Flask(__name__)


line_bot_api = LineBotApi(MAMORU_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(MAMORU_CHANNEL_SECRET)

@app.route('/')
def test():
    return 'OK'

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


#messageのやりとりだけを記述する（処理は他の関数を作成）
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # メッセージを受け取る
    text=event.message.text()

    message = message_return(text)

    #メッセージ送信
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(message))  

if __name__ == "__main__":
    #デフォルト
    # app.run(debug=False, host='0.0.0.0', port=80)

    # dev環境
    app.run(debug=True,host='0.0.0.0', port=8080)
