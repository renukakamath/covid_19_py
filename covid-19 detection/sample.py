from os import walk
import os

import numpy as np

from myknn import *
from glcm import glfeature
def train():
    data=[]
    samples=[]
    names=[]
    for dir,d_path,filnames in walk("static/Dataset/train/MildDemented"):
      for file in filnames:
          sample=glfeature(os.path.join(dir,file))
          names.append(1)
          samples.append(sample)
    for dir,d_path,filnames in walk(r"static/Dataset/train/ModerateDemented"):
      for file in filnames:
        sample=glfeature(os.path.join(dir,file))
        names.append(2)
        samples.append(sample)
    for dir,d_path,filnames in walk(r"static/Dataset/train/NonDemented"):
      for file in filnames:
        sample=glfeature(os.path.join(dir,file))
        names.append(3)
        samples.append(sample)
    for dir,d_path,filnames in walk(r"static/Dataset/train/VeryMildDemented"):
      for file in filnames:
        sample=glfeature(os.path.join(dir,file))
        names.append(4)
        samples.append(sample)
    
    np.savetxt("sample.data",samples)
    np.savetxt("labels.dat",names)
# train()
res=prep("static/Dataset/train/ModerateDemented/moderateDem0.jpg")
print(res,"result")


