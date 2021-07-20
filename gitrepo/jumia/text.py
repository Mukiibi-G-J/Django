from bs4 import BeautifulSoup
import requests
import os
import random
# page = requests.get('https://www.jumia.ug/mattresses-box-springs/')
# page = requests.get('https://www.jumia.ug/wines/')
page = requests.get('https://www.jumia.ug/')
soup =BeautifulSoup(page.text, 'html.parser')


for image in soup.find_all('img'):
    img_name = random.randrange(1,500)
    full_name = str(img_name)
    link = image['data-src']
    with open(full_name + '.jpg','wb') as f:
        im = requests.get(link)
        f.write(im.content) 