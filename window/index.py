import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,title:str,**kwargs):
        super().__init__(**kwargs)
        self.title(title)
        label:ttk.LabelFrame = ttk.Label(self,
                                         text=names2,
                                         font=("arial",20,"bold"),
                                         foreground ='#f00',
                                         background = '#0ff')
        label.pack(padx=100, pady=50)
        #label = tk.Label(self, text= names2)
        #label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file1:
        content:str = file1.read()
    names:list[str]  = content.split()
    return names    

if __name__ == '__main__':
    names:list[str] = get_names()
    print(names)
    print(len(names))
    names1="這是第一支GUI程式"
    names2 = "這是第一支GUI程式的內容"
    #if __name__ == "__main__":
    window:Window = Window(title=names1)
    #window.title("my first pro")
    #window.tk.Label(self, text="Hello World!")
    window.mainloop()