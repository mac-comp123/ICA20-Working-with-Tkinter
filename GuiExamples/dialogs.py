from tkinter import messagebox



import tkinter as tk
from tkinter import simpledialog, ttk


class DialogTester:
    def __init__(self):
        self.main = tk.Tk()

        b1 = ttk.Button(self.main, text="Background Color", command=self.setBG)
        b1.grid(row=0, column=0)

        b2 = ttk.Button(self.main, text="Your age", command=self.getYourAge)
        b2.grid(row=0, column=1)

        b3 = ttk.Button(self.main, text="Your lowest wage", command=self.getWage)
        b3.grid(row = 0, column=2)

        b4 = ttk.Button(self.main, text="Demo Messagebox", command=self.demoMB)
        b4.grid(row = 1, column = 1)

        self.showAge = ttk.Label(self.main, text="")
        self.showAge.grid(row = 1, column = 1, padx=10, pady=10)
        self.showWage = ttk.Label(self.main, text="")
        self.showWage.grid(row = 1, column = 2, padx=10, pady=10)

    def run(self):
        self.main.mainloop()

    def setBG(self):
        ans = simpledialog.askstring("Background Color", "What color should the background be?")
        if ans is not None:
            self.main['bg'] = ans

    def getYourAge(self):
        answer = simpledialog.askinteger("Input", "What is your age?", parent=self.main, minvalue=0, maxvalue=100)
        if answer is not None:
            print(answer)
            self.showAge['text'] = str(answer)

    def getWage(self):
        answer = simpledialog.askfloat("Wage", "What is the lowest hourly wage you have earned?",
                                       parent = self.main, minvalue = 0.0, maxvalue=1000.0)
        if answer is not None:
            print(type(answer))
            self.showWage['text'] = str(answer)

    def demoMB(self):
        # These first boxes don't return any useful result, user just clicks Ok to make them go away
        instructions = "Grab the laces, and wrap them around your ankles."
        messagebox.showinfo("This is how to tie your shoe", instructions)
        messagebox.showerror("Incorrect number type", "The number must be an integer")
        messagebox.showwarning("Warning", "The wumpus is near!")

        # These next ones return an answer, see console for the answer to be printed
        ans4 = messagebox.askquestion("Question example", "Is this a question?")
        print("askquestion answer:", ans4)
        ans5 = messagebox.askokcancel("Okay/Cancel example", "Okay or cancel?")
        print("askokcancel answer:", ans5)
        ans6 = messagebox.askyesno("Yes/No example", "Answer yes or no?")
        print("askyesno answer:", ans6)
        ans7 = messagebox.askretrycancel("Retry/Cancel", "Retry or cancel?")
        print("askretrycancel answer:", ans7)


if __name__ == '__main__':
    myDiagTest = DialogTester()
    myDiagTest.run()


