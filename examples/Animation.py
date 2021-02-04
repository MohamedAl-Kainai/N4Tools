# N4Tools version:1.7.1
from N4Tools.Design import (
	ThreadAnimation,
	Animation,
	AnimationTools
)
import requests

A = Animation()

@ThreadAnimation(Animation=A.Prograsse,kwargs={'min':0,'max':30})
def check_url(Thread,urls):
	result = []
	for index,url in enumerate(urls):
		Thread.set_kwargs(min=index+1,max=len(urls))
		req = requests.get(url)
		result.append([url,req.ok])
	style = ''
	for url,state in result:
		style += url+': '+str(state)+'\n'
	Thread.kill()
	print (style[:-1])

check_url(['https://google.com']*10)


text_animation = AnimationTools.set_text_anim('Loading...')
@ThreadAnimation(Animation=A.Loading,kwargs={'text':text_animation})
def check_url(Thread,urls):
	result = []
	for index,url in enumerate(urls):
		req = requests.get(url)
		result.append([url,req.ok])
	style = ''
	for url,state in result:
		style += url+': '+str(state)+'\n'
	Thread.kill()
	print (style[:-1])

check_url(['https://google.com']*10)
