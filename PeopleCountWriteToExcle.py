#coding=utf8
import xlwt
import pymysql as mdb
import time
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt
startTime = '2017-04-20'
endTime = '2017-04-21'
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet 1')

conn = mdb.connect(host='localhost',user='root',passwd='123456',db='db_data_platform',port=3306)
cur = conn.cursor()		
cur.execute("select * from tb_people_count where DATE_FORMAT(get_time,'%Y-%m-%d') >= '"+startTime+"' and DATE_FORMAT(get_time,'%Y-%m-%d') < '" + endTime+"'")
results = cur.fetchall()

sheet1.write(0,0,"时间".decode('utf8'))
sheet1.write(0,1,'触手'.decode('utf8'))
sheet1.write(0,2,'飞云'.decode('utf8'))
sheet1.write(0,3,'狮吼'.decode('utf8'))
sheet1.write(0,4,'大神'.decode('utf8'))
sheet1.write(0,5,'悟空'.decode('utf8'))
sheet1.write(0,6,'哈直播'.decode('utf8'))
sheet1.write(0,7,'企鹅'.decode('utf8'))

rowNum = 0
columnNum = 0
datatime = ""
for row in results:
	if datatime != row[0].strftime('%Y-%m-%d %H:%M:%S'):
		datatime = row[0].strftime('%Y-%m-%d %H:%M:%S')
		rowNum = rowNum + 1
		sheet1.write(rowNum,0,datatime)
	if row[2] == 'chushou':
		sheet1.write(rowNum,1,row[1])
	if row[2] == 'feiyun':
		sheet1.write(rowNum,2,row[1])
	if row[2] == 'shihou':
		sheet1.write(rowNum,3,row[1])
	if row[2] == 'dashen':
		sheet1.write(rowNum,4,row[1])
	if row[2] == '5kong':
		sheet1.write(rowNum,5,row[1])
	if row[2] == 'hazhibo':
		sheet1.write(rowNum,6,row[1])
	if row[2] == 'QiE':
		sheet1.write(rowNum,7,row[1])
cur.close()
conn.close()
book.save('D:\user_count.xls')