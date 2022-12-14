""" 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer. """

# py ch09e04_dictionaries.py

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = {}
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        for word in words:
            if '@' in word:
                counts[word] = counts.get(word, 0) + 1


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


print(keywithmaxval(counts), max(counts.values()))
