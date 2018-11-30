import os
#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
#Uncomment line above to not use CUDA.
#If you are training but still want to run this script,
# you must disable cuda or you won't have enought memory.
import keras
from config import *
from model import Model

file_name = "checkpoint_500_epoch_7_layers_2.hdf5"

def main():
    m = Model(file_name=file_name)
    m.generate_text(500)
    print("")

if __name__=="__main__":
    main()
