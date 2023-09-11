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


'''
tempo = np.linspace(0, 0.5, 500) # 500 números, de 0 a 0.5 -> 1 kHz de amostragem
sinal = np.sin(40 * 2 * np.pi * tempo) + 0.5 * np.sin(90 * 2 * np.pi * tempo)

matplot.xlabel("Tempo (s)")
matplot.ylabel("Amplitude")
matplot.plot(tempo, sinal)
matplot.savefig('Figura.png')
figura = "D:\ProjetosCodigo\PI\Figura.png"
imshow(imread(figura))
matplot.close()
'''