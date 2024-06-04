from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools

class Window(ThemedTk):
    def __init__(self,**kwargs): 
        super().__init__(**kwargs)
        self.title("AQI顯示")
        self.option_add('*font',('微軟正黑體',25,'bold'))
        ttk.Button(self, text="Quit", command=self.destroy).pack()
        title_frame = ttk.Frame(self)
        style = ttk.Style()
        style.configure('Top.TFrame', background ='#FF0')
        title_frame = ttk.Frame(self,style='Top.TFrame')
        ttk.Label(title_frame,text="全台AQI空品指標").pack()
        title_frame.pack(padx=100,pady=50)


def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:        
        data:list[dict] = tools.get_data(all_data)
        pprint(data)
    '''
    window = Window(theme="blue")
    window.mainloop()
    

if __name__ == '__main__':
    main()