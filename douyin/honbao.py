#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests  
import json
import httplib,urllib2,cookielib
import time
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import StringIO, gzip
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def gzdecode(data) :  
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()
    return data2

def getRedPacket(aweme_id):
	times = (int(round(time.time() * 1000)))
	url = "https://aweme.snssdk.com/aweme/v1/lucky/money/seckill/?os_api=22&device_type=vivo+X6D&device_platform=android&ssmix=a&iid=25848143126&manifest_version_code=174&dpi=480&uuid=868808022801374&version_code=174&app_name=aweme&version_name=1.7.4&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1742&aid=1128&channel=update&_rticket=1518144266346&ts=1518144271&as=a1457077cf20eaab3d7841&cp=070dad5cfbde75bde1yavl&mas=00dea63b2d65521a8d27983f550e0bea268c2c1cec26cc468686a6"
	      # https://aweme.snssdk.com/aweme/v1/lucky/money/scramble/?os_api=22&device_type=vivo+X6D&device_platform=android&ssmix=a&iid=25848143126&manifest_version_code=174&dpi=480&uuid=868808022801374&version_code=174&app_name=aweme&version_name=1.7.4&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1742&aid=1128&channel=update&_rticket=1518145264682&ts=1518145269&as=a1158067b5dfface1d1128&cp=01f9ae5a54df7eece1zkqm&mas=00771ec96c771e9482f429e5a5faa68ec41c4c8c8c268ca6c68666
	      # https://aweme.snssdk.com/aweme/v1/lucky/money/scramble/?os_api=22&device_type=vivo+X6D&device_platform=android&ssmix=a&iid=25848143126&manifest_version_code=174&dpi=480&uuid=868808022801374&version_code=174&app_name=aweme&version_name=1.7.4&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1742&aid=1128&channel=update&_rticket=1518145635105&ts=1518145639&as=a13571172716ca504d3718&cp=1d68a75277d17e01e1yood&mas=0004838bbc2972a70da147ab9b858f0f4e1c8ceccc262c0cac86c6
	headers = {
		'Accept-Encoding':'gzip',
		'Cache-Control':'max-stale=0',
		'Content-Type':'application/x-www-form-urlencoded',
		'Connection':'Keep-Alive',
		'Cookie':'odin_tt=3e4f51062841f621b2844123ea82c1d926296bf1e5ca6689b66487ed0c0e74ee2dcde7d613f8bdfd39afcb3a09006efb; sid_guard=198ce94c38474dcb237902afa5ceed69%7C1518105613%7C2592000%7CSat%2C+10-Mar-2018+16%3A00%3A13+GMT; uid_tt=4c5634c998aa267f819a3f6aa150d00d; sid_tt=198ce94c38474dcb237902afa5ceed69; sessionid=198ce94c38474dcb237902afa5ceed69; qh[360]=1; install_id=25848143126; ttreq=1$cf0e02bc20619946844f1aa80ed86224c0e1591e',
		'User-Agent':'okhttp/3.8.1'
	}
	param = 'aweme_id='+str(aweme_id)+'&source=1&retry_type=no_retry&os_api=22&device_type=vivo%20X6D&device_platform=android&ssmix=a&iid=25848143126&manifest_version_code=174&dpi=480&uuid=868808022801374&version_code=174&app_name=aweme&version_name=1.7.4&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1742&aid=1128&channel=update&_rticket='+str(times)
		   # aweme_id=6520161705576631566&source=1&retry_type=no_retry&os_api=22&device_type=vivo%20X6D&device_platform=android&ssmix=a&iid=25848143126&manifest_version_code=174&dpi=480&uuid=868808022801374&version_code=174&app_name=aweme&version_name=1.7.4&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1742&aid=1128&channel=update&_rticket=1518145264682
		   # aweme_id=6520178379122019597&source=1&retry_type=no_retry&os_api=22&device_type=vivo%20X6D&device_platform=android&ssmix=a&iid=25848143126&manifest_version_code=174&dpi=480&uuid=868808022801374&version_code=174&app_name=aweme&version_name=1.7.4&openudid=b166a679fbac05fc&device_id=38596006049&resolution=1080*1920&os_version=5.1&language=zh&device_brand=vivo&ac=wifi&update_version_code=1742&aid=1128&channel=update&_rticket=1518145635105
	request = urllib2.Request(url = str(url),data = param,headers = headers)
	r = urllib2.urlopen(request).read()

	print gzdecode(r)

def listRedPacket():
	url = 'https://api.amemv.com/aweme/v1/challenge/fresh/aweme/?ch_id=1590457092456462&cursor=20&count=20&type=5&retry_type=no_retry&iid=25848143126&device_id=38596006049&ac=wifi&channel=update&aid=1128&app_name=aweme&version_code=174&version_name=1.7.4&device_platform=android&ssmix=a&device_type=vivo+X6D&device_brand=vivo&language=zh&os_api=22&os_version=5.1&uuid=868808022801374&openudid=b166a679fbac05fc&manifest_version_code=174&resolution=1080*1920&dpi=480&update_version_code=1742&_rticket=1518146480152&ts=1518146485&as=a12521f7f54b1ac3bd7051&cp=15b8ae5956d57d38e1cpzu&mas=00160ba9a8097c470872d44ff9400a3abe8cac0cec2646ccc6868c'
	headers = {
		'Accept-Encoding':'gzip',
		'Cache-Control':'max-stale=0',
		'Content-Type':'application/x-www-form-urlencoded',
		'Connection':'Keep-Alive',
		'Cookie':'odin_tt=3e4f51062841f621b2844123ea82c1d926296bf1e5ca6689b66487ed0c0e74ee2dcde7d613f8bdfd39afcb3a09006efb; sid_guard=198ce94c38474dcb237902afa5ceed69%7C1518105613%7C2592000%7CSat%2C+10-Mar-2018+16%3A00%3A13+GMT; uid_tt=4c5634c998aa267f819a3f6aa150d00d; sid_tt=198ce94c38474dcb237902afa5ceed69; sessionid=198ce94c38474dcb237902afa5ceed69; qh[360]=1; install_id=25848143126; ttreq=1$cf0e02bc20619946844f1aa80ed86224c0e1591e',
		'User-Agent':'okhttp/3.8.1'
	}
	request = urllib2.Request(url = str(url),data = None,headers = headers)
	r = urllib2.urlopen(request).read()

	return gzdecode(r)




# 获取红包
redPackets = listRedPacket()
redPackets = json.loads(redPackets)

for item in redPackets['aweme_list']:
	print str(item['author_user_id'])
	print str(item['aweme_id'])
	print '------------'