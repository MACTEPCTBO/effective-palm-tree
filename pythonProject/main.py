from tkinter import *
import sqlite3



class GUI:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root, width=500, height=500, bg='grey')
        self.frame.pack()

        self.label = []
        self.button = []
        self.entry = []

    def Label(self,x=int ,y=int ,text=str):
        """"Создаётся объект Label и передаёт его на frame"""
        self.lbl1 = Label(master=self.frame,text=text,relief=SOLID,width=20,height=2)
        self.lbl1.place(x=x,y=y)

        self.label.append(self.lbl1)

        return object

    def Button(self,x=int,y=int,text=str,command=str):
        """Создаёт объект Button и передаёт его га frame"""

        self.btn = Button(master=self.frame,text=text,relief=SOLID,width=20,height=2,command=command)
        self.btn.place(x=x,y=y)

        self.button.append(self.btn)

        return object


    def Entry(self,x=int,y=int):
        """Создаёт объект Entry  и передаёт его в frame"""
        self.ent = Entry(master=self.frame,relief=SOLID,width=20)
        self.ent.place(x=x,y=y)

        self.entry.append(self.ent)

        return object



def test():
    print('TEST')

gui = GUI()


if __name__ == '__main__':

    gui.Label(20,20,'привет')
    gui.Button(20,60,'Кнопка',test)
    gui.Entry(20,110)
    
    gui.root.mainloop()