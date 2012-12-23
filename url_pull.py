#!/bin/python  

"""pulls down files from an rss feed after confirming their status in the database"""

from bs4 import BeautifulSoup
import sys
import os
import sqlite3
import urllib.request

class rssScraper(object):

    def __init__(self, dbName = 'rss_feeder.db'):
        self.dbName = dbName

    #This pulls down our page, and pulls all the mp3 file download links. then checks each entry to see if it already exists in the database.
    def pagePull(self, pageToScrape, saveDir):
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

pullIt = rssScaper()
pullIt.pagePull(pageToScrape = 'http://feeds.ign.com/ignfeeds/podcasts/beyond', saveDir = 'files')
