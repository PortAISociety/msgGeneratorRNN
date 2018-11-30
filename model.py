import numpy as np
from keras import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Activation
from keras.layers.wrappers import TimeDistributed
from config import *
import pickle

class Model():

    #If file-name is passed it will load a previous saved model
    def __init__(self,VOCAB_SIZE=None,indexToChar=None,file_name=None):

        if VOCAB_SIZE and indexToChar:
            self.VOCAB_SIZE = VOCAB_SIZE
            self.indexToChar = indexToChar
            self.define_model()
        elif file_name:
            with open('model_vocab.pkl', 'rb') as f:
                info = pickle.load(f)

            self.VOCAB_SIZE = info[0]
            self.indexToChar = info[1]

            self.define_model()
            self.model.load_weights(file_name)

    #Defines the model layer by layer. Feel free to add more layers and see the effect on the model.
    def define_model(self):
        self.model = Sequential()
        self.model.add(LSTM(HIDDEN_DIM, input_shape=(None, self.VOCAB_SIZE),return_sequences=True)) #Input layer

        for i in range(LAYER_NUM -1):
            self.model.add(LSTM(HIDDEN_DIM, return_sequences=True)) #Optional lstm layers
        self.model.add(TimeDistributed(Dense(self.VOCAB_SIZE))) #Output layer
        self.model.add(Activation("softmax"))

        self.model.compile(loss="categorical_crossentropy",optimizer="rmsprop")

    def generate_text(self, length):
        ix = [np.random.randint(self.VOCAB_SIZE)]
        y_char = [self.indexToChar[ix[-1]]]
        X = np.zeros((1, length, self.VOCAB_SIZE))
        for i in range(length):
            X[0, i, :][ix[-1]] = 1
            print(self.indexToChar[ix[-1]], end="")
            ix = np.argmax(self.model.predict(X[:, :i+1, :])[0], 1)
            y_char.append(self.indexToChar[ix[-1]])
        return ('').join(y_char)

    #This function saves the model in a .hdf5 file and the vocabulary used to model_vocabl.pkl.
    #This can be improved by saving the vocab with the model in the hdf5 file.
    def save(self,nb_epoch):
        info = [self.VOCAB_SIZE, self.indexToChar]
        with open("model_vocab.pkl", 'wb') as f:
            pickle.dump(info, f, pickle.HIGHEST_PROTOCOL)
        self.model.save_weights('checkpoint_{}_epoch_{}_layers_{}_newModel.hdf5'.format(HIDDEN_DIM, nb_epoch,LAYER_NUM))
