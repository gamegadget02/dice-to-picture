from pyautogui import size
from PIL import Image

width, height = size()
width = (height*2)/3

image = Image.open("IMG_20221115_120137.png")
widthsm,heightsm = image.size

detail = 10