'''
Author: iku50 wizo.o@outlook.com
Date: 2022-12-13 21:53:24
LastEditTime: 2022-12-16 19:20:17
LastEditors: iku50 wizo.o@outlook.com
FilePath: /AIcouresedesign/ui.py
Description: 
version: Do not edit
Copyright (c) 2022 by iku50, All rights reserved.
'''
from tkinter import *
from eightnum import *
import astar

class App(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.parent = master
        
        self.frame=Frame(self.parent)
        self.frame_select=Frame(self.parent)
        self.frame_openlist=Frame(self.frame)
        self.frame_closedlist=Frame(self.frame)
        self.frame_tree=Frame(self.parent)
        
        self.frame.pack()
        self.frame_openlist.pack()                
        self.frame_closedlist.pack() 
        self.frame_tree.pack()       
        
        self.label=Label(self.frame,text='八数码',font=('Arial', 10),width=15,height=2)
        self.label_openlist=Label(self.frame_openlist,font=('Arial', 10),width=15,height=2,text='openlist')
        self.label_closedlist=Label(self.frame_closedlist,font=('Arial', 10),width=15,height=2,text='closedlist')
        self.label.pack()
        
        self.button=Button(self.frame,text='开始',font=('Arial', 10),width=15,height=2,command=self.start)
        self.button_cal=Button(self.frame,text='计算',font=('Arial', 10),width=15,height=2,command=self.button_calculate)
        self.button_start_cal=Button(self.frame,text='连续计算',font=('Arial', 10),width=15,height=2,command=self.button_start_calculate)
        self.button_yess=Button(self.frame,text='确定选择',font=('Arial', 10),width=15,height=2,command=self.button_yes)
        self.button_showpathh=Button(self.frame,text='显示路径',font=('Arial', 10),width=15,height=2,command=self.button_showpath)
        self.button_soloo=Button(self.frame,text='单步显示',font=('Arial', 10),width=15,height=2,command=self.button_solo)
        self.button_paintsearchtreee=Button(self.frame_tree,text='绘制搜索树',font=('Arial', 10),width=15,height=2,command=self.button_paintsearchtree)
        self.button.pack()
        
        self.canvas=Canvas(self,width=320,height=170,bg='white')
        self.canvas_tree=Canvas(self.frame_tree,width=1000,height=500,bg='white')
        
        list_items=StringVar()
        list_items.set(['不在目标位置的个数','一维数组距离','曼哈顿距离'])        
        self.listbox_calmode=Listbox(self.frame_select,listvariable=list_items,width=30,height=3,font=('Arial', 10))
        self.listbox_openlist=Listbox(self.frame_openlist,width=50,height=3,font=('Arial', 10))
        self.listbox_closedlist=Listbox(self.frame_closedlist,width=50,height=3,font=('Arial', 10))
        
        self.messagelabel=Label(self.frame,width=50,height=2)
        self.messagelabel.configure(font=('Arial', 10))
        self.delist=[0]*100
        self.openlist=StringVar()
        self.closelist=StringVar()
        self.pack()
        self.data=eightnum()
    def start(self):
        start_data=self.data.start_data
        self.button.pack_forget()
        self.canvas.pack()
        self.canvas.create_text(95,30,text='初始状态',font=('Arial', 10),fill='black')
        self.canvas.create_text(225,30,text='目标状态',font=('Arial', 10),fill='black')
        for i in range(9):#画格子
            self.canvas.create_rectangle(50+30*(i//3),40+30*(i%3),80+30*(i//3),70+30*(i%3),fill='white')
            self.canvas.create_rectangle(180+30*(i//3),40+30*(i%3),210+30*(i//3),70+30*(i%3),fill='white')
        for i in range(9):#画数字
            self.canvas.create_text(65+30*(i%3),55+30*(i//3),text=start_data[i],font=('Arial', 10),fill='black')
            self.canvas.create_text(195+30*(i%3),55+30*(i//3),text=self.data.end_data[i],font=('Arial', 10),fill='black')
        self.button_cal.pack()
    def button_calculate(self):
        self.frame_select.pack()
        self.listbox_calmode.pack()
        self.button_yess.pack()
        self.messagelabel.pack()
        self.button_cal.pack_forget()
        self.messagelabel.configure(text='请选择计算模式')
    def button_yes(self):
        if(self.listbox_calmode.curselection()==()):
            self.messagelabel.configure(text='您还未选择计算模式')
            return
        self.button_yess.pack_forget()
        self.messagelabel.configure(text='你选择的计算模式是：'+self.listbox_calmode.get(self.listbox_calmode.curselection()))
        self.button_start_cal.pack()
        self.button_soloo.pack()
    def button_start_calculate(self):
        self.button_soloo.pack_forget()
        self.button_start_cal.pack_forget()
        mode=self.listbox_calmode.curselection()[0]+1
        self.a=astar.astar(self.data.start_data,self.data.end_data,5000)
        time=self.a.search(mode)
        if(self.a.path==None):
            self.messagelabel.configure(text='寻路失败,寻找顶点数超过5000')
        else:
            tt=round(time*1000).__str__()
            ss=len(self.a.path).__str__()
            node=len(self.a.close_list).__str__()  
            self.button_paintsearchtreee.pack()
            self.messagelabel.configure(text='寻路成功,共'+ss+'步,耗时'+tt+'ms,搜寻顶点数'+node)
            self.button_showpathh.pack()
            self.path=self.a.path
    def button_showpath(self):
        self.button_showpathh.pack_forget()
        self.pathcanvas=Canvas(self,bg='white')
        self.pathcanvas.create_text(0,0,text='')
        self.scrollbar=Scrollbar(self.master,orient=HORIZONTAL)
        for i in range(len(self.path)):
            for j in range(9):#画格子
                self.pathcanvas.create_rectangle(50+30*(j//3)+200*i,40+30*(j%3),80+30*(j//3)+200*i,70+30*(j%3),fill='white')
            for j in range(9):#画数字
                self.pathcanvas.create_text(65+30*(j%3)+200*i,55+30*(j//3),text=self.path[len(self.path)-1-i][j],font=('Arial', 10),fill='black')
        self.scrollbar.config(command=self.pathcanvas.xview)
        self.pathcanvas.config(scrollregion=self.pathcanvas.bbox("all"),xscrollcommand=self.scrollbar.set)
        self.pathcanvas.pack()
        self.scrollbar.pack(side='top',fill='x')
    def button_solo(self):
        mode=self.listbox_calmode.curselection()[0]+1
        self.button_soloo.configure(command=self.button_solo_calculate)
        self.button_start_cal.pack_forget()
        self.scrollbaropen=Scrollbar(self.frame_openlist,orient=VERTICAL)
        self.scrollbarclosed=Scrollbar(self.frame_closedlist,orient=VERTICAL)
        self.scrollbaropen.pack(side='right',fill='y')
        self.scrollbarclosed.pack(side='right',fill='y')
        self.label_openlist.pack()
        self.label_closedlist.pack()
        self.a=astar.astar(self.data.start_data,self.data.end_data,5000)
        self.a.search_solo_prepare()
        self.openlist.set([self.a.open_list[0].get()])
        self.listbox_openlist.configure(listvariable=self.openlist,yscrollcommand=self.scrollbaropen.set)
        self.listbox_closedlist.configure(listvariable=self.closelist,yscrollcommand=self.scrollbarclosed.set)
        self.scrollbaropen.config(command=self.listbox_openlist.yview)
        self.scrollbarclosed.config(command=self.listbox_closedlist.yview)
        self.listbox_openlist.pack()
        self.listbox_closedlist.pack()
    def button_solo_calculate(self):
        mode=self.listbox_calmode.curselection()[0]+1
        if self.a.search_solo(mode):
            self.calculate_complete()
        o=[self.a.open_list[i].get() for i in range(len(self.a.open_list))]
        c=[self.a.close_list[i].get() for i in range(len(self.a.close_list))]
        self.openlist.set(o)
        self.closelist.set(c)
        self.listbox_openlist.configure(listvariable=self.openlist)
        self.listbox_closedlist.configure(listvariable=self.closelist)
    def calculate_complete(self):
        self.button_soloo.pack_forget()
        self.listbox_openlist.pack_forget()
        self.listbox_closedlist.pack_forget()
        self.label_openlist.pack_forget()
        self.label_closedlist.pack_forget()
        self.scrollbaropen.pack_forget()
        self.scrollbarclosed.pack_forget()
        self.messagelabel.configure(text='寻路成功,共'+len(self.a.path).__str__()+'步')
        self.button_showpathh.pack()
        self.path=self.a.path
        self.button_paintsearchtreee.pack()
    def button_paintsearchtree(self):
        self.button_paintsearchtreee.pack_forget()
        self.canvas_tree.pack()
        self.scrollbar_tree=Scrollbar(self.frame_tree,orient=HORIZONTAL)
        self.scrollbar_treey=Scrollbar(self.frame_tree,orient=VERTICAL)
        p=self.a.close_list[0]
        self.canvas_tree.create_text(0,0,text='')
        self.canvas_tree.create_rectangle(0,0,100,100,fill='white')
        self.canvas_tree.create_text(50,50,text=p.get(),font=('Arial', 10))
        self.dfs(p,0,0)
        self.scrollbar_tree.config(command=self.canvas_tree.xview)
        self.scrollbar_treey.config(command=self.canvas_tree.yview)
        self.canvas_tree.config(scrollregion=self.canvas_tree.bbox("all"),xscrollcommand=self.scrollbar_tree.set,yscrollcommand=self.scrollbar_treey.set)
        self.canvas_tree.pack(side='left' ,fill='y')
        self.scrollbar_treey.pack(side='right',fill='y')
        self.scrollbar_tree.pack(side='bottom',fill='x')
    def dfs(self,p,i,q):
        k=self.delist[i]
        if p.children!=None:
            for j in range(len(p.children)):
                self.canvas_tree.create_line(50+200*i,50+100*q,50+200*(i+1),50+100*(j+k))
                self.canvas_tree.create_rectangle(200*(i+1),100*(j+k),100+200*(i+1),100+100*(j+k),fill='white')
                self.canvas_tree.create_text(50+200*(i+1),50+100*(j+k),text=p.children[j].get(),font=('Arial', 10))
                self.dfs(p.children[j],i+1,j+k)
                self.delist[i]+=1
app=App()
app.master.title('八数码')
app.mainloop()
