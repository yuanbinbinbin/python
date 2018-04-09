import websocket
import thread
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "### open ###"
    ws.send('{"type":"set_platform","data":{"imei":"03cd3f65cbdd71b47f88cb96dbdb45","os":"Windows","version":"1.0.1","bundle":"web","tm":1517214661666,"tk":"888f55e2","pid":1411}}')
    # ws.send('{"type":"set_platform","data":{"imei":"03cd3f65cbdd71b47f88cb96dbdb45b5","os":"Windows","version":"1.0.1","bundle":"web","tm":1518254194857,"tk":"bd342778","pid":1141}}')
    # def run(*args):
    #     for i in range(10):
    #         time.sleep(1)
    #         ws.send("Hello %d" % i)
    #     time.sleep(1)
    #     ws.close()
    #     print "thread terminating..."
    # thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://jhassistorws.wlanbanlv.com/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()



# from socketIO_client import SocketIO  
# import logging  
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# logging.getLogger('requests').setLevel(logging.WARNING)  
# logging.basicConfig(level=logging.DEBUG) 

# # hosts = 'http://danmu.feiyun.tv?room=334584'  
# hosts = 'https://selab.baidu.com/nv/answer.sock/?xc=fa4817022597a45e64cb9aa6f1940922&EIO=3&transport=websocket'

# def on_message(*args):  
#     # print "recv:", args  
#     # print "geted:", type(args[0])  
#     if type(args[0]) is types.DictType:  
#         rp = args[0]  
#         print "recv:", rp  
  
# sk = SocketIO(hosts)  
# # sk = SocketIO(hosts,port=port,params={'token': 'ksdjfkjdf'})  #create connection with params  
  
# # add lisenter for message response  
# sk.on('message', on_message)  

# # data = {  
# #      "sn": 0,  
# #      "ver": 2}  
# # # send data to message  
# # sk.emit('message', data, on_message)   
# # sk.sendf(data, on_message) # default send data to message  
# # #send data to login  
# # sk.emit('login', data, on_message)   
  
# sk.wait_for_callbacks(seconds=1)  

# # https://selab.baidu.com/nv/answer.sock/?xc=fa4817022597a45e64cb9aa6f1940922&EIO=3&transport=websocket   
# # https://selab.baidu.com/nv/answer.sock/?xc=fa4817022597a45e64cb9aa6f1940922&EIO=3&transport=websocket
# # https://selab.baidu.com/nv/answer.sock/?xc=fa4817022597a45e64cb9aa6f1940922&EIO=3&transport=websocket