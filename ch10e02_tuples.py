"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

# py ch10e02_tuples.py

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = {}
for line in fh :
    if not line.startswith('From '): 
        continue
    else:
        words = line.split()
        for word in words:
            if not ':' in word:
                continue
            else:
                hour = word[0:2]
                counts[hour] = counts.get(hour, 0) + 1

c = sorted(counts.items())

for (k, v) in c:
    print(k, v)