# generates math problems a la flash cards for La Boo'eme


import tkinter as tk
import random


class MathGUI:
    def __init__(self):
        self.root = tk.Tk()

        # variables to hold the checkbutton options
        self.addChoice = tk.StringVar()
        self.subChoice = tk.StringVar()
        self.easyChoice = tk.StringVar()
        self.hardChoice = tk.StringVar()

        # variables to hold the math problem parts
        self.val1Var = tk.StringVar()
        self.val2Var = tk.StringVar()
        self.correctAns = tk.StringVar()
        self.opVar = tk.StringVar()
        self.messageVar = tk.StringVar()
        self.userAns = tk.StringVar()

        self.totalVar = tk.IntVar()
        self.correctVar = tk.IntVar()

        self.easyCheck = None  # Will be defined later
        self.hardCheck = None  # Will be defined later

    def createWidgets(self):
        #################### build GUI ##############################        
        self.root.title('Math Practice')
        # welcome label
        welcome = tk.Label(master=self.root, text="Welcome to Henry's Math Practice Program",
                           font='Arial 20 bold', bd=20, relief='ridge', padx=20, pady=20)
        welcome.grid(row=0, columnspan=10)

        # Stuff for selecting addition or subtraction
        label_1 = tk.LabelFrame(master=self.root, text='Addition or subtraction', padx=20,
                                font='Arial 14 italic', fg='blue', pady=10, bd=5, relief='groove')
        label_1.grid(row=1, column=1, pady=10)

        addCheck = tk.Checkbutton(label_1, text="Addition", variable=self.addChoice, onvalue='yes', offvalue='no', font='Arial 14')
        subCheck = tk.Checkbutton(label_1, text="Subtraction", variable=self.subChoice, onvalue='yes', offvalue='no', font='Arial 14')

        addCheck.grid(row=0, column=1)
        subCheck.grid(row=1, column=1)
        addCheck.select()
        subCheck.deselect()

        # Stuff for selecting difficulty level
        label_2 = tk.LabelFrame(master=self.root, text='Difficulty level', padx=20,
                                font='Arial 14 italic', fg='blue', pady=10, bd=5, relief='groove')
        label_2.grid(row=1, column=8, pady=10)

        self.easyCheck = tk.Checkbutton(label_2, text="Easy", variable=self.easyChoice, onvalue='yes', offvalue='no', font='Arial 14')
        self.hardCheck = tk.Checkbutton(label_2, text="Hard", variable=self.hardChoice, onvalue='yes', offvalue='no', font='Arial 14')

        self.easyCheck.grid(row=0, column=1)
        self.hardCheck.grid(row=1, column=1)
        self.easyCheck.select()
        self.hardCheck.deselect()

        # set up next Problem button
        nextProblem = tk.Button(self.root, text="Next Problem", command=self.nextProb, font='Arial 14 bold',
                                bd=5 , relief='raised', padx=10, pady=10, bg='red', fg='blue')
        nextProblem.grid(row=4, columnspan=10, pady=10)

        # set up math problem frame...
        probFrame = tk.Frame(self.root, bd=5, relief="groove", padx=50,pady=10)
        probFrame.grid(row=6, columnspan=10, padx=10, pady=10)

        # math problem labels etc.
        labelMess = tk.Label(self.root, textvariable=self.messageVar, padx=10, font='Arial 16 bold', pady=5, fg='blue')
        labelV1 = tk.Label(probFrame, textvariable=self.val1Var, padx=20, font='Arial 16', pady=5, bd=5)
        labelV2 = tk.Label(probFrame, textvariable=self.val2Var, padx=20, font='Arial 16', pady=5, bd=5)
        labelOp = tk.Label(probFrame, textvariable=self.opVar, padx = 20, font='Arial 16', pady=5, bd=5)
        labelLine = tk.Label(probFrame, text="------------------", font="Arial 16")

        labelMess.grid(row=12, columnspan=10)
        labelV1.grid(row=0, column=1)
        labelOp.grid(row=1, column=0)
        labelV2.grid(row=1, column=1)
        labelLine.grid(row=2, columnspan=3)

        answerEntry = tk.Entry(probFrame, textvariable=self.userAns, font='Arial 16', bd=1,
                               exportselection=0, width=4, justify='center')
        answerEntry.grid(row=3, column=1)
        answerEntry.bind('<Key-Return>', self.checkAnswer)
        answerEntry.bind('<Key-Tab>', self.checkAnswer)

        # The total correct frame...
        counterFrame = tk.Frame(self.root, bd=5, relief="groove", padx=10, pady=10)
        counterFrame.grid(row=7, columnspan=10, padx=10, pady=10)
        
        txtLabel1 = tk.Label(counterFrame, text="Number correct", padx=5, pady=5, font='Arial 14 italic', fg='blue')
        labelCorr = tk.Label(counterFrame, textvariable=self.correctVar, padx=5, font='Arial 14 italic', pady=5, fg='blue')
        txtLabel2 = tk.Label(counterFrame, text="Total", padx=5, pady=5, font='Arial 14 italic', fg='blue')
        labelTot = tk.Label(counterFrame, textvariable=self.totalVar,  padx=5, font='Arial 14 italic', pady=5, fg='blue')
        txtLabel1.grid(row=0, column=1)
        labelCorr.grid(row=1, column=1)
        txtLabel2.grid(row=0, column=3)
        labelTot.grid(row=1, column=3)

        resetCounter = tk.Button(counterFrame, text="Reset count", command=self.resetCount, font='Arial 14 bold',
                                 bd=5 , relief='raised', padx=10, pady=5, bg='red', fg='blue')
        resetCounter.grid(row=0, rowspan=2, column=5, padx=10)
                          
#         # The quit button
#         quitButton = Button(master = self.root, text = 'Quit', font = 'Arial 14 bold',
#                             bd = 5 , relief = 'raised', padx = 10, pady = 10, bg = 'red', fg = 'blue', command = self.root.quit)
#         quitButton.grid(row = 12, columnspan = 10, pady = 10)
    # End of create_widgets

    def goProgram(self):
        self.root.mainloop()

    def nextProb(self):
        self.val1Var.set("")
        self.val2Var.set("")
        self.opVar.set("")
        self.correctAns.set("")
        self.messageVar.set("")
        self.userAns.set("")

        add = self.addChoice.get()
        sub =  self.subChoice.get()
        easy = self.easyChoice.get()
        hard = self.hardChoice.get()
        
        if (add == 'no' and sub == 'no'):
            probText1 = "Select a problem type!"
            # and then display the text
            #print probText1
            self.messageVar.set(probText1)
        elif (easy == 'no' and hard == 'no'):
            probText1 = "Select a difficulty level"
            # and then display the text
            #print probText1
            self.messageVar.set(probText1)
        else:
            op = self.chooseOperator(add, sub)
            v1, v2, v3 = self.chooseNumbers(easy, hard, op)
            #print v1, op, v2, '=', v3
            self.val1Var.set(v1)
            self.val2Var.set(v2)
            self.opVar.set(op)
            self.correctAns.set(v3)
        # end of else
        # end nextProb

    def chooseOperator(self, add, sub):
        # choose the operator
        if (add == 'yes' and sub == 'yes'):
            return random.choice(['+', '-'])
        elif (add == 'yes'):
            return '+'
        else:
            return '-'
        
    def chooseNumbers(self, easy, hard, op):
        # choose the numbers
        if (easy == 'yes' and hard == 'yes'):
            v1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            v2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            ans = v1 + v2
        elif (easy == 'yes'):
            ans = random.choice([3, 4, 5, 6, 7, 8, 9])
            v1 = random.randint(1, ans - 1)
            v2 = ans - v1
        else:  # hard == 'yes'
            ans = random.choice([10, 11, 12, 13, 14, 15, 16, 17, 18])
            v1 = random.randint(5, 9)
            v2 = ans - v1
        # end of if-then-else
        if op == '+':
            return v1, v2, ans
        else:
            return ans, v1, v2
        # end chooseNumbers

    def checkAnswer(self, event):
        self.messageVar.set("")

        if self.userAns.get() == self.correctAns.get():
            self.messageVar.set("Correct!!")
            self.totalVar.set(self.totalVar.get() + 1)
            self.correctVar.set(self.correctVar.get() + 1)
            self.root.after(1000, self.nextProb)
        else:
            self.totalVar.set(self.totalVar.get() + 1)
            self.messageVar.set("Wrong, try again")
    # end checkAnswer

    def resetCount(self):
        self.correctVar.set(0)
        self.totalVar.set(0)
    # end resetCount
    

def main():
    s = MathGUI()
    s.createWidgets()
    s.goProgram()
    print('back to main')
# end main


if __name__ == '__main__':

    main()
