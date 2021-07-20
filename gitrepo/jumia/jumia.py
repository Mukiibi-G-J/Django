import requests
from bs4 import BeautifulSoup
import os  
import urllib.request
import random

# page = requests.get('https://www.jumia.ug/mattresses-box-springs/')
page = requests.get('https://www.jumia.ug/catalog/?q=wines')
soup =  BeautifulSoup(page.content, 'html.parser')


for img in soup.find_all('img'):
    link = img.get('data-src')
    # # print(src)
    # img_name = random.randrange(1,500)
    # full_name = str(img_name) +  'jpg'
    # print(link)
    with open('full_name') as f:
        im = requests.get(link)
        f.write(im.content) 
    # urllib.request.urlretrieve(src, full_name)
    # print('loop br')