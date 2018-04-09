#coding=utf-8
import requests
import json
import time
import pymysql as mdb
import re
import hashlib
import hmac
import base64

parameters = {
'snake_sign':"0umivmO3gLTtwpbR0nhK0V4VVis=",
'device_id':'imei_357092066902285_uuid_148143757554042336',
'push_id':'111111111222222223333333344444444',
'length':2508,
'version_code':2044,
'channel':'newTencent',
'kill':37,
'version':'3.3',
'platform':2,
'sid':'5b5a945c20116f5197586896e13fc95e',
'market':'newTencent',
'uid':'eafd3e45-fca1-4edb-bab8-5b47898b40e8',
'name':'飞云TV、bin',
'game_mode':2,
'push_channel':2
}
# parameters = {
# 'snake_sign':"kM0sLL88kGl3pmp064RURzxUxjE=",
# 'device_id':'6966B187-94BA-4E3A-BC20-735CE90FEE49-693-0000014E8EEC54CE',
# 'push_id':'+E6U6TXUHGuW3lYoeTbIVUUjFEtrsFRCtSqet0MHBeo=',
# 'length':4203,
# 'version_code':2004,
# 'channel':'apple',
# 'kill':117,
# 'version':'3.1',
# 'platform':1,
# 'sid':'e77fb71aa35a5b7dcc506bf2e95d231d',
# 'market':'apple',
# 'uid':'e0993ab9-a3b0-4cae-b317-1506790cd0a5',
# 'game_mode':1,
# 'push_channel':1
# }
shihou = (requests.post("http://snakeapi2.afunapp.com/top_list_v2/update_score",data=parameters)).text
print shihou
