from mtcnn import MTCNN
import argparse
import tensorflow as tf
import cv2
from os.path import isdir
from os import listdir
from numpy import asarray
from numpy import savez_compressed

detector = MTCNN()
img = cv2.imread('./dataset/train/Duy/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
face = detector.detect_faces(img)
print(">>> faces", face)
[x,y,width,height] = face[0]['box']
face = img[y:y+height,x:x+width]
face = cv2.resize(face, (160,160), face)
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
cv2.imwrite(f'test/1.jpg',face)
