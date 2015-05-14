import csv
import nltk
from nltk import word_tokenize
from nltk import FreqDist

def analyzeTitles():
    fulltitles = []
    titles = []
    with open('../top100clean.csv', 'rb') as bookfile:
        reader = csv.reader(bookfile)
        for row in reader:
            if "..." in row[0]:
                row[0] = " ".join(row[0].split(" ")[:-1])
            words = nltk.word_tokenize(row[0])
            for w in words:
                if w.isalpha() and w.lower() not in ['the','a']:
                    titles.append(w.lower())
            fulltitles.append(row[0])

    titleset = nltk.Text(titles)
    wordsintitle = [len(f.split(" ")) for f in fulltitles]
    wit_fd = FreqDist(wordsintitle)
    print "\nw.i.t.\tfreq"
    print "--------------------"
    for numwords, times in wit_fd.iteritems():
        print str(numwords) + "\t" + str(times)
    print "\n"

    print "\nword\t\tfreq"
    print "--------------------"
    fd = FreqDist(titleset)
    common_words = fd.most_common(25)
    for k, v in common_words:
        print str(k) + "\t\t" + str(v)

analyzeTitles()
