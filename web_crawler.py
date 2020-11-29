import pandas as pd
tables = pd.read_csv('D:/eva_python/cctv_2.csv', encoding = 'utf-8')
tables.columns = ['location','city','weburl','size']
#print (tables)

weburl = tables.pop('weburl')
#print(weburl)

import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Chrome/67.0.3396.99')]

    
import cv2
import requests
from bs4 import BeautifulSoup

#print('start：')

for weburls in weburl:
    tempUrl = weburls
    html = requests.get(weburls)
    sp = BeautifulSoup(html.text, 'html.parser')
    imgurl = sp.find_all(['img'] )
    for img in imgurl:
        href = img.get('src' )
        print(href)
    try : 
        vcap = cv2.VideoCapture(href)
        width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("OK_Image Size: %d x %d" % (width, height))
        #(width, height) = tables.iloc[ : , 3]
        
    except :
        print('No url')


#newcctv = new
#newcctv.to_csv("newcctv.csv", encoding = "utf-8", index = True)
