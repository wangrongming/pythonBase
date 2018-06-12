from urllib.parse import urlencode
import json
from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup
import re
import os
import pymongo
from hashlib import md5
from config import *

client  = pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]


def get_page_index(offset,KEYCORD):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': KEYCORD,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错')
        return None

def download_image(url):
    print('Downloading',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except ConnectionError:
        return None

def save_image(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()

def pase_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield  item.get('article_url')

def get_page_detail(url):
    try:
        if url is not None:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return None
    except RequestException:
        print('请求详情页面出错')

def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title =soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.loads(result.group(1).replace('\\',''))
        if data and 'sub_images'in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            print(images)##########################
            for image in images:download_image(image)
            return {
                'title':title,
                'url':url,
                'images':images
            }
def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('Successfully Saved to Mongo',result)
        return True
    return False


def main(offset):
    html = get_page_index(offset,'街拍')
    for url in pase_page_index(html):
        html = get_page_detail(url)
        if html is not None:
            result=parse_page_detail(html,url)
            if result:save_to_mongo(result)

if __name__=='__main__':
    main(20)