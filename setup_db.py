#!/usr/bin//python3
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

        self.c.execute('''create table if not exists podcasts (
                id int primary key not NULL,
                name text,
                url	text)''')
        self.dbConn.commit()

    # Creation function that handles setting up the downloads table.
    def downloadLinks(self):
        self.dbConn = sqlite3.connect(self.dbName)
        self.c = self.dbConn.cursor()
        self.c.execute('''create table if not exists downloadLib (
                id int primary key not NULL,
                name text,
                url	text)''')
        self.dbConn.commit()

setup = dbSetup()
setup.createPodcasts()
setup.downloadLinks()
