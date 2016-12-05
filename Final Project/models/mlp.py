import numpy as np

import theano
import theano.tensor as T

from gensim.models import Word2Vec

import matplotlib.pyplot as plt

from sklearn.utils import shuffle

import cPickle 

#Vanilla MLP

# D input features, M hidden nodes, K outputs
# x (Dx1), z (Mx1), y (Kx1)
# X (NxD), Z (NxM), Y (NxK)
# Z = relu(X.dot(W1)) (NxM)
# Y = softmax(Z.dot(W2)) (NxK)

# dJ/dW2 = Z.T.dot(pY - T)

# J = sum1..N
# j100 = sum1..100
# plt.plot(np.sin(0.1*np.arange(1000)))
# plt.show()


#print 'x_sentence: ', x_sentence, 'x_id: ', x_id, 'y_label: ', y_label, 'y_id: ', y_id

function_map = {
    'relu': T.nnet.relu,
    'tanh': T.tanh,
    'sofmtax': T.nnet.softmax,
}


def error_rate(t, p):
    return np.mean(t != p)


class DenseLayer:
    def __init__(self, mi=None, mo=None, f=None):
        if all(param is not None for param in (mi, mo, f)):
            W = np.random.randn(mi, mo) / np.sqrt(mi + mo)
            self.W = theano.shared(W)
            b = np.zeros(mo)
            self.b = theano.shared(b)
            self.f = f
            self.params = [self.W, self.b]

    @classmethod
    def create(cls, W, b, f):
        layer = DenseLayer()
        layer.W = theano.shared(W)
        layer.b = theano.shared(b)
        layer.f = f
        layer.params = [layer.W, layer.b]
        return layer

    def forward(self, X):
        return self.f(X.dot(self.W) + self.b)

# MLP([100, 50]), D = 1000, K = 5
#  |
#  |__DenseLayer:
#  |     |
#  |     |_ W (1000, 100), b (100), relu
#  |
#  |__DenseLayer:
#  |     |
#  |     |_ W (100, 50), b (50), relu
#  |
#  |__DenseLayer:
#        |
#        |_ W (50, 5), b (5), softmax
#

class MLP:

    def __init__(self, M): #M is the number of hidden units
        self.M = M
        #self.prediction = prediction

    def fit(self, X, Y, lr=10e-6, mu=0.99, epochs=100, batch_sz=100):
        X, Y = shuffle(X, Y)
        Xvalid, Yvalid = X[-1000:], Y[-1000:]
        X, Y = X[:-1000], Y[:-1000]

        N, D = X.shape
        K = len(set(Y))
        
        mi = D
        self.layers = []
        for mo in self.M:
            layer = DenseLayer(mi, mo, T.nnet.relu)
            self.layers.append(layer)
            mi = mo

        layer = DenseLayer(mi, K, T.nnet.softmax)
        self.layers.append(layer)
        # Winput_0 = np.random.randn(D, self.M) / np.sqrt(D + self.M)
        # self.Winput = theano.shared(Winput_0)
        # binput_0 = np.zeros(self.M)
        # self.binput = theano.shared(binput_0)

        # #Out put shapes of the softmax
        # Wout_0 = np.random.randn(self.M, K) / np.sqrt(self.M + K)
        # self.Wout = theano.shared(Wout_0)
        # bout_0 = np.zeros(K)
        # self.bout = theano.shared(bout_0)

        # params = [self.W1, self.b1, self.W2, self.b2]
        params = []
        for layer in self.layers:
            params += layer.params

        #params = [self.W1, self.b1]
        dparams = [theano.shared(p.get_value()*0) for p in params]

        tX = T.matrix('X')
        tY = T.ivector('Y')

        pY = self.forward(tX)
        # T * log(p(Y|X))
        cost = -T.mean(T.log(pY[T.arange(tY.shape[0]), tY])) #pulls in the best value per each line
        # cost = -T.mean(T_indicator * T.log(pY))
        prediction = T.argmax(pY, axis=1)

        updates = [
            (p, p + mu*dp - lr*T.grad(cost, p)) for p, dp in zip(params, dparams)
        ] + [
            (dp, mu*dp - lr*T.grad(cost, p)) for p, dp in zip(params, dparams)
        ]

        # v(t) = dw(t)
        # w(t) = w(t) + dw(t)

        # dw(t) = mu*dw(t-1) - learning_rate*g(t)

        train_op = theano.function(
            inputs=[tX, tY],
            outputs=[cost, prediction],
            updates=updates
        )

        self.get_cost_and_prediction = theano.function(
            inputs=[tX, tY],
            outputs=[cost, prediction],
        )

        self.predict_sentiment = theano.function(
            inputs=[tX],
            outputs=[prediction],
        )

        costs = []
        n_batches = N / batch_sz
        for i in xrange(epochs):
            for j in xrange(n_batches):
                Xbatch = X[j*batch_sz:(j*batch_sz+batch_sz)]
                Ybatch = Y[j*batch_sz:(j*batch_sz+batch_sz)]

                train_op(Xbatch, Ybatch)
                if j % 500 == 0:
                    c, p = self.get_cost_and_prediction(Xvalid, Yvalid)
                    costs.append(c)
                    print i, j, c, error_rate(Yvalid, p)

                #compare cost after the sume of the epoch - 

        plt.plot(costs)
        plt.show()


    def forward(self, X):
        # Z = T.nnet.relu(X.dot(self.W1) + self.b1)
        # return T.nnet.softmax(Z.dot(self.W2) + self.b2)
        Z = X
        for layer in self.layers:
            Z = layer.forward(Z)
        return Z

    #def wrongly_classified(self, X):

    # root -> softmax
    # root1 + root2 -> softmax


    def predict_from_sentence(self, data, w2v):
        d = w2v.vector_size
        curr_sent_vector = 0
        # counter = 0
        data = data.split()
        for word in data:
            if word in w2v.vocab:
                # counter +=1
                curr_sent_vector += w2v[word]
            else: 
                print 'Word not found: ', word
        final_sent_vector = curr_sent_vector#/int(counter)

        return self.predict_sentiment(final_sent_vector.reshape(1, d))

    def save(self, outputfile):
        params = []
        for layer in self.layers:
            params += layer.params
        np.savez(outputfile, *params)

    @classmethod
    def load(cls, inputfile):
        mlp = cls(1) # 1 is dummy value
        mlp.layers = []
        npz = np.load(inputfile)

        last = len(npz.files) - 2
        for i in xrange(0, len(npz.files), 2):
            W = npz['arr_%s' % i]
            b = npz['arr_%s' % (i+1)]
            if i == last:
                layer = DenseLayer.create(W, b, T.nnet.softmax)
            else:
                layer = DenseLayer.create(W, b, T.nnet.relu)
            mlp.layers.append(layer)

        tX = T.matrix('X')
        pY = mlp.forward(tX)
        prediction = T.argmax(pY, axis=1)
        mlp.predict_sentiment = theano.function(
            inputs=[tX],
            outputs=[prediction],
        )
        return mlp


path_x = '/Users/laurenmccarthy/Documents/nlp_rnn/assignment1_solutions/cs224d/datasets/stanfordSentimentTreebank/dictionary.txt'
path_y = '/Users/laurenmccarthy/Documents/nlp_rnn/assignment1_solutions/cs224d/datasets/stanfordSentimentTreebank/sentiment_labels.txt'

def main(load=False, save=False, inputfile=None):

    w2v = Word2Vec.load('gensim_model.txt')
    V = len(w2v.vocab)
    d = w2v.vector_size
    We = np.zeros((V, d))
    #V x d
    print 'create word2vec'
    for word in w2v.vocab:
       vec = w2v[word]
       index = w2v.vocab[word].index
       We[index] = vec
    

    # label_mappings = { phrase_id : label }
    print 'creating mappings'
    label_mappings = {}
    first = True
    for line in open(path_y):
        if first:
            first = False
        else:
            phrase_id, label = line.split('|')
            label_mappings[int(phrase_id)] = int(float(label)*5)
    X = []
    Y = []
    print 'creating x inputs'
    i = 0
    for line in open(path_x):
        curr_sent_vector = np.zeros((100))
        x_sentence, x_id = line.split('|')
        list_words = x_sentence.split()
        #for i in len(words):
        for word in list_words:
            if word in w2v.vocab:
                curr_sent_vector += w2v[word]
        final_sent_vector = curr_sent_vector#/len(list_words)
        X.append(final_sent_vector)
        label = label_mappings[int(x_id)]
        Y.append(label)
        i += 1
        # print as it is training
        #if i % 10000 == 0:
        #    print "sentence:", i
        #print X_list

    #Notes on dimensions
    #d = 100
    #X (Nx100), Y (Nx1)


    #print 'training...'
    X = np.array(X) 
    #print X.shape #X is (239232,1)
    if load:
        mlp = MLP.load(inputfile)
    else:
        #mlp = MLP([100]) #this takes in the number of hidden units M=100
        mlp = MLP([100,100,100]) #this takes in the number of hidden units M=100
        mlp.fit(X, Y) #fit this
    if save:
        mlp.save(inputfile)
    #print mlp.predict_from_sentence("This movie sucks", w2v)
    while True:
        data = raw_input("Enter a sentence:\n")
        print mlp.predict_from_sentence(data, w2v)


if __name__ == '__main__':
    #main(load=False, save=True, inputfile='mymlplayers.npz')
    #main(load=True, inputfile='mymlplayers.npz')
    main(load=True, save=False, inputfile='mymlp.npz')


