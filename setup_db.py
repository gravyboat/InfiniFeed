#!/usr/bin/python3
"""
Creates the database that is used by the application.
"""

import sqlite3

# Initial db and podcast table creation needs to be in a function.
class dbSetup(object):
    
    def __init__(self, dbName = 'rss_feeder.db'):
        self.dbName = dbName
    
    # Creation function that setups the podcast table.
    
    def createPodcasts(self):
        self.dbConn = sqlite3.connect(self.dbName)
        self.c = self.dbConn.cursor()

        self.c.execute('''CREATE TABLE if not EXISTS podcasts (
                id INTEGER PRIMARY KEY not NULL,
                name TEXT,
                url TEXT)''')
        self.dbConn.commit()

    # Creation function that handles setting up the downloads table.
    def createDownloads(self):
        self.dbConn = sqlite3.connect(self.dbName)
        self.c = self.dbConn.cursor()
        self.c.execute('''CREATE TABLE if not EXISTS downloads (
                id INTEGER PRIMARY KEY not NULL,
                name TEXT,
                url TEXT)''')
        self.dbConn.commit()

    # creation function that handles setting up the relations table to
    # link the podcasts and downloads.
    def createRelations(self):
        self.dbConn = sqlite3.connect(self.dbName)
        self.c = self.dbConn.cursor()
        self.c.execute('''CREATE TABLE if not EXISTS podcasts_downloads (
                podcasts_id INTEGER,
                downloads_id INTEGER)''')
        self.dbConn.commit()

setup = dbSetup()
setup.createPodcasts()
setup.createDownloads()
setup.createRelations()
