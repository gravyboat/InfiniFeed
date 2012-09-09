#!/usr/python  

"""pulls down files from an rss feed"""

from bs4 import BeautifulSoup
import sys
import os
import urllib.request


saveDir = 'files'
pageToScrape = 'http://feeds.ign.com/ignfeeds/podcasts/beyond/'

scrapedPage = urllib.request.urlopen(pageToScrape).read()
soup = BeautifulSoup(scrapedPage)

for link in soup.find_all('enclosure'):
    fixedUrl = (link.get('url'))
    print(fixedUrl)
    fileName = urllib.request.url2pathname(fixedUrl).rpartition('/')
    print(fileName[2])

    if os.path.isfile(saveDir + '/' + fileName[2]):
        print(fileName[2] + ' alread exists!')
    else:
        readItIn = urllib.request.urlopen(str(fixedUrl))
        output = open(saveDir + '/' + fileName[2], 'wb')
        output.write(readItIn.read())
        output.close()
