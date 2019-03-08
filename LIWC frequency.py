import nltk
from nltk import FreqDist
## import the text file of TOP 15 LIWC in all 32 topics, and tokenize it
file = open('C:\\Users\Mingy\Desktop\BITS Lab\Mann Whitney U Test\Convingcing features\LIWC.txt')
liwc = file.read()
liwc_token = nltk.word_tokenize(liwc)
print(liwc_token[:100])
print(len(liwc_token))
## Frequency Distribution
fdist=FreqDist(liwc_token)
topkeys=fdist.most_common(100) #print top 50 words with its frequency
for pair in topkeys:
    print(pair)
##plot
fdist.plot(100,cumulative=False)
