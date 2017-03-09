import os
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Job
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(os.getenv('ChannelAccessToken'))
handler = WebhookHandler(os.getenv('ChannelSecret'))

# Create your views here.
def homepage(request):
	template = get_template('index.html')
	# jobs = Job.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

def showjob(request, slug):
	template = get_template('post.html')
	try:
		job = Job.objects.get(slug=slug)
		if job != None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=event.message.text)	
	)

@handler.default()
def default(event):
	print(event)
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Currently Not Support None Text Message')
	)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
