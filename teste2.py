import matplotlib.pyplot as mp
import numpy as np

def imread(filename):
    im = mp.imread(filename)
    if (im.dtype == "float32"):
        im = np.uint8(255*im)
    if (len(im.shape) >= 3 and im.shape[2] > 3):
        im = im[:, :, 0:3]
    return im

def imshow(im):
    plot = mp.imshow(im, cmap=mp.gray(), origin="upper")
    plot.set_interpolation('nearest')
    mp.show()

image = imread("D:\ProjetosCodigo\PI\deci.png")
imshow(image)