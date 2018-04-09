import requests  

keywords = {  
         'type':'avatar',  
         'pf':'web',  
         'cv':'3.5.11',
         'id':'WU_FILE_1',
         'type':'image/png'  
        }  


pictures = {    
	          'file':('Icon-192.png',open("E:\\QQ\\2460666162\\FileRecv\\logo(2)\\Icon-192.png",'rb'),'image/png')
           } 


url = "http://www.feiyun.tv/api/upload/image?type=avatar&pf=web&cv=3.5.11"  

r = requests.post(url, data = keywords ,files = pictures)  

print r.text