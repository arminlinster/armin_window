import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        label = tk.Label(self, text="Hello World!")
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)

def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file1:
        content:str = file1.read()
    names:list[str]  = content.split()
    return names    

if __name__ == '__main__':
    names:list[str] = get_names()
    print(names)
    print(len(names))
    #if __name__ == "__main__":
    window = Window()
    window.mainloop()