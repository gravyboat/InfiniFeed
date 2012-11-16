#!/usr/bin//python3
"""
Creates the database that is used by the application.
"""

import sqlite3

# Initial db and podcast table creation needs to be in a function.
def podcasts(url, shortname)
	dbConn = sqlite3.connect('rss_feeder.db')

	c = dbConn.cursor()

	c.execute('''create table podcasts (
			pid	int	primary key not NULL,
			name	text,
			url	text)''')
	c.commit()

# Creation function that handles adding new direct podcast links.

def downloadLinks(url, shortname):
	dbConn = sqlite3.connect('rss_feeder.db')
	c = dbConn.cursor()
	c.execute('''create table downloadLib (
			did	int	primary key not NULL,
			name	text,
			url	text)''')
	c.commit

