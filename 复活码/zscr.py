import requests  
import json
import httplib,urllib2,cookielib
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getHedaders():
	headers = {
		'Accept':'application/json',
		'Content-Type':'text/plain; charset=utf-8',
		'User-Agent': 'okhttp/3.5.0',
	}
	return headers

def login(num,code,requestId):
	url = "http://service.h7tuho5mf.cn/api/v1/login?cc=TG43909&lc=3e5563f89bab84b5&mtxid=f0b4293daa7d&devi=868808000000000&sid=&osversion=android_22&cv=CR1.2.00_Android&imei=868808000000000&proto=8&conn=wifi&ua=vivovivoX110&logid=&uid=0&icc=&aid=aeb880ff7951ad70&smid=&imsi=&mtid=705b2f4a6af92a130ab6702bb6709146"
	headers = getHedaders()
	param = '{"phone":"'+str(num)+'","platform":"phone","request_id":"'+str(requestId)+'","code":"'+str(code)+'"}'
	request = urllib2.Request(url = str(url),data = param,headers = headers)
	r = urllib2.urlopen(request).read()
	print r
	r = json.loads(r)
	return r['session']

def getCode(num):
	headers = getHedaders()
	url = 'http://service.h7tuho5mf.cn/api/v1/verification_code?cc=TG43909&lc=3e5563f89bab84b5&mtxid=f0b4293daa7d&devi=868808000000000&sid=&osversion=android_22&cv=CR1.2.00_Android&imei=868808000000000&proto=8&conn=wifi&ua=vivovivoX110&logid=&uid=0&icc=&aid=aeb880ff7951ad70&smid=&imsi=&mtid=705b2f4a6af92a130ab6702bb6709146'
	param = '{"phone":"'+str(num)+'","region":"cn"}'
	request = urllib2.Request(url = str(url),data = param,headers = headers)
	r = urllib2.urlopen(request).read()
	print r
	r = json.loads(r)
	return r['request_id']

def bindInviteCode(session,code):
	headers = getHedaders()
	url = 'http://service.h7tuho5mf.cn/api/invite_code/bind?cc=TG43909&lc=3e5563f89bab84b5&mtxid=f0b4293daa7d&devi=868808000000000&sid='+str(session)+'&osversion=android_22&cv=CR1.2.00_Android&imei=868808000000000&proto=8&conn=wifi&ua=vivovivoX110&logid=&uid=10581329&icc=&aid=aeb880ff7951ad70&smid=&imsi=&mtid=705b2f4a6af92a130ab6702bb6709146&code='+str(code)
	request = urllib2.Request(url = str(url),data = None,headers = headers)
	r = urllib2.urlopen(request).read()
	print r

request_id = getCode('8615612196288')
# sessionToken = login('15612196289','5333')
# print sessionToken
# bindInviteCode('305i1aJufhp68cyNVeJAaui2SXuDh7ORnuqBh8FOQ93FlZuTOnki3','1')

#login('8615612196289','5333','1516162366223088')