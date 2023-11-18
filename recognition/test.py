from keras_facenet import FaceNet
from numpy import load
embedder = FaceNet()
data = load('./6_faces_dataset.npz')
print(data)
# Gets a detection dict for each face
# in an image. Each one has the bounding box and
# face landmarks (from mtcnn.MTCNN) along with
# the embedding from FaceNet.


# If you have pre-cropped images, you can skip the
# detection step.
embeddings = embedder.embeddings(images)