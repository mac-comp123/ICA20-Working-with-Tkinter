import tkinter as tk


class MazeLines:
    """Draws lines for a maze on a canvas. Quits when user types q."""
    def __init__(self):
        self.main = tk.Tk()
        self.main.bind('q', self.quit)

        canvas = tk.Canvas(self.main, width=400, height=400, bg="light blue")
        canvas.grid(row=0, column=0)

        outlineList = [4, 4, 4, 400, 400, 400, 400, 4, 4, 4]
        line1 = [0, 100, 200, 100, 200, 200, 100, 200, 100, 300, 200, 300]
        line2 = [300, 0, 300, 200, 300, 300]
        id1 = canvas.create_line(outlineList, fill="dark red", width=3)
        print("id1", id1)
        id2 = canvas.create_line(line1, fill="dark red", width=3)
        print("id2", id2)
        id3 = canvas.create_line(line2, fill='dark red', width=3)
        print("id3", id3)

    def go(self):
        self.main.mainloop()

    def quit(self, event):
        self.main.destroy()


if __name__ == '__main__':
    ml = MazeLines()
    ml.go()
