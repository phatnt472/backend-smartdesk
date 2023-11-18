import cv2
import numpy as np

import glob

from keras.models import load_model

FRmodel = load_model('models/face-rec_Google.h5')
print("Total Params:", FRmodel.count_params())