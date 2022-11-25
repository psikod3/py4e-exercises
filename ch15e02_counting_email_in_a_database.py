"""This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (
i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: emaildb.py.

The data file for this application is the same as in previous assignments: mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is
read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely
writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program,
there is a balance between the number of operations you execute between commits and the importance of not losing the
results of operations that have not yet been committed. """

import sqlite3
import re

conn = sqlite3.connect('organizationdb.sqlite')  # checking access to the file or creates it
cur = conn.cursor()  # kinda like handle

cur.execute('DROP TABLE IF EXISTS Counts')  # clean db in case that it already exists

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    org_list = re.findall("@(\S+)", line)
    org = org_list[0]
    # below line isn't reading any data yet, just checking structure and preparing for next step
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))  # ? to prevent sql injection; need to use tuple even just one item
    row = cur.fetchone()  # and this gets data from DB
    if row is None:  # if there is no row with given organization add it and start counting
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))  #
    else:  # update count if there is that organization already
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()  # write data into DB file (may take a while, so sometimes it is placed after loop or set up to write
    # every x times)

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
