# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import Dieview

def main():
# create the application window
	win = GraphWin("Dice Roller")
	win.setCoords(0,0,10,10)
	win.setBackground("green2")

	# draw the interface widgets
	die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

	# event loop
	pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

	# close the window
	win.close()

from graphics import *

class Button:
	""" A button is a labeled rectangle in a window. It is activated or deactivated
	with the activate() and deactivate() methods. The clicked (p) method returns
	true if the button is active and p is inside it. """

	def __init__ (self, win, center, width, height, label):
	"""" creates a rectangualr button, eg:
	qp = Button (myWin, centerPoint, width, height, 'quit')"""

	def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

	def clicked(self, p):
	"""returns true if the button active and p is inside"""

	def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

	def getLabel(self):
	"""returns the label string of the button"""

	def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

	def activate(self):
	"""Sets this button to 'active'"""

	def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

	def deactivate (self):
	"""Sets this button to 'active'"""
	
	def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

from graphics import *

class DieView:
	"""DieView is a widget that displays a graphical representation of a standard six-sided die."""

	def __init__(self, win, center, size):
	""" create a view of a die e.g: d1 = DieView (myWin, Point(40,50), 20).
	This creates a die centered at (40,50) with length 20. """

	# define standard values for drawing the die
		self.win = win 				#for drawing the pips
		self.background = "white"	#colour of die face
		self.foreground = "black"	#colour of pips
		self.psize = 0.1 * size 	#radius of each pip
		hsize = size/2				#half the size of the die
		offset = 0.6 * hsize		#distance from centre to outer pips

	# create a square for the face
	self.win = win            # save this for drawing pips later
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size   # radius of each pip
        hsize = size / 2.0        # half the size of the die
        offset = 0.6 * hsize      # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

	# create 7 circles for standard pip locations
	self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)

	# Draw an initial value

	def __makePip(self, x, y):
		""" Internal helper method to draw a pip at (x,y)"""
		def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

	def setValue(self, value):
		"""Set this die to display value. """

		self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

		if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)        
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)

#class definition for an n-sided die

#import packages

class MSdie:

  #constructor here
  class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

  #define classmethod 'roll' to roll the MSdie
  def roll(self):
        self.value = randrange(1, self.sides+1)

  #define classmethod 'getValue' to return the current value of the MSdie
  def getValue(self):
        return self.value

  #define classmethod 'setValue' to set the die to a particular value
  def setValue(self, value):
        self.value = value            
	

main()
