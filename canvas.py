import numpy as np
from PIL import Image


class Canvas:
    """
    Creates the main canvas to draw shapes onto
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8) # Creates a 3D array matrix (Depth 3 rows)
        self.data[:] = self.color  # Yellow

     # Pass the file name as argument and it will save the file.
    def make(self, img_path):
        img = Image.fromarray(self.data, "RGB")
        img.save(img_path)


