# To run this, download the BeautifulSoup zip file
# bs4.zip
# and unzip it in the same directory as this file

# py ch12e03_following_links.py

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1

# Retrieve all of the anchor tags
tags = soup('a')
while True:
    count -= 1
    if count < 0:
        break
    content_list = []
    for tag in tags:
        link = tag.get('href', None)
        content_list.append(link)
    new_link = content_list[pos]
    content_list.clear()
    print(count, new_link)
    url = new_link
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')