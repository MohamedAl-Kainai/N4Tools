from N4Tools.Design import ThreadAnimation,AnimationTools
import requests,time


@ThreadAnimation(Animation=AnimationTools.Loading,kwargs=(lambda **kwargs:kwargs)(text='Loading: [0/4]...'))
def check_url(Thread,urls):
	result = []
	for index,url in enumerate(urls):
		Thread.kwargs['text'] = f'Loading: [{index+1}/{len(urls)}]...'
		req = requests.get(url)
		result.append([url,req.ok])

	style = ''
	for url,state in result:
		style += url+': '+str(state)+'\n'

	Thread.kill()
	print (style[:-1])
#	Thread.set_end(style[:-1])

check_url(['https://google.com']*4)

