from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools1
from tkinter import messagebox
from tkinter.simpledialog import 
import math
all_data1:dict[any]

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("全台空氣品質指標(AQI)")
        #self.option_add("*Font","微軟正黑體 40")
        #定義style的名稱
        style = ttk.Style()
        style.configure('Top.TFrame')
        style.configure('Top.TLabel',font=('Helvetica',25,'bold'))

        title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')
        ttk.Label(title_frame,text='全台空氣品質指標(AQI)',style='Top.TLabel').pack(expand=True,fill='y')
        title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

        func_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')
        ttk.Button(func_frame,text="AQI品質最好的5個",command=self.click1).pack(side='left',expand=True)
        ttk.Button(func_frame,text="AQI品質最差的5個",command=self.click2).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)
        ttk.Button(func_frame,text="職能學院附近的ubike點",command=self.click4).pack(side='left',expand=True)
        func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

    def click1(self):
        messagebox.showinfo("information","Infomative message")
    
    def click2(self):
        messagebox.showerror("Error","Error message")

    def click3(self):
        messagebox.showwarning("Warning","Warning message")
    
    def click4(self):
        ShowInfo(parent=self,title="這是Dialog")

class ShowInfo(Dialog):
    global buf
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def body(self, master):
        text = tk.Text(self,height=8,font=('Helvetica',25),width=40)
        text.pack(padx=10,pady=10)
        #sprintf(buf,"A = %d\n , B= %s\n",all_data[-1]['sna'],all_data[-1]['sarea'])
        text.insert(tk.INSERT,buf)
        text.config(state='disabled')
        return None

buf = ''

def main():
    global buf
    try:
        all_data:dict[any] = tools1.download_json()
        print(all_data[-1])
        #sprintf(buf,"A = %d\n , B= %s\n",all_data[-1]['sna'],all_data[-1]['sarea'])
        buf += "SNA = %s\n , SAREA = %s\n, total = %d\n" % (all_data[-1]['sna'], all_data[-1]['sarea'], all_data[-1]['total'])
        all_data1 = all_data
    except Exception as error:
        print(error)
    else:        
        #data:list[dict] = tools1.get_data(all_data)
        #pprint(data)
        print("data")
for dat in all_data:
    if abs(dat['lat'] - 25.115000) < 0.00150 and abs(dat['lng'] - 121.537500) < 0.00150:
        print(dat['lat'] - 25.115000)
        print(dat['lng'] - 121.537500) 
        print(dat['lat'])
        print(dat['lng']) 
        print(dat['sna'])
        print(dat['sarea'])
        print(dat['ar'])
        print(dat['act'])
        print(dat['rent_bikes'])
        print(dat['retuen_bikes'])
    window = Window(theme="arc")
    window.mainloop()
    

if __name__ == '__main__':
    main()