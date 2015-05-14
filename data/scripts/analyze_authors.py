import csv
import nltk
from nltk import word_tokenize
from nltk import FreqDist

def analyzeAuthors():

    authors = []
    with open('../top100clean.csv', 'rb') as bookfile:
        reader = csv.reader(bookfile)
        for row in reader:
            authors.append(row[4])

    authorset = nltk.Text(authors)
    fd = FreqDist(authorset)
    prolific = fd.most_common(10)
    for k, v in prolific:
        print str(k) + "\t" + str(v)

analyzeAuthors()
