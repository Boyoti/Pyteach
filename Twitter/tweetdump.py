# tweetdump.py
# Filter tweets and extract specific information
# The filter is a regular expression given as a command line parameter

import sys
import re
import sqlite3

if len(sys.argv) < 2:
	print "Not enough parameters -- usage: tweetdump handle"
	sys.exit()
else:
	db = sys.argv[1]+".db"


# create a connection to the database
conn = sqlite3.connect(db)

# create a cursor object
c = conn.cursor()

#get the tweets

rows = c.execute("select text from tweet")


for row in rows:
	rowstr = " ".join(row) # convert row to a string
	if len(sys.argv) > 2:

		match = re.search(sys.argv[2]+'\w+',rowstr)
		if match:
			print match.group()
	else:
		try:
			print rowstr
		except:
			pass


