#coding=utf-8
import requests
import json
import time

matcherNum = ""

def search(num,searchNum):
	try:
		global matcherNum
		requestTime = int(time.time()*1000)
		url = "https://m.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=11&cityCode=110&monthFeeLimit=0&groupKey=30242833&searchCategory=3&net=01&amounts=200&codeTypeCode=&qryType=02&goodsNet=4&_="
	#sjz	# url = "https://m.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=18&cityCode=188&monthFeeLimit=0&groupKey=15237219&searchCategory=3&net=01&amounts=200&codeTypeCode=&qryType=02&goodsNet=4&_="		
		url += str(requestTime)
		url = url + "&searchValue="+ str(num)
		result = requests.get(url).text
		result = result.replace("jsonp_queryMoreNums(","")
		result = result.replace(");","")
		# print(result)
		result = json.loads(result)
		result = result["numArray"]
		for item in result:
			# print str(searchNum) +"  "+str(item)
			if str(searchNum) in str(item) :
				# print "matcherNum"+matcherNum+str(str(matcherNum).find(str(item)))
				if str(matcherNum).find(str(item)) < 0:
					print item
					print "\a"
					matcherNum = matcherNum + str(item)+","
	except Exception : requestTime = 0

def search():
	try:
		global matcherNum
		requestTime = int(time.time()*1000)
		url = "http://m.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=18&cityCode=188&monthFeeLimit=0&groupKey=15237219&searchCategory=3&net=01&amounts=200&codeTypeCode=&searchValue=&qryType=02&goodsNet=4&_="
		url += str(requestTime)
		result = requests.get(url).text
		result = result.replace("jsonp_queryMoreNums(","")
		result = result.replace(");","")
		# print(result)
		result = json.loads(result)
		result = result["numArray"]
		for item in result:
			# if item != 0 and item != 1:
			# 	print str(item)
			if "0000" in str(item) :
				addNum(str(item))
			elif "1111" in str(item):
				addNum(str(item))
			elif "2222" in str(item):
				addNum(str(item))
			elif "3333" in str(item):
				addNum(str(item))
			elif "4444" in str(item):
				addNum(str(item))
			elif "5555" in str(item):
				addNum(str(item))
			elif "666" in str(item):
				addNum(str(item))
			elif "7777" in str(item):
				addNum(str(item))
			elif "888" in str(item):
				addNum(str(item))
			elif "999" in str(item):
				addNum(str(item))
	except Exception : 
		print "error"

def addNum(num):
	global matcherNum
	if(str(matcherNum).find(str(num))) < 0:
		print num+"\a"
		# print "\a"
		matcherNum = matcherNum + str(num)+","

# print str('15612196289,'.find("15612196289"))
# search(99,"999")
# time.sleep(5)
# search(99,"999")
# time.sleep(5)
# print ("\a")
# matchNum("1562199289")
# search()
while True:
	search()
	time.sleep(5)

	# search(11,"111")
	# time.sleep(5)
	# search(22,"222")
	# time.sleep(5)
	# search(33,"333")
	# time.sleep(5)
	# search(44,"444")
	# time.sleep(5)
	# search(55,"555")
	# time.sleep(5)
	# search(66,"666")
	# time.sleep(5)
	# search(77,"777")
	# time.sleep(5)
	# search(88,"888")
	# time.sleep(5)
	# search(99,"999")
	# time.sleep(5)
