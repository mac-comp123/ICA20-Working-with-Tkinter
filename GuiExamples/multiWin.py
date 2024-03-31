import tkinter as tk

class MultiWindows:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("I am the main window")

        otherWin = tk.Toplevel(self.mainWin)
        otherWin["bg"] = "green"
        otherWin.title("I am the helper window")

    def run(self):
        self.mainWin.mainloop()


mw = MultiWindows()
mw.run()
