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

def imread(fonte):
    imagem = matplot.imread(fonte)
    if (imagem.dtype == "float32"):
        imagem = np.uint8(255*im)
    if (len(imagem.shape) >= 3 and imagem.shape[2] > 3):
        imagem = imagem[:, :, 0:3]
    return imagem

def imshow(imagem):
    plot = matplot.imshow(imagem, cmap=matplot.gray(), origin="upper")
    plot.set_interpolation('nearest')
    matplot.show()

###QUESTAO 1
def nchannels(fonte):
    objeto = imread(fonte).shape
    if (len(objeto) == 2):
        return 1
    else:
        return objeto[2] 
    
###QUESTAO 2
def size(fonte):
    objeto = imread(fonte).shape
    altura = objeto[0]
    largura = objeto[1]
    return [largura, altura]

###QUESTAO 3
def rgb2gray(fonte):
    imagemCopia = fonte.copy()
    imagemCinza = np.dot(imagemCopia, [R, G, B])
    return imagemCinza

###QUESTAO 4
def imreadgray(fonte):
    imagem = rgb2gray(fonte)
    return imshow(imagem)



imshow(imagem_cinza)
#imshow(imread(deci))

'''
imagemAtual = deci

print("Numeros de canais eh:",nchannels(imagemAtual))
print("Vetor com largura e altura:",size(imagemAtual))
'''

