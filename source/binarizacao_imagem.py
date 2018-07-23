import cv2
from matplotlib import pyplot 
import numpy


def obter_imagem():
    imagem = cv2.imread("imagens/img.jpg", 0)
   
    return imagem


def exibir_imagem(imagem):
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def salvar_imagem(imagem):
    cv2.imwrite("imagens/img-binarizada.jpg", imagem)


def binarizar_imagem(imagem):
    limiar, imagem_binarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

    return imagem_binarizada


def binarizar_imagem_adaptive_mean(imagem):
    imagem_binarizada = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    return imagem_binarizada


def binarizar_imagem_adaptive_gaussian(imagem):
    imagem_binarizada = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return imagem_binarizada

def binarizar_imagem_adaptive_limiar_otsu(imagem):
    blur = cv2.GaussianBlur(imagem,(5,5),0)
    limiar, imagem_binarizada = cv2.threshold (blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return imagem_binarizada

def main():
    salvar_imagem(binarizar_imagem_adaptive_mean(obter_imagem()))
    exibir_imagem(binarizar_imagem_adaptive_mean(obter_imagem()))
    

if __name__ == '__main__':
    main()