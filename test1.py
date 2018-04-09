#coding=utf-8
import requests
import json
import time
import pymysql as mdb
import re

def getJson(url):
	jsons = requests.get(url)
	return jsons.text
def insertData(times,count,platform):
	try:
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		cur.execute("insert into tb_people_count values(%s,%s,%s)",(times,count,platform))
		conn.commit()
		cur.close()
		conn.close()
	except Exception : print("error")
def getChuShouCount():
	count = 0
	try:
		chushou = getJson("http://chushou.tv/live/down-v2.htm")
		result = json.loads(chushou)
		count = result["data"]["count"]
	except Exception : count = 0
	return count
def getFeiYunCount():
	count = 0
	try:
		feiyun = getJson("http://www.feiyun.tv/room");
		pattern = "\\(([0-9]*)\\)"
		ret = re.search(pattern,feiyun)
		if ret:
			for x in ret.groups():
				return x
	except Exception : count = 0
	return count
def getShiHouCount():
	j = 0
	count = 0
	try:
		while(j >= 0) :
			count = j
			parameters = {'offset':j}
			shihou = (requests.post("http://api.shihou.tv/api/hotwar",data=parameters)).text
			result =json.loads(shihou)
			j = result["offset"]
			if(j < 0):
				count = count + len(result["data"]["data"])
	except Exception : count = 0
	return count
def getLanShaCount():
	try:
		lansha = getJson("http://www.lansha.tv/liveList.html")
		pattern = "<em>([0-9]*)</em>"
		ret = re.search(pattern,lansha)
		if ret:
			for x in ret.groups():
				return x
		else:
			return 0
	except Exception : return 0

def getDaShenCount():
	count = 0
	try:
		dashen = getJson("http://www.dashen.tv/live/get_all_live_list/")
		result = json.loads(dashen)
		count = result['result_data']['count']
	except Exception : count = 0
	return count
def get5kongCount():
	count = 0
	try:
		wukong = getJson("http://api.5kong.tv/Live/List/liveList")
		result = json.loads(wukong)
		count = result['data']['total']
	except Exception : count = 0
	return count
def getHaZhiBoCount():
	room_limit = 10
	itemCount = 10
	count = 0
	try:
		while(itemCount >= room_limit) :
			hazhibo = (requests.get("http://api.hahabo.com/service/home/recom_list?room_limit="+str(room_limit)+"&offset="+str(count))).text
			result =json.loads(hazhibo)
			itemCount = len(result["data"])
			count += itemCount
	except Exception : count = 0
	return count
def getQiECount():
	count = 0-9
	try:
		qiEParameters = {'param':"{\"0\":{\"module\":\"pgg_live_read_svr\",\"method\":\"get_live_list\",\"param\":{\"layout_id\":\"hot\",\"page_num\":1,\"page_size\":2,\"other_uid\":0}}}",'app_info':"{\"platform\":4,\"terminal_type\":2,\"egame_id\":\"egame_official\"}"}
		qie = (requests.post("http://share.egame.qq.com/cgi-bin/pgg_skey_async_fcgi?&cgi_method=get_live_list&g_tk=832538900",data=qiEParameters)).text
		result = json.loads(qie)
		count = result["data"]["0"]["retBody"]["data"]["total"]
	except Exception : count = 0
	return count
while True:
	requestTime = time.localtime()
	insertData(requestTime,getChuShouCount(),"chushou")
	insertData(requestTime,getFeiYunCount(),"feiyun")
	insertData(requestTime,getShiHouCount(),"shihou")
#	insertData(requestTime,getLanShaCount(),"lansha")
	insertData(requestTime,getDaShenCount(),"dashen")
	insertData(requestTime,get5kongCount(),"5kong")
	# insertData(requestTime,getHaZhiBoCount(),"hazhibo")
	insertData(requestTime,getQiECount(),"QiE")
	time.sleep(300)