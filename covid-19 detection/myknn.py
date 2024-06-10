import math

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
# import pandas as pd
import random
from collections import Counter
# from sklearn import preprocessing
import time

import numpy as np
import argparse
import time

import os

#for plotting
from glcm import *


class CKNN:

    def __init__(self):
        self.accurate_predictions = 0
        self.total_predictions = 0
        self.accuracy = 0.0
        ##########
        with open('labels.dat') as f:
            lines = f.readlines()
        lines=[s.strip('\n') for s in lines]
        training_data=np.loadtxt("sample.data",dtype=float,delimiter=" ")
        # li=[1,9,2,3]
        # print((li[:-1]))




        self.training_set= { '1':[],'2':[],'3':[],'4':[]}
        test_set = {2: [], 4:[]}

        #Split data into training and test for cross validation
        #training_data = lbls[: len(lbls)]
        test_data = []#[-int(test_size * len(dataset)):]

        #Insert data into the training set
        cnt=0

        for record in training_data:
            st=lines[cnt][0]
            cnt+=1


            self.training_set[st[-1]].append( record[:])

    #########

    def predict(self,  to_predict, k = 1):
        # print(to_predict,training_data['6'][0])
        # if len(training_data) >= k:
        #     print("K cannot be smaller than the total voting groups(ie. number of training data points)")
        #     return

        distributions = []
        for group in self.training_set:
            i=0
            # print(group,'group')
            for features in self.training_set[group]:

                euclidean_distance = np.linalg.norm(np.array(features)- np.array(to_predict))
                if  group=='6':
                    # print('hi',euclidean_distance,training_data[group],len(training_data[group]),len(to_predict),i)
                    i+=1
                distributions.append([euclidean_distance, group])

        # print(distributions)
        results = [i[1] for i in sorted(distributions)[:k]]
        # print("rs",results,self.training_set.keys())
        result = Counter(results).most_common(1)[0][0]

        
        # print("rsaaa",result)
        confidence = Counter(results).most_common(1)[0][1]/k

        return result, confidence



def prep(filename):


    s = time.clock()
    feat=glfeature(filename)
    knn = CKNN()
    res=knn.predict(feat)#training_set['6'][1])
    print(res,"")





    return res[0]


# blob = cv2.dnn.blobFromImage(r"C:\Users\Lenovo\PycharmProjects\E_FRESH\src\static\dataset\freshapples\rotated_by_15_Screen Shot 2018-06-08 at 5.03.47 PM.png", 1 / 255.0, (416, 416),swapRB=True, crop=False)

# prep(blob)
# r=prep(r"C:\Users\Lenovo\PycharmProjects\E_FRESH\src\static\dataset\freshapples\rotated_by_15_Screen Shot 2018-06-08 at 5.03.47 PM.png")
# print(r)