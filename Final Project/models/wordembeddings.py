from gensim.models import Word2Vec
# import logging
# from bs4 import BeautifulSoup
# import pandas as pd
# import nltk.data
# import re
import numpy as np
#nltk.download()  

#lowercase everything
#deal with unknown tokens
#returnce dimensions


# Read data from file 
# data = pd.read_csv("/Users/laurenmccarthy/Documents/nlp_rnn/assignment1_solutions/cs224d/datasets/stanfordSentimentTreebank/dictionary.txt", delimiter="|", header=None)

# #take text and put words into a list of words
# def text_to_wordlist(text):
# 	text = re.sub("[^a-zA-Z]"," ", text) #remove non letters
# 	words = text.lower().split() #split all words
# 	return(words)

# Load the punkt tokenizer in english
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Define a function to split a review into parsed sentences
# def text_to_sentences(raw_sentence, tokenizer):
#     raw_sentences = tokenizer.tokenize(text.strip())
#     sentences = []
#     for raw_sentence in raw_sentences:
#         # If a sentence is empty, skip it
#         if len(raw_sentence) > 0:
#             # Otherwise, call review_to_wordlist to get a list of words
#             sentences.append( text_to_wordlist( raw_sentence ))
#     # Return the list of sentences (each sentence is a list of words
#     return sentences

# sentences = []  # Initialize an empty list of sentences
# print "Parsing sentences from data set"
# text = data[0]
#word_set = set()

#def add_words_to_word_set(s):
#	global word_set
#	word_set = word_set.union(s.split())
#data[0].apply(add_words_to_word_set)

# for line in text:
#     sentences += text_to_sentences(text, tokenizer)

# print sentences[0]

# We = np.zeros((V, d))
# for word_index, word in words:
# 	We[word_idex] = gensim_model[word]

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main(sentences):
  model = Word2Vec(size=50, window=5, min_count=1)
  model.build_vocab(sentences)
  alpha, min_alpha, passes = (0.025, 0.001, 20)
  alpha_delta = (alpha - min_alpha) / passes

  for epoch in range(passes):
    model.alpha, model.min_alpha = alpha, alpha
    model.train(sentences)

    print ('completed pass %i at alpha %f' % (epoch + 1, alpha))
    alpha -= alpha_delta

    np.random.shuffle(sentences)
  model.save('gensim_model.txt')
  return model

inputfile = "/Users/laurenmccarthy/Documents/nlp_rnn/assignment1_solutions/cs224d/datasets/stanfordSentimentTreebank/dictionary.txt"

def parse_sentence(line):
	return line.split('|')[0].split()

if __name__ == '__main__':
	sentences = [parse_sentence(line) for line in open(inputfile)]

	model = main(sentences)

	check = model.most_similar("documentary")
	print check

