#run this command in stanford
#java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer

from pycorenlp import StanfordCoreNLP
import pandas as pd
from clean_data import *

#read in data
text = pd.read_csv('/Users/laurenmccarthy/Documents/Columbia/Fall2016/NLP/FINAL_PROJECT/data/samsung_top_posts.csv')

for index, row in text.iterrows():
    print row, index
    #print row['comment']
    #text[row['comment']] = clean_data(row['comment'])
#text.head()