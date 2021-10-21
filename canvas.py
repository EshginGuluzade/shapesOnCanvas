import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.image_data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.image_data[:] = [self.color[0], self.color[1], self.color[2]]

    def make(self):
        img = Image.fromarray(self.image_data, 'RGB')
        img.save('canvas.png')