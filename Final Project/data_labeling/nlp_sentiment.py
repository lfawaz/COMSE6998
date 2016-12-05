from pycorenlp import StanfordCoreNLP
import pandas as pd
from clean_data import *

#read in data
text = pd.read_csv('/Users/laurenmccarthy/Documents/Columbia/Fall2016/NLP/FINAL_PROJECT/data/samsung_top_posts.csv')
row = text.columns[1]
text_list = text[row].tolist()

#clean up data
text_str = def clean_data(text_list)

strings = []
S = [x*8000 for x in xrange(85)]
S = S[:]
#print S
for i in xrange(len(S)):
    start = S[i]
    #print i
    #print len(S)
    #print 'start', start
    #print start
    if i == (len(S)-1):
        #print 'last number', i
        current_str = text_str[start:]
    else:
        end = S[i+1]
        current_str = text_str[start:end]
    #print len(current_str)
    #print 'start', start, 'end', end
    strings.append(current_str)
#print strings

nlp = StanfordCoreNLP('http://localhost:9000')

for i in xrange(39, len(strings)):
    print i
    output = pd.DataFrame()
    text_str = strings[i]
    res = nlp.annotate(text_str,
                       properties={
                           'annotators': 'sentiment',
                           'outputFormat': 'json'
                       })
#    for s in res["sentences"]:
#        print "%d: '%s': %s %s" % (
#            s["index"],
#            " ".join([t["word"] for t in s["tokens"]]),
#            s["sentimentValue"], s["sentiment"])
    index_val = []
    sentence = []
    sentimentValue = []
    sentiment = []
    for s in res["sentences"]:
        index_val.append(s["index"])
        current_sentence = " ".join([t["word"] for t in s["tokens"]])
        sentence.append(current_sentence)
        sentimentValue.append(s["sentimentValue"])
        sentiment.append(s["sentiment"])
    
    output['index'] = index_val
    output['sentence'] = sentence
    output['sentimentValue'] = sentimentValue
    output['sentiment'] = sentiment
    save_path = 'output'+str(i)
    output.to_csv('/Users/laurenmccarthy/Desktop/outputfiles/'+save_path)