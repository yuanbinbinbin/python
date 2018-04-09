#coding:utf8

from flask import Blueprint, current_app, render_template,request
import charts
import pymysql
import time

pc = Blueprint("pc",__name__)

feiyundata = []
chushoudata = []
shihoudata = []
lanshadata = []
dashendata = []
wukongdata = []
hazhibodata = []
qiedata = []
getTime = []

@pc.route('/index')
def index():
	del feiyundata[:]
	del chushoudata[:]
	del shihoudata[:]
	del lanshadata[:]
	del dashendata[:]
	del wukongdata[:]
	del hazhibodata[:]
	del qiedata[:]
	del getTime[:]
	start = request.args.get('start')
	end = request.args.get('end')
	sqlDate = ""
	if start == None:
		sqlDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	else:
		sqlDate = start
	if end != None:
		sqlDate = "DATE_FORMAT(get_time,'%Y-%m-%d') >= '"+sqlDate +" 'and DATE_FORMAT(get_time,'%Y-%m-%d') <= '"+end+"'"
	else:
		sqlDate = "DATE_FORMAT(get_time,'%Y-%m-%d') = '"+sqlDate+"'"
	sqlS = "SELECT DATE_FORMAT(get_time,'%Y-%m-%d %H') as ttt ,avg(count) from tb_people_count where "+sqlDate
	try:
		conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='db_data_platform',port=3306)
		cur = conn.cursor()
		#cur.execute("select DATE_FORMAT(get_time,'%d-%H'),AVG(count) from tb_people_count where platform = 'feiyun' GROUP BY DATE_FORMAT(get_time,'%d-%H')")
		#print sqlS+" and platform = 'feiyun' group by ttt"
		cur.execute(sqlS+" and platform = 'feiyun' group by ttt")
		results = cur.fetchall()
		for row in results:
			getTime.append(row[0])
			feiyundata.append(int(row[1]))

		cur.execute(sqlS+" and platform = 'chushou' group by ttt")
		results = cur.fetchall()
		for row in results:
			chushoudata.append(int(row[1]))

		cur.execute(sqlS+" and platform = 'shihou' group by ttt")
		results = cur.fetchall()
		for row in results:
			shihoudata.append(int(row[1]))

		cur.execute(sqlS+" and platform = 'lansha' group by ttt")
		results = cur.fetchall()
		for row in results:
			lanshadata.append(int(row[1]))

		cur.execute(sqlS+" and platform = 'dashen' group by ttt")
		results = cur.fetchall()
		for row in results:
			dashendata.append(int(row[1]))

		cur.execute(sqlS+" and platform = '5kong' group by ttt")
		results = cur.fetchall()
		for row in results:
			wukongdata.append(int(row[1]))

		cur.execute(sqlS+" and platform = 'hazhibo' group by ttt")
		results = cur.fetchall()
		for row in results:
			hazhibodata.append(int(row[1]))

		cur.execute(sqlS+" and platform = 'QiE' group by ttt")
		results = cur.fetchall()
		for row in results:
			qiedata.append(int(row[1]))

		results.close()
		cur.close()
		conn.close()
	except:
		print('Error')
	return render_template('peopleCount.html')

@pc.route('/feiyun')
def feiyun():
	mchart = charts.SplineChart(title="直播平台各个时间段人数", subtitle="",div_id ='feiyun')
	mchart.setyAxistitle('人数')
	mchart.setxAxiscategories(getTime)
	mchart.setseries({
		'name':'飞云',
		'data':feiyundata
		})
	mchart.setseries({
		'name':'触手',
		'data':chushoudata
		})
	mchart.setseries({
		'name':'狮吼',
		'data':shihoudata
		})
	mchart.setseries({
		'name':'蓝鲨',
		'data':lanshadata
		})
	mchart.setseries({
		'name':'大神',
		'data':dashendata
		})
	mchart.setseries({
		'name':'悟空',
		'data':wukongdata
		})
	mchart.setseries({
		'name':'哈直播',
		'data':hazhibodata
		})
	mchart.setseries({
		'name':'企鹅电竞',
		'data':qiedata
		})
	return mchart.dumps()
	
@pc.route('/chushou')
def chushou():

	mchart = charts.SplineChart(title="触手TV各个时间段人数", subtitle="",div_id ='chushou')
	mchart.setyAxistitle('人数')
	mchart.setxAxiscategories(getTime)
	mchart.setseries({
		'name':'chushou',
		'data':chushoudata
		})
	return mchart.dumps()
