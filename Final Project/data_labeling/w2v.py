from gensim.models import Word2Vec
import numpy as np

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

