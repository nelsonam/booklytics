import csv

with open('top100kindle.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open('top100clean.csv', 'wb') as cleanedfile:
        writer = csv.writer(cleanedfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            row[3] = row[3].split(' ')[0]
            row[4] = ' '.join(row[4].split(' ')[1:]).strip()
            row[5] = row[5].split(';')[0]
            if ':' in row[6]:
                row[6] = row[6].split(':')[1].strip()
            writer.writerow(row)
