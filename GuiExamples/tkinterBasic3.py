import tkinter as tk
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk


class BasicGUI3:
    """An object containing a GUI program that asks the user a question"""

    def __init__(self):
        """Initialize the BasicGUI3 object and all its widgets"""
        
        self.rootWin = tk.Tk()
        self.rootWin.title("Fourth example")

        tPic = Image.open("catWalking.jpg")
        self.turtlePic = ImageTk.PhotoImage(tPic)   # IMAGES MUST ALWAYS BE OBJECT VARIABLES!!
        imgLabel = tk.Label(self.rootWin, image=self.turtlePic)
        imgLabel.grid(row=0, column=0)

        # Create a frame to hold the label and entry
        self.frame = tk.Frame(self.rootWin, padx=10, pady=10)
        self.frame.grid(row = 1, column = 0)
        
        # Create a label to ask the question
        instrLabel = tk.Label(self.frame, text="Do you like green eggs and ham?",
                           relief=tk.RAISED,
                           padx=5, pady=5)
        instrLabel.grid(row=0,column=0)
        
        # Make an entry for the user to type in, connect its text to the StringVar
        self.userInputEntry = tk.Entry(self.frame, text="",
                               width=10, relief=tk.RAISED)
        self.userInputEntry.grid(row=0, column = 3)
        
        # When the user hits return or tab while in the entry box, this callback
        # will be triggered.
        self.userInputEntry.bind("<Return>", self.respond)
        self.userInputEntry.bind("<Tab>", self.respond)

    def go(self):
        """Takes no inputs, and calls the root windows main loop to run the GUI"""
        self.rootWin.mainloop()

    def respond(self, event):
        """Takes an event object as input, and is the callback for the user's input
        box.  It reads the text in the box through the StringVar, and changes 
        the color of the frame to green or blue depending on the text"""
        userText = self.userInputEntry.get()
        self.userInputEntry.delete(0, tk.END)
        if 'yes' in userText.lower():
            self.userInputEntry.insert(0, "yes")
            self.frame['bg'] = 'Green'
        else:
            self.userInputEntry.insert(0, "no")
            self.frame['bg'] = 'Blue'


if __name__ == '__main__':
    # --- here it goes...
    myGui = BasicGUI3()
    myGui.go()
