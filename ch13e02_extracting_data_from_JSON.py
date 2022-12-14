"""Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to json2.py. The program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute
the sum of the numbers in the file and enter the sum below:

The data consists of a number of names and comment counts in JSON as follows:

{ comments: [ { name: "Matthias" count: 97 }, { name: "Geomer" count: 97 } ... ] }

The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at
geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2..."""

# py ch13e02_extracting_data_from_JSON.py

import json
import urllib.request, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')  # http://py4e-data.dr-chuck.net/comments_1616384.json
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)  # loads = load string
print('Retrieving', url)
# print('Retrieved', len(info), 'characters')

comments = []
for item in info["comments"]:  # value of "comments" key is a list of dicts (items here)
    comment_count = item["count"]
    print('Count:', comment_count)
    comments.append(comment_count)

print('Sum:', sum(comments))

