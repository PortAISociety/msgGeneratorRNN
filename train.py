import numpy as np
from config import *
from model import Model


#This will encode the dataset and break it down into sequences.
#indexToChar can be used to convert an index to a char.
#charToIndex for the other way around.
def generate_dataset():
    data = open(INPUT_FILE, "r").read()
    chars = list(set(data))
    #This will be the number of features
    VOCAB_SIZE = len(chars)
    indexToChar = {i:char for i, char in enumerate(chars)}
    charToIndex = {char:i for i, char in enumerate(chars)}

    X = np.zeros((int(len(data)//SEQ_LENGTH), SEQ_LENGTH, VOCAB_SIZE))
    y = np.zeros((int(len(data)//SEQ_LENGTH), SEQ_LENGTH, VOCAB_SIZE))
    for i in range(0, int(len(data)/SEQ_LENGTH)):
        X_sequence = data[i*SEQ_LENGTH:(i+1)*SEQ_LENGTH]
        X_sequence_ix = [charToIndex[value] for value in X_sequence]
        input_sequence = np.zeros((SEQ_LENGTH, VOCAB_SIZE))
        for j in range(SEQ_LENGTH):
            input_sequence[j][X_sequence_ix[j]] = 1.
        X[i] = input_sequence

        y_sequence = data[i*SEQ_LENGTH+1:(i+1)*SEQ_LENGTH+1]
        y_sequence_ix = [charToIndex[value] for value in y_sequence]
        target_sequence = np.zeros((SEQ_LENGTH, VOCAB_SIZE))
        for j in range(SEQ_LENGTH):
            target_sequence[j][y_sequence_ix[j]] = 1.
        y[i] = target_sequence

    return VOCAB_SIZE, chars, indexToChar, charToIndex, X, y



if __name__ == "__main__":

    VOCAB_SIZE, chars, indexToChar, charToIndex, X, y  = generate_dataset()

    m = Model(VOCAB_SIZE,indexToChar)

    #Epochs are training iterations on the dataset.
    nb_epoch = 0

    #We could just set the epochs in the fit function to the value we want.
    #But we are doing it this way so we can visually see the
    #    progress since we want to generate text every iteration.
    #And we are also saving the model every 5 iterations.
    for i in range(5):
        print('\n\n')
        m.model.fit(X, y, batch_size=BATCH_SIZE, verbose=1, epochs=1)
        nb_epoch += 1
        m.generate_text(GENERATE_LENGTH)
        if nb_epoch % 5 == 0:
            m.save(nb_epoch)
