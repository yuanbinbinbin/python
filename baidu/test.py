from socketIO_client import SocketIO  
import logging  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
logging.getLogger('requests').setLevel(logging.WARNING)  
logging.basicConfig(level=logging.DEBUG) 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# hosts = 'http://danmu.feiyun.tv?room=334584'  
hosts = 'https://selab.baidu.com/nv/xiguashipin/answer'
def ackSend(data):
	ack = {sn:data.sn,timestamp: data.timestamp, step:data.step}
	sk.emit('answer-ack', ack, on_message)

def on_message(*args):  
    print "recv:", args  
    # print "geted:", type(args[0])  
    # if type(args[0]) is types.DictType:  
    #     rp = args[0]  
    #     print "recv:", rp  

params = {'path':'/nv/answer.sock','transports':'["websocket"]','query':'{"xc":"fa4817022597a45e64cb9aa6f1940922"}'}  
sk = SocketIO(hosts,port=443,params=params)

# sk = SocketIO(hosts,port=port,params={'token': 'ksdjfkjdf'})  #create connection with params  
  
# add lisenter for message response  
sk.on('answer', on_message)  

# data = {  
#      "sn": 0,  
#      "ver": 2}  
# # send data to message  
# sk.emit('message', data, on_message)   
# sk.sendf(data, on_message) # default send data to message  
# #send data to login  
# sk.emit('login', data, on_message)   
  
sk.wait_for_callbacks(seconds=1)  