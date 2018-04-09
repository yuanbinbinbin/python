import requests  
import json
import httplib,urllib2,cookielib
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getRequest(url):
	httplib.HTTPConnection.debuglevel = 0
	request = urllib2.Request(str(url))
	request.add_header("Accenp","*/*")
	request.add_header("Accenp-Encoding","gzip,deflate,br")
	request.add_header("Accept-Language","zh0CN,en-US;q=0.8")
	request.add_header("User_Agent","Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 SearchCraft/1.6.2 (Baidu; P1 4.4.4)")
	request.add_header("Referer","https://secr.baidu.com/answer?xc=4cb7e5d341886c3a066e8fcb727308b7&app=xiguashipin")
	opener = urllib2.build_opener();
	f = opener.open(request)
	return f.read()

# https://secr.baidu.com/answer?xc=4cb7e5d341886c3a066e8fcb727308b7&app=xiguashipin
def getHeader(refe):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 SearchCraft/1.6.2 (Baidu; P1 4.4.4)',
		'Referer': str(refe),
		'Accept':'*/*',
		'Accept-Language':'zh_CN,en-US;q=0.8',
		'Accenp-Encoding':'gzip,deflate,br'
	}
	return headers

def getCookies(sid):
	cookie = cookielib.CookieJar()
	handler=urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)

def getRequest2(url,sid):
	httplib.HTTPConnection.debuglevel = 0
	headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 SearchCraft/1.6.2 (Baidu; P1 4.4.4)',
		'Referer':'https://secr.baidu.com/answer?xc=4cb7e5d341886c3a066e8fcb727308b7&app=xiguashipin',
		'Accept':'*/*',
		'Accept-Language':'zh_CN,en-US;q=0.8',
		'Accenp-Encoding':'gzip,deflate,br',
		'Cookie':'BAIDUID=B99A27A9112F2FA7E880039C30B07ED3:FG=1; BAIDUCUID=la2nigakHugIOS8MlOBjilitHijAaBiOgaHRila2S88puv83_u2C8_aj2ig7uviPA; BAIDULOC=1.29430404E7_4832366.27_1000_null_1515829495828; io='+str(sid)
	}
	request = urllib2.Request(url = str(url),data = None,headers = headers)
	return urllib2.urlopen(request).read()


url = "http://secr.baidu.com/nv/answer.sock/?EIO=3&transport=polling&t=M3kPiTt"  

r = getRequest2(url,"")

# r = requests.get(url).text

print r

r = r[r.find("{"):r.rfind("}")+1]

result = json.loads(r)

time.sleep(1)

sid = result["sid"]
url = "http://secr.baidu.com/nv/answer.sock/?EIO=3&transport=polling&t=M3kPiTt&sid="+str(sid)

r = getRequest2(url,str(sid))

print r