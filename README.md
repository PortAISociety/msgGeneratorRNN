# msgGeneratorRNN

The goal of this project is to generate a conversation based on facebook chat logs.

Requirements:
Keras, Tensorflow, Numpy

You can install them by running:\
  pip install keras\
  pip install tensorflow\
  pip install numpy


To train this model:

1. Download data from Facebook and move the chats you want to use to this folder.
2. Run:\
  ./parse.sh facebookchatdata.json\
or\
  ./parse.sh \*.json\
If you get permission errors just run:\
  chmod +x ./parse.sh\
3. Run: python3 train.py

To test the model:
 1. Edit main.py, changing file_name to the file.hdf5 that you want to test.\
    file_name = "checkpoint.hdf5"
 2. Run:\
    python3 main.py
