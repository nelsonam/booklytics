import sys
from wordcloud import WordCloud

def genWordCloud(filename):
    text = open(filename).read()
    words = WordCloud(width=1000, height=1000, font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    words.generate(text)
    words.to_file(filename.split('.')[0] + '.png')

if __name__ == '__main__':

    for i in range(1,15):
        genWordCloud('sources/'+str(i)+'.txt')
