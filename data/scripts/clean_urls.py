import csv

with open('urls.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    urls = []
    for row in reader:
        url = row[0]
        stuff = url.split('\n')
        for entry in stuff:
            if entry != '' and entry != 'http://www.amazon.com/Best-Sellers-Kindle-Store-eBooks/zgbs/digital-text/154606011/' and entry != 'title.href':
                urls.append(entry)

#for u in urls:
#    print u
for u in urls:
    split = u.split('/')
    for s in split:
        if 'B00' in s:
            print "http://www.amazon.com/dp/" + s + "/"
