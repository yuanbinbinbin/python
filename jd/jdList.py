import requests  
import json
import httplib,urllib2,cookielib
import time
import ssl
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ssl._create_default_https_context = ssl._create_unverified_context

url = "http://a.jd.com/coupons.html?st=2&page=1&ct=4"  


r = requests.get(url).text

# r = r.replace(" ","")

pDataKey = r'(?<=data-key=").+?(?=")'
patternDataKey = re.compile(pDataKey)
# match1 = re.search(pattern1,r)
dataKey = patternDataKey.findall(r)

for x in dataKey:
	print x


pDataLink = r'(?<=data-linkUrl=").+?(?=")'
patternLink = re.compile(pDataLink)
# match1 = re.search(pattern1,r)
link = patternLink.findall(r)

for x in link:
	print "https:"+x


pMoney = r'(?<=<strong class="num">).+?(?=</strong>)'
patternMoney = re.compile(pMoney)
money = patternMoney.findall(r)

for x in money:
	print x


pMoneyLimit = r'(?<=<span class="ftx-06">).+?(?=</span></div>)'
patternMoneyLimit = re.compile(pMoneyLimit)
moneyLimit = patternMoneyLimit.findall(r)

for x in moneyLimit:
	print x