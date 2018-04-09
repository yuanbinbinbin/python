import requests  
import json
import httplib,urllib2,cookielib
import hashlib
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getHedaders():
	headers = {
		'Accept':'gzip',
		'Content-Type':'application/x-www-form-urlencoded',
		'User-Agent': 'okhttp/3.8.1',
	}
	return headers

def login(num,code,requestId):
	url = "https://is.snssdk.com/user/mobile/send_code/v2/?os_api=22&device_type=vivo+X6D&device_platform=android&ssmix=a&iid=23009261004&manifest_version_code=169&dpi=480&uuid=868808022801374&version_code=169&app_name=aweme&version_name=1.6.9&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1692&aid=1128&channel=update&_rticket=1516170563735&ts=1516170563&as=a1056e0533c49a0dbe&cp=eb49ab533de95ed9e1"
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

#request_id = getCode('8615612196288')
# sessionToken = login('15612196289','5333')
# print sessionToken
# bindInviteCode('305i1aJufhp68cyNVeJAaui2SXuDh7ORnuqBh8FOQ93FlZuTOnki3','1')

#login('8615612196289','5333','1516162366223088')

num = '15612196289'
by = bytearray(num)
print type(by)
print '----------'
for i in range(len(by)):
	by[i] = 0x05 ^ by[i]

a = [ 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102 ];
resultBy = by + by

print len(by)
print len(resultBy)
j = 0
for i in range(len(by)):
	k = 0xFF & by[i+0]
	m = j + 1
	resultBy[j] = a[k >> 4]
	j = m + 1
	resultBy[m] = a[k & 0xF]

s = str(resultBy)
print s

# 2e3d333430333437343c33373d3c
# 3430333437343c33373d3c