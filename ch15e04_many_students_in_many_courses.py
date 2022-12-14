"""This application will read roster data in JSON format, parse the file, and then produce an SQLite database that
contains a User, Course, and Member table and populate the tables from the data file.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data,
run the following SQL command:

SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

The output should look as follows:
    Zoya|si430|0
    Zofia|si430|0

Once that query gives the correct data, run this query:
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;

You should get one row with a string that looks like XYZZY53656C696E613333."""

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')  # checks access to the file or creates it
cur = conn.cursor()  # kinda like handle

# Do some setup
# role: 1 - teacher, 0 -student
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)  # loads = load string

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    # because we set names to be UNIQUE we need to add IGNORE so python won't blow up
    # INSERT OR IGNORE is SQLite syntax, won't work in other SQLs
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES ( ?, ?, ? )',
                ( user_id, course_id, role ) )

    conn.commit()  # write data into DB file (may take a while, so sometimes it is placed after loop or set up to write
    # every x times)