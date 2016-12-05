from gensim.models import Word2Vec
import pandas as pd
import numpy as np

#change input file to test this
inputfile = "/Users/laurenmccarthy/Documents/Columbia/Fall2016/NLP/FINAL_PROJECT/COMSE6998/Final Project/outputfiles/clean_output.csv"
df = pd.read_csv(inputfile)
sentences = df[df.columns[1]]
print sentences

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

model = main(sentences)

##check = model.most_similar("documentary")
#print check

check = model.most_similar("phone")
print check