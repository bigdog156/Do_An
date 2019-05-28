from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH,RIGHT,LEFT,RAISED
import tkinter.messagebox as mbox
from tkinter.filedialog import askopenfilename
from tkinter import Label
import os
import sys
from huffman import HuffmanCoding
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.path = ""
        self.h=None
        self.initUI()
  
    def initUI(self):
        self.parent.title("Nén HuffMan")
        
        self.pack()
        self.choiceButton()
        self.NenButton()
        self.GiaiNenButton()

    def choiceButton(self):
        choice = Button(self,text="Chọn File",command=self.choice)
        choice.grid(column=0,row=1)
        return self.path
       
    def choice(self):
        filename = askopenfilename()
        lable=Label(self,text="",relief=RAISED)
        lable.configure(text=filename)
        lable.grid(column=0,row=2)
        lable1=Label(self,text="")
        lable1.configure(text="Dung lượng "+ str(os.path.getsize(filename))+ " bytes")
        lable1.grid(column=0,row=3)
        self.path = filename
        self.h = HuffmanCoding(filename)

    def NenButton(self):
        nen=Button(self,text="Nén ",command=self.Nen)
        nen.grid(column=1,row=4)
        
    def Nen(self):
        ht=self.h
        output_path = ht.compress()
        print("Compressed file path: " + output_path)
        lableNen=Label(self,text="")
        lableNen.configure(text=output_path)
        lableNen.grid(column=0,row=5)

        lableByte=Label(self,text="",relief=RAISED)
        lableByte.configure(text="Dung lượng "+ str(os.path.getsize(output_path))+ " bytes")
        lableByte.grid(column=0,row=6)
        self.path=output_path
        

    def GiaiNenButton(self):
        giainen=Button(self,text="Giai Nén",command=self.GiaiNen)
        giainen.grid(column=2,row=4)
        
    def GiaiNen(self):
        path = self.pathUrl()
        ht= self.h
        decom_path = ht.decompress(path)
        print("Decompressed file path: " + decom_path)
        print("Compress complated")
        lableGiai=Label(self,text="")
        lableGiai.configure(text=decom_path)
        lableGiai.grid(column=0,row=7)

        lableBytes=Label(self,text="",relief=RAISED)
        lableBytes.configure(text="Dung lượng "+ str(os.path.getsize(decom_path))+ " bytes")
        lableBytes.grid(column=0,row=8)

    #Path url in Hufman
    def pathUrl(self):
        path = self.path[::-1]
        pathstr=''
        for i in path:
            if i=='/':
                break
            pathstr +=i
        return pathstr[::-1]            


  
root = Tk()
ex = Example(root)
root.minsize(400,200)
root.mainloop()