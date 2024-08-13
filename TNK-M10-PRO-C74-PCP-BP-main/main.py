import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
from keras.models import Sequential,load_model,Model
from keras.layers import Conv2D,MaxPool2D,Dense,Dropout,BatchNormalization,Flatten,Input
from sklearn.model_selection import train_test_split
from cvzone.FaceDetectionModule import FaceDetector

# Create a path variable to the path of your dataset
path = "Pneumothorax-New-Dataset"


# Create empty images list and categories list
infected = []
uninfected = []


# Loop throught each img in path
for img in os.listdir(path):
    try:
          print(img)
          type = img.split("_")[0]
          img = cv2.imread(str(path)+"/"+str(img))
          img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
          if type == '0':
              infected.append(img)
          else :
              uninfected.append(img)

    except:
        print("error in reading")
        print("Count of infected images", len(infected))
        print("Count of uninfected images", len(uninfected))

