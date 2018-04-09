import requests  
import json
import httplib,urllib2,cookielib
import time
import sys
import random
import ssl
import StringIO, gzip

reload(sys)
sys.setdefaultencoding('utf-8')

def gzdecode(data) :  
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()
    return data2

# http://140.143.49.31/api/ans2?key=xigua&wdcallback=jQuery321041284294542856514_1516181849356&_=1516181849377
randomKey = random.random()
print randomKey
key = 'fb4b4e639e345d31d2814523bb4e5cdb74aa5e69ca797a23f77dba8a22bdebfe121a075f6429a24cb070e7fbd9650ee3'
url = "https://a.jd.com/ajax/freeGetCoupon.html?key="+str(key)+'&r='+str(randomKey)

referer = 'https://a.jd.com/coupons.html?st=2&page=2&ct=4'
headers = {
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; vivo X110 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 SogouSearch Android1.0 version3.0 AppVersion/5903',
	'Referer':str(referer),
	'Cookie':'pinId=Bcvu1NY80V38pdfhGP2B3rV9-x-f3wj7; pin=jd_79103a216fef7; unick=jd_156733oeu; _tp=5X0hWwYKZ%2FJjG3GMRQ3BobGHYM0FFGb5JQ2xtgDUyqo%3D; _pst=jd_79103a216fef7; __jdu=15124742663851386091563; 3AB9D23F7A4B3C9B=ZSSY7GVHTCGG5D6JHZEEAAESXI4YOCQLMSFCNOLTSI2CN3UWGKW6MVMTH57CHX75KVU5HA4OZUU34IDWLGW65QTFDM; mba_muid=15124742663851386091563; shshshfp=b4f444211f338da1836195eeeab83652; shshshfpa=c025e1f0-7fa0-45a7-9455-24e235676368-1513754154; shshshfpb=0e977637c6ac176b9669e9b94bbdf46fa88984c56fdeec4065a3a0e2a3; TrackerID=UvJGG40MkuFI1KmUUMSSAmSH0oWtZaEg5Ig4fPhha92bV3EovQpe6b3ETuyO7MPnQuo6XCt93gbTg8dZ9jaZ8TDVwhVX_3UJKUImGNS6Gu4; __jda=122270672.15124742663851386091563.1512474266.1514968326.1517372202.13; __jdc=122270672; __jdv=122270672|direct|-|none|-|1517372201584; _jrda=8; _jrdb=1517372229014; wlfstk_smdl=3ms7r3kl60ka0iun0d5tbv674q63d31g; TrackID=1v1cBwKnagO9V1EgbHRcKyKvZLQL3J_4ZlozGYp4rLnRtoUfbtFbiM-8SPlZfRlgtPItMPo3a8LzX54Pl_6HIIkfWop3w-gd2mGQpLZLqPr8; thor=6EFF23FFB4FC5FA9BA2F13B50518E8B03DAFE6DAEF2B0B19ACCE8D8377AE8D17DBE08E400FF6A7C840E8DFB72263A0D11944E859062A278640B2E0AFD528F05CD6CF60E455462274F2166B5E596C1B2EE5E90833E645B67A1C61B141236B16568160EFF2E154C4EB0918BC8053CC6853EEAEDADEA8C7B820A0FF3BCA4D342E85C386F20DADE1A48B3E0A21DA30990F66006A45AE3F884AA2EB157BA7DE807CD0; ceshi3.com=000; JSESSIONID=B5884DF92D19723E4EE43C652E80582F.s1; __jdb=122270672.6.15124742663851386091563|13.1517372202',
	'X-Requested-With':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

ssl._create_default_https_context = ssl._create_unverified_context
request = urllib2.Request(url = str(url),data = None,headers = headers)
print time.time()
r = urllib2.urlopen(request).read()
print time.time()
print gzdecode(r)

#                                              cb75e9a5cef7fefb589cf3e8ee8cc9d48e185c802c2f6dfa2d5869b57c204faa8fa917ebb5005255f9a06a17456c0f12
# cb75e9a5cef7fefb589cf3e8ee8cc9d48e185c802c2f6dfa2d5869b57c204faa8fa917ebb5005255f9a06a17456c0f12&r=0.8878958963854333

