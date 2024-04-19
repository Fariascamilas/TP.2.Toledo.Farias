import numpy as np
from PIL import Image

def open_image(path):
    return np.array(Image.open(path))
path = '..\cafe_b.jpg'
M = open_image(path)
print(M.shape)
