#https://tkdocs.com/tutorial/firstexample.html
from logging import root
from tkinter import *
from tkinter import ttk

class feetToMeters:

    def __init__(self, root):
        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding=(3,3,12,12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.feet = StringVar()
        ttk.Button(mainframe, text="Launch Program", command = self.run).grid(column=2, row=2)
        self.meters = StringVar()

        l =ttk.Label(mainframe, text="Starting...")
        l.grid(column=2, row=3)
        l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
        l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
        l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
        l.bind('<3>', lambda e: l.configure(text='Clicked third mouse button'))
        l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
        l.bind('<B3-Motion>', lambda e: l.configure(text=f'third button drag to {e.x},{e.y}'))
        
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", self.run)

        
    def run(self):
        pass
    
    # def calculate(self, *args):
    #     try: 
    #         value = float(self.feet.get())
    #         self.meters.set(round(0.3048 * value, 4))
    #     except ValueError:
    #         pass

root = Tk()
feetToMeters(root)
root.mainloop()