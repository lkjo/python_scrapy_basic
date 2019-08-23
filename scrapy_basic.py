import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os
import sys
def download_image(articles):
    for j in articles:
        new_name = j.text.replace(":","")
        if not os.path.isdir(os.path.join('download',j.text or new_name)):
            os.mkdir(os.path.join('download',new_name))
        res = requests.get('https://www.ptt.cc'+j['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,os.path.join('download',new_name,ID))

def crawler(pages = 3):
    if not os.path.isdir('download'):
        os.mkdir('download')
    url = 'https://www.ptt.cc/bbs/GHIBLI/index.html'
    
    for i in range(pages):
        global reg_imgur_file
        reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        articles = soup.select('div.title a')
        paging = soup.select('div.btn-group-paging a')
        next_url = 'https://www.ptt.cc'+paging[1]['href']
        url = next_url
        download_image(articles)

"""
利用CMD去輸入參數值，agrv
"""
crawler(int(sys.argv[1]))


    
