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
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet 1')

conn = mdb.connect(host='localhost',user='root',passwd='123456',db='db_data_platform',port=3306)
cur = conn.cursor()		
cur.execute("select * from tb_user_lansha where count > 0 ORDER BY count DESC")
results = cur.fetchall()
sheet1.write(0,0,'id')
sheet1.write(0,1,"用户名".decode('utf8'))
sheet1.write(0,2,'粉丝数'.decode('utf8'))
sheet1.write(0,3,'公告'.decode('utf8'))
sheet1.write(0,4,'游戏分类'.decode('utf8'))
sheet1.write(0,5,'写入时间'.decode('utf8'))
sheet1.write(0,6,'EncodeID')
sheet1.write(0,7,'JSON')

i = 1
for row in results:
	for j in range(0,8):
		if j == 5:
			if row[j] == None:
				sheet1.write(i,j,"")
			else:
				sheet1.write(i,j,row[j].strftime('%Y-%m-%d %H:%M:%S'))
		else:
			sheet1.write(i,j,row[j])
	i = i + 1
cur.close()
conn.close()
book.save('D:\lansha_user_20161202.xls')