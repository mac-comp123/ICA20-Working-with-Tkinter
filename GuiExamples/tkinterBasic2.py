import tkinter as tk
from tkinter import ttk


class BasicGUI2:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Second example")
        
        # Create a title label.
        titleLabel = tk.Label(self.rootWin, text = "Welcome to my program!",
                           font = "Arial 20 bold", relief = tk.GROOVE,
                           justify = tk.CENTER)
        titleLabel.grid(row = 0, column = 0, columnspan = 3)
        
        # Create a Button object for a quit button
        quitButton = ttk.Button(self.rootWin, text = "Quit", command = self.quit)
        quitButton.grid(row = 1, column = 1)
        
        # Create a frame to hold a set of labels.  
        labelFrame = tk.Frame(self.rootWin, bg="LightBlue", borderwidth=3,
                           relief = tk.GROOVE, padx=10, pady=10)
        labelFrame.grid(row = 2, columnspan = 3)
        
        # These 9 labels belong to the labelFrame.  
        label00 = tk.Label(labelFrame, text = "A", font = "Arial 14", padx=5, pady=5)
        label01 = tk.Label(labelFrame, text = "B", font = "Arial 14", padx=5, pady=5)
        label02 = tk.Label(labelFrame, text = "C", font = "Arial 14", padx=5, pady=5)
        label10 = tk.Label(labelFrame, text = "D", font = "Arial 14", padx=5, pady=5)
        label11 = tk.Label(labelFrame, text = "E", font = "Arial 14", padx=5, pady=5)
        label12 = tk.Label(labelFrame, text = "F", font = "Arial 14", padx=5, pady=5)
        label20 = tk.Label(labelFrame, text = "G", font = "Arial 14", padx=5, pady=5)
        label21 = tk.Label(labelFrame, text = "H", font = "Arial 14", padx=5, pady=5)
        label22 = tk.Label(labelFrame, text = "I", font = "Arial 14", padx=5, pady=5)
        label00.grid(row = 0, column = 0)
        label01.grid(row = 0, column = 1)
        label02.grid(row = 0, column = 2)
        label10.grid(row = 1, column = 0)
        label11.grid(row = 1, column = 1)
        label12.grid(row = 1, column = 2)
        label20.grid(row = 2, column = 0)
        label21.grid(row = 2, column = 1)
        label22.grid(row = 2, column = 2)

    # This method just calls the root window's method for starting everything
    # running.  There are other ways in later examples for running the GUI
    def go(self):
        self.rootWin.mainloop()

    # This is a "callback" method attached to the quit button.  It destroys
    # the main window, which thus ends the program
    def quit(self):
        self.rootWin.destroy()


if __name__ == '__main__':
    # --- here it goes...
    myGui = BasicGUI2()
    myGui.go()
