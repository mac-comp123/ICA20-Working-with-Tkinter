import tkinter as tk
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk


class CatMover:
    """Draws a canvas and places an image of a cat walking on it. Then the user can use the wasd keys
    to move the cat around the canvas."""

    def __init__(self):
        self.rootWin = tk.Tk()
        self.myCanvas = tk.Canvas(self.rootWin)
        self.myCanvas["width"] = 400
        self.myCanvas["height"] = 300
        self.myCanvas.grid(row=10, column=10)

        initPhoto = Image.open("catWalking.jpg")
        self.photo1 = ImageTk.PhotoImage(initPhoto)

        self.theCat = self.myCanvas.create_image(50, 50, image=self.photo1)
        self.rootWin.bind("w", self.moveCat)
        self.rootWin.bind("a", self.moveCat)
        self.rootWin.bind("s", self.moveCat)
        self.rootWin.bind("d", self.moveCat)

    def moveCat(self, event):
        if event.char == 'w':
            self.myCanvas.move(self.theCat, 0, -5)
        elif event.char == 's':
            self.myCanvas.move(self.theCat, 0, 5)
        elif event.char == 'a':
            self.myCanvas.move(self.theCat, -5, 0)
        elif event.char == 'd':
            self.myCanvas.move(self.theCat, 5, 0)

    def run(self):
        self.rootWin.mainloop()


if __name__ == '__main__':
    myGui = CatMover()
    myGui.run()
