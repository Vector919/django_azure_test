from django.shortcuts import render
from django.views.generic import View
import twitter
import json

class CONFIG(object):
	consumer_key = 'HpG6plhrTclBIL3sHoImtIpYv'
	consumer_secret = 'Ni4w70KlEtNjleLWBAxkciEh5yfAWqG54ZYnJKkOvcnTEFEAfq'
	access_token_key = '2726599771-fDvJtERRfLUXk0kzHLn5wjaVJdtt1pdsqgPfn5O'
	access_token_secret = 'LTWMKKpqpfMYKkRPjZRwrlPWADETkYdfhmGTaqsQhsivR'



from django.http import HttpResponse

class TwitterProxy(View):
	def get(self, request, *args, **kwargs):
		api = twitter.Api(
			consumer_key=CONFIG.consumer_key,
			consumer_secret=CONFIG.consumer_secret,
			access_token_key=CONFIG.access_token_key,
			access_token_secret=CONFIG.access_token_secret
		)
		djangocon_tweets = api.GetSearch("#djangocon")
		tweets_list = json.dumps([tweet.text for tweet in djangocon_tweets])
		return HttpResponse(tweets_list, content_type="application/json")
					
class DashView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'dashboard.html', {})
