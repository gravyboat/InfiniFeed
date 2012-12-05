#!/usr/bin/python
"""
manages our database, allowing us to add entries to the database.
"""

class dbQuery(object):
    def __init__(self, dbName = 'rss_feeder.db'):
        self.dbName = dbName

    # Adds items to the podcasts table.
    def updatePodcasts(self, ID, name, url):
        self.ID = ID
        self.name = name
        self.url = url
        self.dbConn = sqlite3.connect(self.dbName)
        self.c = self.dbConn.cursor()
        self.c.execute('''INSERT INTO podcasts (id, name, url) values (?, ?, ?)''', (self.ID, self.name, self.url))
        self.dbConn.commit()

    # Adds items to the downloads table.
    def updateDownloads(self, ID, name, url):
        self.ID = ID
        self.name = name
        self.url = url

    # Adds items to the podcasts_downloads table.
    def updateRelations(self, PID, DID):
        self.PID = PID
        self.DID = DID

