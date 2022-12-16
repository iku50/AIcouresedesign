'''
Author: iku50 wizo.o@outlook.com
Date: 2022-12-14 00:49:27
LastEditTime: 2022-12-16 18:16:44
LastEditors: iku50 wizo.o@outlook.com
FilePath: /AIcouresedesign/astar.py
Description: 
version: Do not edit
Copyright (c) 2022 by iku50, All rights reserved.
'''
from Node import *
from eightnum import *
import time

class astar(eightnum):
    def __init__(self,start_data,end__data,max_depth):
        self.start_node=Node(start_data,0,None)
        self.end_node=Node(end__data,0,None)
        self.max_depth=max_depth
        self.spce=[-3,3,-1,1]
        self.open_list=[]
        self.close_list=[]
        self.path=[]
        self.count=0
    def copyarray(self,array):
        new_array=[]
        return new_array+array
    def intable(self,node,table):
        for i in table:
            if (i.state==node.state).all():
                if i.depth>node.depth:
                    i.depth=node.depth
                    i.parent=node.parent
                return True
        return False
    def search(self,mode=1):
        start_time=time.time()
        self.open_list.append(self.start_node)
        while self.open_list!=[] or self.count<self.max_depth:
            self.count+=1
            for i in self.open_list:
                i.f=i.ff(mode=mode)            
            self.open_list.sort()
            n=self.open_list.pop(0)
            if (n.state==self.end_node.state).all():
                while n.parent!=None:
                    self.path.append(n.state)
                    n=n.parent
                self.path.append(n.state)
                end_time=time.time()
                return end_time-start_time
            else:
                self.close_list.append(n)
                for i in self.spce:
                    if ((i==1 and n.find_zero()%3!=2) or 
                        (i==-1 and n.find_zero()%3!=0) or 
                        (i==-3 and n.find_zero()>=3) or
                        (i==3 and n.find_zero()<6)):
                        new_state=n.move(n.find_zero(),i)
                        new_node=Node(new_state,n.depth+1,n)
                        if self.intable(new_node,self.close_list):
                            continue
                        if not self.intable(new_node,self.open_list):
                            self.open_list.append(new_node)
                            n.children.append(new_node)
    def search_solo_prepare(self):
        self.start_node.ff()
        self.open_list.append(self.start_node)
    def search_solo(self,mode):
        if self.open_list==[]:
            return False
        self.count+=1
        for i in self.open_list:
            i.f=i.ff(mode=mode)            
        self.open_list.sort()
        n=self.open_list.pop(0)
        if (n.state==self.end_node.state).all():
            while n.parent!=None:
                self.path.append(n.state)
                n=n.parent
            self.path.append(n.state)
            return True
        else:
            self.close_list.append(n)
            for i in self.spce:
                if ((i==1 and n.find_zero()%3!=2) or 
                    (i==-1 and n.find_zero()%3!=0) or 
                    (i==-3 and n.find_zero()>=3) or
                    (i==3 and n.find_zero()<6)):
                    new_state=n.move(n.find_zero(),i)
                    new_node=Node(new_state,n.depth+1,n)
                    if self.intable(new_node,self.close_list):
                        continue
                    if not self.intable(new_node,self.open_list):
                        self.open_list.append(new_node)
        return False