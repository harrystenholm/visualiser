#https://tkdocs.com/tutorial/firstexample.html
from multiprocessing import Process
from tkinter import *
from tkinter import ttk
import tkinter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np
import pandas as pd

class displayGraph:

        def __init__(self, root, mainframe):
            
            
            self.mainframe = mainframe
            self.root = root

            self.root.title("Display Graph")

            self.buttonText = StringVar(self.mainframe, value="Launch Program")
            self.exponent = IntVar(self.mainframe, value=2)
            
            quitButton = ttk.Button(self.mainframe, width=20, text="Quit", command=
                                    lambda: [])
            quitButton.grid(column=2, row=1, sticky=(W,E))

            b = ttk.Button(self.mainframe, width=20, textvariable=self.buttonText, command=self.plot)
            b.grid(column=2, row=3)
            b.bind("<Enter>", lambda e: self.buttonText.set(self.buttonText.get().upper()))
            b.bind("<Leave>", lambda e: self.buttonText.set(self.buttonText.get().lower()))

            vcmd = (self.mainframe.register(self.validateIntEntry), '%P')

            intEntry = ttk.Entry(self.mainframe, width=7, textvariable=self.exponent,
                                validate='all', validatecommand=vcmd)
            intEntry.grid(column=2, row=5, sticky=(W,E))
            intEntry.focus_set()
            intEntry.bind("<Return>", self.updatePlot)

        def updatePlot(self, event):
            # Call plot and then schedule focus to return to the entry widget
            self.plot()
            event.widget.after_idle(lambda: event.widget.focus_force())
            return "break"

        def validateIntEntry(self, input):
            return input.isdigit() or input == ""

        def plot(self):
            e = float(self.exponent.get())
            x = np.linspace(0,10,100)
            fig, axs = plt.subplots(figsize=(6, 4), layout='constrained')
            axs.plot(x, x**e, c='b')
            
            canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
            canvas.draw()
            canvas.get_tk_widget().grid(column=2, row=3, sticky=(N,E,W,S))

        def _quit(self):
            self.root.quit()     # stops mainloop
            self.root.destroy()  # necessary on Windows to prevent a fatal error


def run_gui():
    root = Tk()
    mainframe = ttk.Frame(root, padding=(10, 10))
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    displayGraph(root, mainframe)
    root.mainloop()

if __name__ == "__main__":
    # Start GUI in a separate process. Don't daemonize so it runs independently.
    p = Process(target=run_gui)
    p.start()

    try:
        input("GUI started in child process. Press Enter to stop...\n")
    finally:
        p.terminate()
        p.join()