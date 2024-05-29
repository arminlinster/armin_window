import tkinter as tk
from tkinter import ttk
names2 = "這是第一支GUI程式的內容"

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry('700x300')
        '''
        btn1:ttk.Button = ttk.Button(self,text="Top")
        btn1.pack()
        btn2:ttk.Button = ttk.Button(self,text="Middle")
        btn2.pack()
        btn3:ttk.Button = ttk.Button(self,text="Bottom")
        btn3.pack()
        '''
        btn4:ttk.Button = ttk.Button(self,text="btn01").pack(side='left')
        btn5:ttk.Button = ttk.Button(self,text="btn02").pack(side='left')
        btn6:ttk.Button = ttk.Button(self,text="btn03").pack(side='left')
        label:ttk.LabelFrame = ttk.Label(self,
                                         text=names2,
                                         font=("arial",20,"bold"),
                                         foreground ='#f00',
                                         background = '#0ff')
        label.pack(padx=10, pady=5)

if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()