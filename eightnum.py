'''
Author: iku50 wizo.o@outlook.com
Date: 2022-12-14 00:50:58
LastEditTime: 2022-12-16 18:29:52
LastEditors: iku50 wizo.o@outlook.com
FilePath: /AIcouresedesign/eightnum.py
Description: 
version: Do not edit
Copyright (c) 2022 by iku50, All rights reserved.
'''
import numpy as np
import random

class eightnum:
    start_data=[]
    end_data=np.array([1,2,3,
                       4,5,6,
                       7,8,0])
    def __init__(self):
        self.start_data=random.sample(range(0,9),9)
        while not self.check_data():
            self.start_data=random.sample(range(0,9),9)
        self.start_data=np.array(self.start_data)
        #self.start_data=np.array([0,2,3,1,4,6,7,5,8])
    def check_data(self):
        ss=0
        ee=0
        for i in range (9):
            for j in range(i):
                if self.start_data[j]!=0 and self.start_data[j]<self.start_data[i]:
                    ss+=1
                if self.end_data[j]!=0 and self.end_data[j]<self.end_data[i]:
                    ee+=1
        return ss%2==ee%2
