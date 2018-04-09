#coding=utf-8
import requests
import json
import time
import pymysql as mdb
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def isExist(room_id):
	sqlS = "select room_id from tb_user_ha where room_id = '"+str(room_id)+"'"
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
def updateData(room_id,nickname,fans_count,video_count,notice,class_name):
	try:
		print "update: "+str(room_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		Sqq = "update tb_user_ha set nickname ='"+str(nickname)+"', fans_count = "+str(fans_count)+", video_count = "+str(video_count)+", notice = '"+str(notice)+"', class_name = '"+str(class_name)+"' where room_id = '" +str(room_id)+"'"
		cur.execute(Sqq)
	#	cur.execute("update tb_user_ha set nickname = %s,fans_count = %s,video_count = %s ,notice = %s, class_name = %s where room_id = %s",,(nickname,fans_count,video_count,notice,class_name,room_id))
		cur.close()
		conn.commit()
		conn.close()
	except Exception,e : print("error updateData"+str(e)+" roomid "+ str(room_id))

def insertData(room_id,nickname,fans_count,video_count,notice,class_name):
	# print room_id
	# print(nickname)
	# print fans_count
	# print(video_count)
	# print notice
	# print class_name
	try:
		print "insertData: "+str(room_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		cur.execute("insert into tb_user_ha values(%s,%s,%s,%s,%s,%s)",(room_id,nickname,fans_count,video_count,notice,class_name))
		conn.commit()
		cur.close()
		conn.close()
	except Exception,e : print("error insertData"+str(e)+" roomid " + str(room_id))

room_limit = 1022168
j = 1020001
i = 0
try:
	while(j < room_limit) :
		roomid = j
		roominfo = (requests.get("http://api.hahabo.com/service/zhibo/room_info?room_id="+str(roomid)).text)
		roominfoResult = json.loads(roominfo)
		if roominfoResult["data"]["fans_count"] > 0:
			if isExist(roomid):
				updateData(roomid,roominfoResult["data"]["nickname"],roominfoResult["data"]["fans_count"],roominfoResult["data"]["video_count"],roominfoResult["data"]["notice"],roominfoResult["data"]["class_name"])
			else:
				i = i + 1
				insertData(roomid,roominfoResult["data"]["nickname"],roominfoResult["data"]["fans_count"],roominfoResult["data"]["video_count"],roominfoResult["data"]["notice"],roominfoResult["data"]["class_name"])
		j = j + 1
		print "-------------------------------------------------"+str(j)
		time.sleep(5)
except Exception,e : print("error main"+str(e))
print "共导入数据: "+str(i)+"条"

