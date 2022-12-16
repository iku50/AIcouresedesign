'''
Author: iku50 wizo.o@outlook.com
Date: 2022-12-14 00:46:53
LastEditTime: 2022-12-16 17:43:50
LastEditors: iku50 wizo.o@outlook.com
FilePath: /AIcouresedesign/Node.py
Description: 
version: Do not edit
Copyright (c) 2022 by iku50, All rights reserved.
'''
'''
structure
    game--the game
        |_start_state   ----state(list)
        |_end_state     ----state(list)
        |_algorithm     ----astar
            |_open      ----open list(list of node)
            |_close     ----close list
            

'''
import numpy as np

class Node:
    state=[]
    def __init__(self,state,depth,parent):
        self.f=0
        self.state=state
        self.depth=depth
        self.parent=parent
        self.children=[]
        self.end_data=np.array([1,2,3,
                                4,5,6,
                                7,8,0])
    def find_zero(self):
        for i in range(9):
            if self.state[i]==0:
                return i
    def move(self,space,move):
        new_state=self.state.copy()
        new_state[space+move],new_state[space]=new_state[space],new_state[space+move]
        return new_state
    #不在taget位置的数据的数目
    def h1(self):
        h=0
        for i in range(1,9):
            if self.state[i]!=self.end_data[i]:
                h+=1
        return h
    #current state到target state换成一维数组的距离
    def h2(self):
        h=0
        for i in range(1,9):
            idx_end=np.where(self.end_data==i)[0][0]
            idx_self=np.where(self.state==i)[0][0]
            h+=abs(idx_end-idx_self)
        return h
    #current state到target state的曼哈顿距离
    def get(self):
        s=''
        s+='节点数据'+'\r'
        for i in range(3):
            for j in range(3):
                s+=str(self.state[i*3+j])+','
            s+='\r'
        s+='节点深度'+str(self.depth)+'\r'
        s+='估价函数值:'+str(self.f)+'\r'
        return s
    def h3(self):
        h=0
        for i in range(1,9):
            idx_end=np.where(self.end_data==i)[0][0]
            idx_self=np.where(self.state==i)[0][0]
            h+=abs(idx_end//3-idx_self//3)+abs(idx_end%3-idx_self%3)
        return h
    def ff(self,mode=1):
        if mode==1:
            return self.depth+self.h1()
        if mode==2:
            return self.depth+self.h2()
        if mode==3:
            return self.depth+self.h3()
    def __gt__(self,other):
        if self.f>other.f:
            return True
        elif self.f==other.f:
            if self.depth<other.depth:
                return True
        else:
            return False