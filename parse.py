## by Allison Nelson

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
from nltk.corpus import stopwords
import nltk, re, pprint
from nltk import word_tokenize

def prepFile(filename):
    # prep file
    with codecs.open(filename, 'r', 'utf-8') as book:
        raw = book.read()
        stop = stopwords.words('english')
        # the normal tokenized file
        tokens = word_tokenize(raw)

        # this stuff weeds out the stopwords/overly common words
        # to get a more meaningful freqdist
        nostops = [w for w in tokens if w not in stop]
        nostops = [w for w in nostops if w.isalpha()]
        nostops = [w.lower() for w in nostops]
        extra_stops = ['said','he','she','i', 'the', 'a', 'and', 'it']
        nostops = [w for w in nostops if w not in extra_stops]

        ns_text = nltk.Text(nostops)
        text = nltk.Text(tokens)
        return text,ns_text

def describe(text):
    
    # most common phrases that occur together
    text.collocations(50)
    # most common words
    fd = nltk.FreqDist(text)
    print fd.most_common(50)

text, ns_text = prepFile(sys.argv[1])
# this is the original text
describe(text)
print "\n"
# this one has a lot of common words taken out
describe(ns_text)

