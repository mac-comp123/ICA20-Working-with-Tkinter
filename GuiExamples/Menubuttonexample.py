import tkinter as tk


class MenuGUI:
    def __init__(self):
        self.boss = tk.Tk()

        self.label = tk.Label(self.boss, text="Hello")
        self.label.grid(row=0, column=0, padx=20)
        self.button = tk.Menubutton(self.boss, text='Choose One', relief=tk.GROOVE)
        self.menu = tk.Menu(self.button)
        self.button['menu'] = self.menu
        self.select = tk.StringVar()
        for opt in ['option a', 'option b', 'option c', 'option d', 'option e']:
            self.menu.add_radiobutton(label=opt, variable=self.select, value=opt)
        self.button.grid(row=0, column=1)
        self.boss.bind("<Return>", self.checkMenu)

    def checkMenu(self, event):
        value = self.select.get()
        print(value)
        self.label['text'] = value

    def go(self):
        self.boss.mainloop()


if __name__ == '__main__':
    mg = MenuGUI()
    mg.go()

