class Square:
    """
    Creates a square object at the X & Y  coordinates location on canvas
    The side will create the size of the square object.
    The color will create the color of the square object.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

     # draws the square on the canvas
    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = [self.color]



class Rectengle:
    """
    Creates a rectangle object at the X & Y coordinates location on canvas
    The width/height will create the size of the rectangle object.
    The color will create the color of the rectangle object.
     """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    # draws the rectangle on the canvas
    def draw(self, canvas):
        canvas.data[self.x:self.x + self.width, self.y:self.y + self.height] = [self.color]