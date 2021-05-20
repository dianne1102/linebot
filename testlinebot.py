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

line_bot_api = LineBotApi('VVHYMLeRHGLXgMJO4Vez/nRi89DbgIvAUemepsOqZxa6PvIEXTKLHRqfBU/EF53Das9pkV+qF1FiqZflcge/SGxLFX2YOm9uhSXDwn4QbCB4/K3HEkU96U+ppd04snzurfNnHRSh4aVamVXlcuESFwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b479faeeb04dc6f361c645016c40dbb4')


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


@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
    #print("Hi")
    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(text=event.message.text))
     #line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World!'))

def work(event):

	worktext=event.message.text
	if(worktext == "工作" or worktext == "工作經歷"):
		line_bot_api.reply_message(
        		event.reply_token,
        		TextSendMessage(text= "曾在明基材料擔任intern, 負責瑕疵辨識專案, 此專案主要使用CNN訓練及測試瑕疵圖片")
    		)

	if(worktext == "介紹" or worktext == "自我介紹"):
		line_bot_api.reply_message(
        		event.reply_token,
        		TextSendMessage(text= "目前就讀於台灣科技大學資管所碩一, 專長為ISO27001, 目前也在考IEC62443 certification, 大學也從事過醫療 AI 方面的專題")
    		)


	if(worktext == "技能" or worktext == "個人技能"):
		line_bot_api.reply_message(
        		event.reply_token,
        		TextSendMessage(text= "目前使用的程式語言為 Python 及 C++, 對於ISO27001, IEC62443等等法規標準也有一些了解, TOEIC 分數為775")
    		)
	
	if(worktext == "學歷" or worktext == "教育程度"):
		line_bot_api.reply_message(
        		event.reply_token,
        		TextSendMessage(text= "元智大學 資訊工程學系 2016-2020 \n台灣科技大學資訊管理所 2020-")
    		)

	
	if(worktext == "其他" or worktext == "other"):
		line_bot_api.reply_message(
        		event.reply_token,
        		TextSendMessage(text= "大學期間, 我曾經擔任scratch夏/冬令營的leader, 負責分配教學及教學桃園偏鄉小學孩童")
    		)

#def profile(event):
	#profiletext=event.message.text
	#if(profiletext == "介紹" or profiletext == "自我介紹"):
		#line_bot_api.reply_message(
        		#event.reply_token,
        		#TextSendMessage(text= "目前就讀於台灣科技大學資管所碩一, 專長為ISO27001, 目前也在考IEC62443 certification, 大學也從事過醫療 AI 方面的專題")
    		#)


#def me(event):
	#metext=event.message.text
	#if(metext == "技能" or metext == "個人技能"):
		#line_bot_api.reply_message(
        		#event.reply_token,
        		#TextSendMessage(text= "目前使用的程式語言為 Python 及 C++, 對於ISO27001, IEC62443等等法規標準也有一些了解, TOEIC 分數為775")
    		#)

#def education(event):
	#metext=event.message.text
	#if(educationtext == "技能" or educationtext == "個人技能"):
		#line_bot_api.reply_message(
        		#event.reply_token,
        		#TextSendMessage(text= "元智大學 資訊工程學系 2016-2020, 台灣科技大學資訊管理所 2020-")
    		#)

#def other(event):
	#othertext=event.message.text
	#if(othertext == "其他" or othertext == "other"):
		#line_bot_api.reply_message(
        		#event.reply_token,
        		#TextSendMessage(text= "大學期間, 我曾經擔任scratch夏/冬令營的leader, 負責分配教學及教學桃園偏鄉小學孩童")
    		#)



#def echo(event):
    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(text=event.message.text)
    #)



if __name__ == "__main__":
    app.run()