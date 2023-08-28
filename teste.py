import matplotlib.pyplot as matplot
import numpy as np

def imread(source):
    im = matplot.imread(source)
    if (im.dtype == "float32"):
        im = np.uint8(255*im)
    if (len(im.shape) >= 3 and im.shape[2] > 3):
        im = im[:, :, 0:3]
    return im

def imshow(image):
    plot = matplot.imshow(image, cmap=matplot.gray(), origin="upper")
    plot.set_interpolation('nearest')
    matplot.show()

###QUESTAO 1
def nchannels(source):
    altura, largura, canais  = imread(source).shape
    return canais

###QUESTAO 2
def size(source):
    altura, largura, canais  = imread(source).shape
    return [altura, largura]

    
deci = "D:\ProjetosCodigo\PI\deci.png"

#print("Numeros de canais eh: ",nchannels(deci))
#print("Vetor com altura e largura: ",size(deci))
#imshow(imread(deci))

tempo = np.linspace(0, 0.5, 500) # 500 números, de 0 a 0.5 -> 1 kHz de amostragem
sinal = np.sin(40 * 2 * np.pi * tempo) + 0.5 * np.sin(90 * 2 * np.pi * tempo)

matplot.xlabel("Tempo (s)")
matplot.ylabel("Amplitude")
matplot.plot(tempo, sinal)
matplot.savefig('exportacao.png')
imagem = "D:\ProjetosCodigo\PI\exportacao.png"
imshow(imread(imagem))
matplot.close()