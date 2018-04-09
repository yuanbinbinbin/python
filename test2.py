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
	sqlS = "select room_id from tb_user_shihou where room_id = '"+str(room_id)+"'"
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
def updateData(room_id,nickname,fans_count,notice,detail,class_name):
	try:
		print "update: "+str(room_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		Sqq = "update tb_user_shihou set nickname ='"+str(nickname)+"', fans_count = "+str(fans_count)+", notice = '"+str(notice)+"', master_detail = '"+str(detail)+"', class_name = '"+str(class_name)+"' where room_id = '" +str(room_id)+"'"
		cur.execute(Sqq)
	#	cur.execute("update tb_user_ha set nickname = %s,fans_count = %s,video_count = %s ,notice = %s, class_name = %s where room_id = %s",,(nickname,fans_count,video_count,notice,class_name,room_id))
		cur.close()
		conn.commit()
		conn.close()
	except Exception,e : print("error updateData"+str(e)+" roomid "+ str(room_id))

def insertData(room_id,nickname,fans_count,notice,detail,class_name):
	try:
		print "insertData: "+str(room_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		cur.execute("insert into tb_user_shihou values(%s,%s,%s,%s,%s,%s)",(room_id,nickname,fans_count,notice,detail,class_name))
		conn.commit()
		cur.close()
		conn.close()
	except Exception,e : print("error insertData"+str(e)+" roomid " + str(room_id))

j = 16000
end = 16100
i = 0
while(j <= end) :
	print j
	try:
		sjson = (requests.get("http://api.shihou.tv/api/room?room_id="+str(j))).text
		result = json.loads(sjson)
		if result["error"] == 0:
			if result["data"]["notice"] != "" or result["data"]["master_detail"] != "": 
				if isExist(result["data"]["room_id"]):
					updateData(result["data"]["room_id"],result["data"]["nick_name"],result["data"]["follow_number"],result["data"]["notice"],result["data"]["master_detail"],result["data"]["game_name"])
				else:
					i += 1
					insertData(result["data"]["room_id"],result["data"]["nick_name"],result["data"]["follow_number"],result["data"]["notice"],result["data"]["master_detail"],result["data"]["game_name"])
	except Exception,e : print("error main"+str(e))
	j += 1
	time.sleep(10)
print "共导入数据: "+str(i)+"条"

