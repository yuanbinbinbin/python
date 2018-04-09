#coding=utf-8
import requests
import json
import time
import pymysql as mdb
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

def isExist(room_id):
	sqlS = "select room_id from tb_user_shihou2 where room_id = '"+str(room_id)+"'"
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
def updateData(room_id,nickname,fans_count,notice,detail,class_name,last_bord):
	try:
		print "update: "+str(room_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		Sqq = "update tb_user_shihou2 set nickname ='"+str(nickname)+"', fans_count = "+str(fans_count)+", notice = '"+str(notice)+"', master_detail = '"+str(detail)+"', class_name = '"+str(class_name)+"' where room_id = '" +str(room_id)+"'"
		cur.execute(Sqq)
	#	cur.execute("update tb_user_ha set nickname = %s,fans_count = %s,video_count = %s ,notice = %s, class_name = %s where room_id = %s",,(nickname,fans_count,video_count,notice,class_name,room_id))
		cur.close()
		conn.commit()
		conn.close()
	except Exception,e : print("error updateData"+str(e)+" roomid "+ str(room_id))

def insertData(room_id,nickname,fans_count,notice,detail,class_name,last_bord,age,mobile):
	try:
		print "insertData: "+str(room_id)
		conn = mdb.connect(host="localhost",user="root",passwd="123456",db="db_data_platform",port=3306)
		cur = conn.cursor()
		cur.execute("insert into tb_user_shihou2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(room_id,nickname,fans_count,notice,detail,class_name,timestamp_datetime(last_bord),age,mobile))
		conn.commit()
		cur.close()
		conn.close()
	except Exception,e : print("error insertData"+str(e)+" roomid " + str(room_id))

has_more = 1
offset = 0
i = 0

while(has_more == 1) :
	try:
		j = 0
		parameters = {'keywords':'','offset':offset}
		sjson = (requests.post("http://api.shihou.tv/search/master",data=parameters)).text
		result = json.loads(sjson)
		if result["error"] == 0:#room_id,nickname,fans_count,notice,detail,class_name,last_bord
			has_more = result["data"]["master_block"]["has_more"]
			offset = result["data"]["master_block"]["offset"]
			resultList = result["data"]["master_block"]["list"]
			for item in resultList:
				if isExist(item["room"]["id"]):
					print("hhhhhhhhhhhh:" + str(item["room"]["id"]))
					j += 1
				else:
					i += 1
					insertData(item["room"]["id"],item["master"]["nick_name"],item["master"]["follow_number"],item["room"]["notice"],item["master"]["detail"],item["room"]["snapshot"],item["room"]["last_broad"],item["master"]["age"],item["master"]["mobile"])
		if j == 20:
			break
		offset = result["data"]["master_block"]["offset"]
	except Exception,e : print("error main"+str(e)+"  "+str(offset))
	time.sleep(15)
print "共导入数据: "+str(i)+"条"

