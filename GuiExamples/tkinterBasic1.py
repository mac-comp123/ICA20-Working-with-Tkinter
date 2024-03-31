import tkinter as tk


class BasicGUI1:
    """Creates a simple GUI with a welcome label and quit button."""
    
    def __init__(self):
        """Create a BasicGUI1 object, setting up the GUI in the process"""
        
        # set up the overall window, as an instance variable
        self.rootWin = tk.Tk()
        self.rootWin.title("First example")
        
        # set up a label as a local variable (doesn't need to be accessed)
        titleLabel = tk.Label(self.rootWin, text = "Welcome to my program!",
                           font = "Arial 20 bold", relief = tk.GROOVE,
                           justify = tk.CENTER)
        titleLabel.grid(row = 0, column = 0, columnspan = 3)
        
        # set up a button as a local variable (doesn't need to be accessed)
        quitButton = tk.Button(self.rootWin, text = "Quit",
                            font = "Arial 16", command = self.quit)
        quitButton.grid(row = 1, column = 1)

    # This method just calls the root window's method for starting everything
    # running.  There are other ways in later examples for running the GUI
    def go(self):
        """This takes no inputs, and sets the GUI running"""
        self.rootWin.mainloop()

    def quit(self):
        """This is a callback method attached to the quit button.
        It destroys the main window, which ends the program"""
        self.rootWin.destroy()


if __name__ == '__main__':
    # --------------------------------
    # Below here is the script part, which creates the object and sets it running
    myGui = BasicGUI1()
    myGui.go()
