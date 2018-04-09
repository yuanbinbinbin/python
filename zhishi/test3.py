import requests  
import json
import httplib,urllib2,cookielib
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# url = "http://secr.baidu.com/nv/answer.sock/?EIO=3&transport=polling&t=M3kPiTt"  


# r = requests.get(url).text

# print r

# r = r[r.find("{"):r.rfind("}")+1]

# result = json.loads(r)


# sid = result["sid"]
# url = "http://secr.baidu.com/nv/answer.sock/?EIO=3&transport=polling&t=M3kPiTt&sid="+str(sid)


# r = (requests.post(url,data="21:40/nv/huajiao/answer,")).text

# print r

# r = requests.get(url).text

# print r


# xigua      25:40/nv/xiguashipin/answer,
# chongding  28:40/nv/chongdingdahui/answer,
# huajiao    21:40/nv/huajiao/answer,


# times = (int(round(time.time() * 1000)))
# # http://140.143.49.31/api/ans2?key=xigua&wdcallback=jQuery321041284294542856514_1516181849356&_=1516181849377
# print times
# url = "http://140.143.49.31/api/ans2?key=cddh&_="+str(times)
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; vivo X110 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 SogouSearch Android1.0 version3.0 AppVersion/5903',
# 	'Referer':'http://fex.sa.sogou.com/',
# 	'x-wap-profile': 'http://218.249.47.94/Xianghe/MTK_LTE_Phone_L_UAprofile.xml',
# 	'Cookie':'IPLOC=CN1100; dt_ssuid=7060071477; SNUID=7864148FEAEF8835FEB76EECEA18FE0B; SUID=928EFE651810990A000000005A5D6D73; SUV=00CBC48965FE8E925A5D6D74C113D530; wuid=AAEufZGzHQAAAAqZElH+xwcAzQM=; adlocation=100; usid=kvu3QgJnVrBRQl6m; FREQUENCY=1516072308206_2; ld=tkllllllll2zgQC1lllllVINbgolllllBKfn6kllllwlllll9llll5@@@@@@@@@@; gpsloc=%E5%8C%97%E4%BA%AC%E5%B8%82%09%E6%B5%B7%E6%B7%80%E5%8C%BA; qqpos=116.272|39.954; SGS_FE_WAID=WAID2018011600000000000000166883; vrpos=TsxU/VVWHvUEwCNDYdt7tw=='
# }
# request = urllib2.Request(url = str(url),data = None,headers = headers)
# r = urllib2.urlopen(request).read()

# pDataLink = r'(?<=\\",\\"result\\":\\").+?(?=\\",\\"search_infos\\":)'
# patternLink = re.compile(pDataLink)
# # match1 = re.search(pattern1,r)
# link = patternLink.findall(r)


# print r
# print ''
# for item in link:
# 	print item


# r = requests.get("http://sa.sogou.com/user/configs?appinfo=SgL8QvtGkoc7xfT9%2Bcv6KdPJ4CiZGvkEYFS5V9OebGn7c3o1i8J9aR5gFJ1cv4%2FEvIVkgqpaU2KJFNmi44CCIw0WOqs9sxdHCQDxFcWCvIxQvtl27fJMPMn3c3I9mztcIq9446TQFkPa34DOesOhouHuEut5X9NwN7kfwKF%2F0O3XChmvmpOnONSdFz2UmyK1o68eFiY67K7cyFNeFzvuE78MQiZukyrDUZ6BwZmNi53EPTqc6RaW0f7%2Fif3cYEk4HcYMCKwutza3%2FFcYiLAN5LI6%2BFncxXbaInYQvTIDXvAMZFgJDANviVPcX8YsXUlhxTaO2S9Urbim16KiceXbYWgrQ0%2Bnru0BqbxKGLScuUJ2rrPqXpDuApDKyDo5Vi6h45PtMzsGPS7nmTo695kRCGg1teY98dWF1fEnArZkkfUuzFwj5c8DOHkUROt%2BPt7HgIYQTW6AQkjXm4RWz8jhD%2Bvia7WA%2FVPNZ6Iqz9jxkt4z70a%2Ft475YKmsc4eGiTM%2Bl57tL3WxuCtua6AbkyzRX2i35kMr1x9K9lUI4jVi%2FLboKhVK5uH9S1fntOdW51n%2FXtLbyly%2BbXHrpCb49Q3jtBZl2KYqtIsZJ0z9ooqGeoyQDBNjYp3HWxVjyxl%2BFdRD9EBRa%2Fu%2FWwyhNCVzBdnfL1xFPlcEym2q7CxMkuyI3x4iBPgc65Gk4bgLYKNtvq9NgzVwst96ZZmm9sUXM9eF0zwkhWXS5ewc9SB0Qs%2FKJLveqOiSXy%2F9eklAIo2PCBJrNJjd2jOlwjkpmcFes1FpIQ%3D%3D&from=app&mid=1aab868808022801374&product_id=fr9H6hncTEmpn8AJjYairg&resources=%5B%7B%22name%22%3A%22homepagechannels%22%2C%22sig%22%3A%2263a1c6426c70078784f67159568c43fb%22%2C%22type%22%3A%22%22%7D%5D&serv_ver=1&sign=8a5e6af83294c8b7403a673756e98dd4816cc9bb&time_stamp=1516182803558").text;
# # print r
# r = json.loads(r)
# r = r['result']['homepagechannels']['result']['channels'][1]['url']

# r = requests.get(r).text
# print r


# r = requests.get('https://wdpush.sogoucdn.com/api/anspush?key=huajiao&wdcallback=jQuery200006947432598099113_1518059718567&_=1518059718568').text
# print r

times = (int(round(time.time() * 1000)))
print times
url = "https://wdpush.sogoucdn.com/api/anspush?key=huajiao&_="+str(times)
headers = {
	'User-Agent': 'User-Agent: Mozilla/5.0 (Linux; Android 5.1; vivo XXX Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 SogouSearch Android1.0 version3.0 AppVersion/5903',
	'Referer':'https://assistant.sogoucdn.com/v5/cheat-sheet?channel=hj',
	'Cookie':'APP-SGS-ID=1aab86880802280'
}
request = urllib2.Request(url = str(url),data = None,headers = headers)
r = urllib2.urlopen(request).read()

print r
# pDataLink = r'(?<=\\",\\"result\\":\\").+?(?=\\",\\"search_infos\\":)'
# patternLink = re.compile(pDataLink)
# # match1 = re.search(pattern1,r)
# link = patternLink.findall(r)