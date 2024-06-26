import tkinter as tk
import random


class CanvasGUI2:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Second Canvas example")
        
        
        # Create a canvas object that is 500 by 500 pixels wide, with a yellow background
        self.canvas = tk.Canvas(self.rootWin, bg="yellow",width = 500, height = 500, bd = 0)
        self.canvas.grid(row = 1, column = 1)
        # Show all of the canvas
        self.canvas.config(scrollregion= self.canvas.bbox(tk.ALL))

        # Bind the canvas and main window to respond to mouse button and keyboard entry
        self.canvas.bind("<Button-1>", self.chooseBall)
        self.rootWin.bind("w", self.moveBallUp)
        self.rootWin.bind("s", self.moveBallDown)
        self.rootWin.bind("a", self.moveBallLeft)
        self.rootWin.bind("d", self.moveBallRight)

        self.rootWin.bind("<Up>", self.moveBallUp)
        self.rootWin.bind("<Down>", self.moveBallDown)
        self.rootWin.bind("<Left>", self.moveBallLeft)
        self.rootWin.bind("<Right>", self.moveBallRight)
        
        # Create an instance variable to hold which ball the user has selected
        self.selectedBall = None
        
        # Save info about the balls.  This randomizes the balls, and their speeds,
        # and uses a dictionary keyed by the ID from the canvas.  Each entry in the
        # dictionary is also a dictionary, with separate keys values for each feature
        self.ballCollection = {}
        for ballColor in ['red', 'green', 'blue', 'LightBlue', 'LightGreen']:
            nextDict = {}
            xStart = random.randint(20, 480)
            yStart = random.randint(20, 480)
            deltaX = random.randint(1, 2)
            deltaY = random.randint(1, 2)
            nextBall = self.canvas.create_oval(xStart,yStart, xStart+20, yStart+20,
                                               fill = ballColor, outline = "black")
            nextDict['xDist'] = deltaX
            nextDict['yDist'] = deltaY
            nextDict['moving'] = True
            self.ballCollection[nextBall] = nextDict

    def go(self):
        """Takes no inputs, and runs its own loop for the GUI.  This is so we can move 
        the balls without waiting for some user input."""
        try:
            while True:
                self.moveAllBalls()
                self.rootWin.update_idletasks() # redraw
                self.rootWin.update() # process events
        except tk.TclError:
            pass # to avoid errors when the window is closed

    def moveAllBalls(self):
        """Takes no inputs, and moves the balls in the ball list.  It bounces
        back when it reaches the walls of the canvas"""
        for ballId in self.ballCollection:
            ballInfo = self.ballCollection[ballId]
            if ballInfo['moving']:
                (x0, y0, x1, y1) = self.canvas.coords(ballId)
                if x1 >= 500 or x0 <= 5:
                    ballInfo['xDist'] = - ballInfo['xDist']
                if y1 >= 500 or y0 <= 5:
                    ballInfo['yDist'] = - ballInfo['yDist']
                self.canvas.move(ballId, ballInfo['xDist']/5, ballInfo['yDist']/5)

    # --------------------------------------------------------------------------
    # Below here are the callback methods for the canvas to respond to mouse 
    # and key inputs
    def chooseBall(self, event):
        """Called when the user clicks on the canvas, this determines if there is a
        ball currently selected or not. If there is a selected ball, then it "unselects" it
        and starts it moving again as normal. If there is no selected ball, then it
        checks if there is a ball close enough to where the mouse was clicked If so, then it selects
        that ball (or one of them) and stops it moving. It remembers which ball has been selected."""
        x = event.x
        y = event.y
        ballSet = self.canvas.find_overlapping(x-5, y-5, x+5, y+5)
        if self.selectedBall != None:
            ballInfo = self.ballCollection[self.selectedBall]
            ballInfo['moving'] = True
            self.selectedBall = None
        elif len(ballSet) > 0:
            self.selectedBall = ballSet[0]
            ballInfo = self.ballCollection[self.selectedBall]
            ballInfo['moving'] = False
        
    def moveBallUp(self, event):
        """Callback function that is triggered by the user typing the up arrow. It checks if any ball
        has been selected, and if so it moves it up by 5 pixels."""
        if self.selectedBall is not None:
            self.canvas.move(self.selectedBall, 0, -5)
        
    def moveBallDown(self, event):
        """Callback function that is triggered by the user typing the down arrow. It checks if any ball
        has been selected, and if so it moves it down by 5 pixels."""
        if self.selectedBall is not None:
            self.canvas.move(self.selectedBall, 0, 5)

    def moveBallLeft(self, event):
        """Callback function that is triggered by the user typing the left arrow. It checks if any ball
        has been selected, and if so it moves it left by 5 pixels."""
        if self.selectedBall is not None:
            self.canvas.move(self.selectedBall, -5, 0)

    def moveBallRight(self, event):
        """Callback function that is triggered by the user typing the right arrow. It checks if any ball
        has been selected, and if so it moves it right by 5 pixels."""
        if self.selectedBall is not None:
            self.canvas.move(self.selectedBall, 5, 0)

# end of class CanvasGUI


if __name__ == '__main__':
    # --- here it goes...
    myGui = CanvasGUI2()
    myGui.go()
