import os
from PIL import Image
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def downscale_images(directory, size=(80, 44)):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(directory, filename))
            img = img.resize(size, Image.LANCZOS)
            img.save(os.path.join(directory, 'blurred_'+filename))

def upscale_images(directory, size=(400, 300)):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(directory, filename))
            img = img.resize(size, Image.LANCZOS)
            img.save(os.path.join(directory, 'upscaled_'+filename))


PATH = 'temp/'

downscale_images(PATH)

