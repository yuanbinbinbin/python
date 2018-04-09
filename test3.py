#coding=utf-8
import requests
import json
import time
import pymysql as mdb
import re
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def isExist(anchor_id):
	sqlS = "select anchor_id from tb_user_qie where anchor_id = '"+str(anchor_id)+"'"
	length = 0
	try:
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		cur.execute(sqlS)
		results = cur.fetchall()
		for row in results:
			length = length + 1
		cur.close()
		conn.close()
		if length > 0:
			return True
		else:
			return False
	except Exception,e : print("error isExist"+str(e))
	return False
def updateData(anchor_id,nick_name,game,brief,sex,fans_count,video_count,registerTime,country,province,city,requestTime):
	try:
		#print "update: "+str(anchor_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		Sqq = "update tb_user_qie set nick_name ='"+str(nick_name)+"', game = '"+str(game)+"', brief = '"+str(brief)+"', sex = '"+str(sex)+"', fans_count = "+str(fans_count)+", video_count = "+str(video_count)+", country = '"+str(country)+"', province = '"+str(province)+"', city = '"+str(city)+"', last_time = '"+str(requestTime)+"' where anchor_id = '" +str(anchor_id)+"'"
		cur.execute(Sqq)
	#	cur.execute("update tb_user_ha set nickname = %s,fans_count = %s,video_count = %s ,notice = %s, class_name = %s where room_id = %s",,(nickname,fans_count,video_count,notice,class_name,room_id))
		cur.close()
		conn.commit()
		conn.close()
	except Exception,e : print("error updateData"+str(e)+" roomid "+ str(anchor_id))

def insertData(anchor_id,nick_name,game,brief,sex,fans_count,video_count,registerTime,country,province,city,requestTime):
	# print room_id
	# print(nickname)
	# print fans_count
	# print(video_count)
	# print notice
	# print class_name
	try:
		print "insertData: "+str(anchor_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		cur.execute("insert into tb_user_qie values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(anchor_id,nick_name,game,brief,sex,fans_count,video_count,registerTime,country,province,city,requestTime))
		conn.commit()
		cur.close()
		conn.close()
	except Exception,e : print("error insertData"+str(e)+" roomid " + str(anchor_id))
page_num = 0
page_size = 50
arr = []
j = page_size
requestTime = time.localtime()
while True:
	insertCount = 0
	j = page_size
	page_num = 0
	requestTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	del arr[:]
	try:
		while j >= page_size:
			page_num = page_num + 1
			qiEParameters = {'param':"{\"0\":{\"module\":\"pgg_live_read_svr\",\"method\":\"get_live_list\",\"param\":{\"layout_id\":\"hot\",\"page_num\":"+str(page_num)+",\"page_size\":"+str(page_size)+",\"other_uid\":0}}}",'app_info':"{\"platform\":4,\"terminal_type\":2,\"egame_id\":\"egame_official\"}"}
			qie = (requests.post("http://share.egame.qq.com/cgi-bin/pgg_skey_async_fcgi?&cgi_method=get_live_list&g_tk=832538900",data=qiEParameters)).text
			result = json.loads(qie)
			j = len(result["data"]["0"]["retBody"]["data"]["live_data"]["live_list"])
			for item in result["data"]["0"]["retBody"]["data"]["live_data"]["live_list"]:
				arr.append(item["anchor_id"])
		for items in arr:
			parameter12 = {'param':"{\"0\":{\"module\":\"pgg_live_read_svr\",\"method\":\"get_live_and_profile_info\",\"param\":{\"anchor_id\":"+str(items)+"}}}",'app_info':"{\"platform\":4,\"terminal_type\":2,\"egame_id\":\"egame_official\"}"}
			info = (requests.post("http://share.egame.qq.com/cgi-bin/pgg_barrage_async_fcgi?&cgi_method=get_barrage&g_tk=796800133",data=parameter12)).text
			resultInfo = json.loads(info)
			info1 = resultInfo["data"]["0"]["retBody"]["data"]["profile_info"]
			info2 = resultInfo["data"]["0"]["retBody"]["data"]["video_info"]
			sex = "女"
			if info1["sex"] == 1:
				sex = "男"
			if isExist(items):
				updateData(info2["anchor_id"],info1["nick_name"],info2["appname"],info1["brief"],sex,info1["fans_count"],info1["video_count"],time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((info1["register_ts"]))),info1["country"],info1["province"],info1["city"],requestTime)
			else:
				insertCount = insertCount + 1
				insertData(info2["anchor_id"],info1["nick_name"],info2["appname"],info1["brief"],sex,info1["fans_count"],info1["video_count"],time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((info1["register_ts"]))),info1["country"],info1["province"],info1["city"],requestTime)
	except Exception,e :print str(e)
	print(insertCount)
	time.sleep(300)	
#2346742
