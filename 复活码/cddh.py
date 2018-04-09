import requests  
import json
import httplib,urllib2,cookielib
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getHedaders(xToken):
	headers = {
		'Accept':'application/json',
		'Content-Type':'application/json',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; vivo X110 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 SogouSearch Android1.0 version3.0 AppVersion/5903',
		'X-Live-App-Version':'1.0.6',
		'X-Live-Device-Type': 'android',
		'X-Live-Session-Token': str(xToken)
	}
	return headers

def login(num,code):
	url = "http://api.api.chongdingdahui.com/user/login"
	headers = getHedaders('')
	param = '{"phone":"'+str(num)+'","code":"'+str(code)+'"}'
	request = urllib2.Request(url = str(url),data = param,headers = headers)
	r = urllib2.urlopen(request).read()
	r = json.loads(r)
	print r
	return r['data']['user']['sessionToken']

def getCode(num):
	headers = getHedaders('')
	url = 'http://api.api.chongdingdahui.com/user/requestSmsCode'
	param = '{"phone":"'+str(num)+'"}'
	request = urllib2.Request(url = str(url),data = param,headers = headers)
	r = urllib2.urlopen(request).read()
	print r

def bindInviteCode(code):
	headers = getHedaders('1.30960819.1426043.JLd.fb74f9d42f2dcf2dd0d441143fc0a5ff')
	url = 'http://api.api.chongdingdahui.com/user/bindInviteCode'
	param = '{"inviteCode":"'+str(code)+'"}'
	request = urllib2.Request(url = str(url),data = param,headers = headers)
	r = urllib2.urlopen(request).read()
	print r

# getCode('15612196289')
# sessionToken = login('15612196289','5333')
# print sessionToken
bindInviteCode('1')