from mtcnn import MTCNN
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--index', required=True)
args = vars(ap.parse_args())
detector = MTCNN()
filename = f'./dataset/test_img/{args["index"]}.jpg'
img = cv2.imread(filename)
face = detector.detect_faces(img)
[x,y,width,height] = face[0]['box']
face = img[y:y+height,x:x+width]
face = cv2.resize(face, (160, 160), face)

cv2.imwrite(f'./dataset/test_img/{args["index"]}_cut.jpg', face)
