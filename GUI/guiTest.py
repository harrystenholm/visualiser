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

        self.buttonText = StringVar(self.mainframe, value="Line Plot")
        self.exponent = IntVar(self.mainframe, value=2)
        
        quitButton = ttk.Button(self.mainframe, width=20, text="Quit", command=self._quit)
        quitButton.grid(column=10,row=1, sticky=(N,E))

        lb = ttk.Button(self.mainframe, width=20, textvariable=self.buttonText, command=self.linePlot)
        lb.grid(column=1, row=2)
        lb.bind("<Enter>", lambda e: self.buttonText.set(self.buttonText.get().upper()))
        lb.bind("<Leave>", lambda e: self.buttonText.set(self.buttonText.get().lower()))

        ib = ttk.Button(self.mainframe, width=20, text="Image Plot", command=self.imagePlot)
        ib.grid(column=3, row=2)

        hb = ttk.Button(self.mainframe, width=20, text="Histogram Plot", command=self.histPlot)
        hb.grid(column=5, row=2)

        vcmd = (self.mainframe.register(self.validateIntEntry), '%P')

        self.intEntry = ttk.Entry(self.mainframe, width=7, textvariable=self.exponent,
                            validate='all', validatecommand=vcmd)
        self.intEntry.grid(column=1, row=5, sticky=(W,E))
        self.intEntry.bind("<Return>", self.updatePlot)

    def updatePlot(self, event):
        # Call plot and then schedule focus to return to the entry widget
        self.linePlot()
        event.widget.after_idle(lambda: event.widget.focus_force())
        return "break"

    def validateIntEntry(self, input):
        return input.isdigit() or input == ""

    def linePlot(self):
        # Plot a line graph
        e = float(self.exponent.get())
        x = np.linspace(0,10,100)
        fig, axs = plt.subplots(figsize=(3, 2), layout='constrained')
        axs.plot(x, x*e, c='b')
        
        canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=3, sticky=(E,W))

        self.intEntry.after_idle(lambda: self.intEntry.focus_force())

    def imagePlot(self):
        # Plot an image with random values
        plt.cla()
        values = np.random.random_sample((20,20))
        fig = plt.figure(figsize=(3, 2), layout='constrained')
        axs = fig.add_subplot()
        axs.imshow(values, interpolation="none")
        axs.set_xticks([])
        axs.set_yticks([])

        canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(column=3, row=3, sticky=(E,W))

    def histPlot(self):
        # Plot a histogram
        params = ((10,10),(4,12),(50,12),(6,55))
        fig, axs = plt.subplots(figsize=(3, 2), layout='constrained')
        for a, b in params:
            values = np.random.beta(a,b,10000)
            axs.hist(values, histtype="stepfilled", bins=30,
                        alpha=0.8, density=True)
        
        canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(column=5, row=3, sticky=(E,W))

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