#java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer

from pycorenlp import StanfordCoreNLP
import pandas as pd
import re
from clean_data_6 import *

text = pd.read_csv('/Users/laurenmccarthy/Documents/Columbia/Fall2016/NLP/FINAL_PROJECT/COMSE6998/Final Project/reddit_data/samsung_top_posts_cleansed.csv')

#data clean
text = text.drop(text.index[921]).reset_index(drop=True)
text = text.drop(text.index[1146]).reset_index(drop=True)
text = text.drop(text.index[1242]).reset_index(drop=True)
text = text.drop(text.index[2496]).reset_index(drop=True)
text = text.drop(text.index[2610]).reset_index(drop=True)
text = text.drop(text.index[2642]).reset_index(drop=True)
text = text.drop(text.index[2904]).reset_index(drop=True)

nlp = StanfordCoreNLP('http://localhost:9000')
output = pd.DataFrame()
N, d = text.shape
index_val = []
sentence = []
sentimentValue = []
sentiment = []
column = text['comment']

for date_index in xrange(0, 3200):
    if date_index % 100 == 0:
        print date_index
    comment = column[date_index]
    comment = clean_data(comment)
    comment_clean = re.sub("[^a-zA-Z0-9]", " ", comment)
    comment_clean = re.sub(" +", " ", comment_clean)
    res = nlp.annotate(comment_clean,
                       properties={
                           'annotators': 'sentiment',
                           'outputFormat': 'json'
                       })
    for i,s in enumerate(res["sentences"]):
        #print i#, s
        index_val.append(date_index)
        current_sentence = " ".join([t["word"] for t in s["tokens"]])
        sentence.append(current_sentence)
        #print s["sentimentValue"], s["sentiment"], current_sentence
        #output
        sentimentValue.append(s["sentimentValue"])
        sentiment.append(s["sentiment"])

output['index'] = index_val
output['sentence'] = sentence
output['sentimentValue'] = sentimentValue
output['sentiment'] = sentiment
save_path = 'output'+str(i)
output.to_csv('/Users/laurenmccarthy/Desktop/'+save_path)