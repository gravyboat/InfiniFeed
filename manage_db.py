#!/usr/bin/python
"""
manages our database, allowing us to add entries to the database.
"""

class dbQuery(object):
    def __init__(self, dbName = 'rss_feeder.db'):
        self.dbName = dbName

    # Adds items to the podcast table.
    def updatePodcast(self, ID, name, url):
        self.ID = ID
        self.name = name
        self.url = url

    # Adds items to the downloadLib table.
    def updateDownloadLib(self):
