import matplotlib.pyplot as matplot
import numpy as np

COMPUTADOR = "CASA"
#COMPUTADOR = "UFS"

if (COMPUTADOR == "UFS"):
    teste =     "/media/aluno/SHAHDAD/processamentoimagens/anexo/imagens/teste.png"
    deci =      "/media/aluno/SHAHDAD/processamentoimagens/anexo/imagens/deci.png"
    lena =      "/media/aluno/SHAHDAD/processamentoimagens/anexo/lena/lena_orig.png"
    lenaCinza = "/media/aluno/SHAHDAD/processamentoimagens/anexo/lena/lena_gray.png"
    lenaOlho =  "/media/aluno/SHAHDAD/processamentoimagens/anexo/lena/lena_orig_eye.png"    
if (COMPUTADOR == "CASA"):
    teste =     r'E:\processamentoimagens\anexo\imagens\teste.png'
    deci =      r'E:\processamentoimagens\anexo\imagens\deci.png'
    lena =      r'E:\processamentoimagens\anexo\lena\lena_orig.png'
    lenaCinza = r'E:\processamentoimagens\anexo\lena\lena_gray.png'
    lenaOlho =  r'E:\processamentoimagens\anexo\lena\lena_orig_eye.png'
    
#---------
R = 0.299
G = 0.587
B = 0.114
#---------

def imread(fonte):
    imagem = matplot.imread(fonte)
    if (imagem.dtype == "float32"):
        imagem = np.uint8(255*imagem)
    if (len(imagem.shape) >= 3 and imagem.shape[2] > 3):
        imagem = imagem[:, :, 0:3]
    return imagem

def imshow(imagem):
    plot = matplot.imshow(imagem, cmap=matplot.gray(), origin="upper")
    plot.set_interpolation('nearest')
    matplot.show()

###QUESTAO 1
def nchannels(imagem):
    objeto = imagem.shape
    if (len(objeto) == 2):
        return 1
    else:
        return objeto[2] 
    
###QUESTAO 2
def size(imagem):
    objeto = imagem.shape
    altura = objeto[0]
    largura = objeto[1]
    return [largura, altura]

###QUESTAO 3
def rgb2gray(imagem):
    if (nchannels(imagem) == 1):
        return imagem
    imagemSaida = np.copy(imagem)
    imagemSaida = (
        imagem[:, :, 0] * R +
        imagem[:, :, 1] * G +
        imagem[:, :, 2] * B)
    return imagemSaida

###QUESTAO 4
def imreadgray(fonte):
    imagem = matplot.imread(fonte)
    return rgb2gray(imagem)

###QUESTAO 5:
def thresh(imagem, limiar):
    imagemSaida = np.copy(imagem)
    return imagemSaida

def negative(imagem):
    imagemSaida = np.copy(imagem)
    '''
    largura, altura = size(imagem)
    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem[y, x]
            imagemSaida[y, x] = [255 - r, 255 - g, 255 - b]
    '''
    imagemSaida = 255 - imagem
    return imagemSaida

imagemAtual = deci
#imagemAtual = lena
#imagemAtual = lenaCinza
#imagemAtual = lenaOlho

print("Numeros de canais eh: ",nchannels(imread(imagemAtual)))
print("Vetor com altura e largura: ",size(imread(imagemAtual)))
imshow(imread(imagemAtual))
imshow(imreadgray(imagemAtual))
imshow(negative(imread(imagemAtual)))
