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