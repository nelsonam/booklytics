## by Allison Nelson

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
from nltk.corpus import stopwords
import nltk, re, pprint
from nltk import word_tokenize
from textstat.textstat import textstat

def prepFile(filename):
    # prep file
    with codecs.open(filename, 'r', 'utf-8') as book:
        raw = book.read()
        stop = stopwords.words('english')
        # the normal tokenized file
        tokens = word_tokenize(raw)
        
        nopunct = [w for w in tokens if w.isalpha()]

        # this stuff weeds out the stopwords/overly common words
        # to get a more meaningful freqdist
        nostops = [w for w in tokens if w not in stop]
        nostops = [w for w in nostops if w.isalpha()]
        nostops = [w.lower() for w in nostops]
        extra_stops = ['said','he','she','i', 'the', 'a', 'and', 'it']
        nostops = [w for w in nostops if w not in extra_stops]

        ns_text = nltk.Text(nostops)
        text = nltk.Text(tokens)
        np_text = nltk.Text(nopunct)
        return raw, text,ns_text,np_text

def describe(text):
    # most common phrases that occur together
    text.collocations(50)
    # most common words
    fd = nltk.FreqDist(text)
    print fd.most_common(50)

def ngrams(text, n):
    # n-grams
    print "n-grams"
    ngrams = nltk.ngrams(text,n)
    ngrams = nltk.FreqDist(ngrams)
    ng = ngrams.most_common(25)
    for n in ng:
        print n
    print "\n"
    
def reading_level(raw_text):
    print "Flesch Reading Ease: ",textstat.flesch_reading_ease(raw_text)
    print "Flesch-Kincaid Grade Level: ", textstat.flesch_kincaid_grade(raw_text)
    print "Average Sentence Length: ", textstat.avg_sentence_length(raw_text)
    print "Average Word Length: ", textstat.avg_letter_per_word(raw_text)

raw, text, ns_text, np_text = prepFile(sys.argv[1])
# this is the original text
describe(text)
print "\n"
# this one has a lot of common words taken out
describe(ns_text)
print "\n"
print "Reading Level"
print "-------------"
reading_level(raw)
print "\n"
# this needs non punct text to work best
ngrams(np_text,5)
