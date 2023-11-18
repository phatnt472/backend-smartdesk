from numpy import load, expand_dims
from random import choice
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from matplotlib import pyplot
import argparse
import cv2
from keras_facenet import FaceNet
from predict_face_embeddings import get_embedding
ap = argparse.ArgumentParser()
ap.add_argument('-fd', '--face_dataset', required=True)
ap.add_argument('-fe', '--face_embedding', required=True)
args = vars(ap.parse_args())



data = load(args['face_embedding'])
trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
print('Dataset: train=%d, test=%d' % (trainX.shape[0], testX.shape[0]))

in_encoder = Normalizer(norm='l2')
trainX = in_encoder.transform(trainX)
testX = in_encoder.transform(testX)

out_encoder = LabelEncoder()
out_encoder.fit(trainy)
trainy = out_encoder.transform(trainy)
testy = out_encoder.transform(testy)

model = SVC(kernel='linear', probability=True)
model.fit(trainX, trainy)

# predict
yhat_train = model.predict(trainX)
yhat_test = model.predict(testX)
# score
score_train = accuracy_score(trainy, yhat_train)
score_test = accuracy_score(testy, yhat_test)
print(testy, yhat_test)
print('Accuracy: train=%.3f, test=%.3f' % (score_train*100, score_test*100))

img = cv2.imread('./dataset/test_img/1_cut.jpg')
new_img = get_embedding([img])
yhat_class = model.predict(new_img)
yhat_prob = model.predict_proba(new_img)
# get name
class_index = yhat_class[0]
class_probability = yhat_prob[0,class_index] * 100
predict_names = out_encoder.inverse_transform(yhat_class)
print('Predicted: %s (%.3f)' % (predict_names[0], class_probability))
cv2.imshow(predict_names[0], img)
cv2.waitKey(0)

