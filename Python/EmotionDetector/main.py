# import the required modules
import cv2
import pprint
import matplotlib.pyplot as plt
from deepface import DeepFace

img = cv2.imread('img.jpg')

result = DeepFace.analyze(img,actions=['age', 'gender', 'emotion'],enforce_detection=False)

pprint.pprint(result)