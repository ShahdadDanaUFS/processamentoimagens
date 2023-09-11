import matplotlib.pyplot as matplot
import numpy as np

COMPUTADOR = "CASA"
#COMPUTADOR = "UFS"

REF_CASA = "E"
REF_UFS = "D"

if (COMPUTADOR == "CASA"):
    caminho = REF_CASA
if (COMPUTADOR == "UFS"):
    caminho = REF_UFS

deci = caminho+r':\processamentoimagens\anexo\imagens\deci.png'
lena = caminho+r':\processamentoimagens\anexo\lena\lena_orig.png'
lenaCinza = caminho+r':\processamentoimagens\anexo\lena\lena_gray.png'
lenaOlho = caminho+r':\processamentoimagens\anexo\lena\lena_orig_eye.png'

R = 0.299
G = 0.587
B = 0.114

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
    objeto = imread(source).shape
    if (len(objeto) == 2):
        return 1
    else:
        return objeto[2] 
    
###QUESTAO 2
def size(source):
    objeto = imread(source).shape
    altura = objeto[0]
    largura = objeto[1]
    return [largura, altura]

    
imagemAtual = deci

print("Numeros de canais eh:",nchannels(imagemAtual))
print("Vetor com largura e altura:",size(imagemAtual))
imshow(imread(imagemAtual))
