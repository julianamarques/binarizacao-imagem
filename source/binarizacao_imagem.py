import cv2
from matplotlib import pyplot 
import numpy


def obter_imagem():
    imagem = cv2.imread("imagens/img777.jpg", 0)
   
    return imagem


def exibir_imagem(imagem):
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def salvar_imagem(imagem):
    cv2.imwrite("imagens/img-binarizada.jpg", imagem)


def binarizar_imagem(imagem):
    limiar, imagem_binarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY_INV)

    return imagem_binarizada


def binarizar_imagem_adaptive_mean(imagem):
    imagem_binarizada = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 1)

    return imagem_binarizada


def binarizar_imagem_adaptive_gaussian(imagem):
    imagem_binarizada = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return imagem_binarizada


def aplicar_filtro_median_blur(imagem):
    imagem_filtrada = cv2.medianBlur(imagem, 5)

    return imagem_filtrada


def aplicar_filtro_gaussian_blur(imagem):
    imagem_filtrada = cv2.GaussianBlur(imagem,(5,5),0)

    return imagem_filtrada


def aplicar_scharr_x(imagem):
    imagem_com_scharr_x = cv2.Scharr(imagem, cv2.CV_64F, 1, 0)

    return imagem_com_scharr_x


def aplicar_scharr_y(imagem):
    imagem_com_scharr_y = cv2.Scharr(imagem, cv2.CV_64F, 0, 1)

    return imagem_com_scharr_y


def aplicar_scharr_x_y(imagem):
    imagem_com_scharr_x = cv2.Scharr(imagem, cv2.CV_64F, 1, 0)
    imagem_com_scharr_y = cv2.Scharr(imagem, cv2.CV_64F, 0, 1)

    return imagem_com_scharr_x + imagem_com_scharr_y


def aplicar_sobel_x(imagem):
    imagem_com_sobel = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)

    return imagem_com_sobel


def aplicar_sobel_y(imagem):
    imagem_com_sobel = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)

    return imagem_com_sobel


def aplicar_laplacian(imagem):
    imagem_com_laplacian = cv2.Laplacian(imagem,cv2.CV_64F)

    return imagem_com_laplacian


def aplicar_canny(imagem):
    imagem_com_canny = cv2.Canny(imagem, 100, 200)

    return imagem_com_canny


def aplicar_auto_canny(imagem, sigma=0.33):
    v = numpy.median(imagem)
    baixo = int(max(0, (1.0 - sigma) * v))
    auto = int(min(255, (1.0 + sigma) * v))
    imagem_com_canny = cv2.Canny(imagem, baixo, auto)

    return imagem_com_canny



def aplicar_sobel_x_y(imagem):
    imagem_com_sobel_x_y = aplicar_sobel_x(imagem) + aplicar_sobel_y(imagem)

    return imagem_com_sobel_x_y

def main():
    #salvar_imagem(binarizar_imagem_adaptive_mean(obter_imagem()))
    #exibir_imagem(binarizar_imagem_adaptive_mean(obter_imagem()))
    #salvar_imagem(aplicar_filtro_median_blur(binarizar_imagem_adaptive_mean(obter_imagem())))
    #salvar_imagem(aplicar_sobel_x(obter_imagem()))
    #salvar_imagem(aplicar_sobel_y(obter_imagem()))
    #salvar_imagem(aplicar_scharr_x(obter_imagem()))
    #salvar_imagem(aplicar_scharr_y(obter_imagem()))
    salvar_imagem(aplicar_scharr_x_y(obter_imagem()))
    #salvar_imagem(aplicar_laplacian(obter_imagem()))
    #salvar_imagem(aplicar_canny(obter_imagem()))
    #salvar_imagem(aplicar_canny(aplicar_filtro_gaussian_blur(obter_imagem())))
    #salvar_imagem(aplicar_auto_canny(aplicar_filtro_gaussian_blur(obter_imagem())))
    #salvar_imagem(aplicar_canny(obter_imagem()))
    #salvar_imagem(aplicar_sobel_x_y(obter_imagem()))
    #salvar_imagem(aplicar_sobel_x_y(aplicar_filtro_gaussian_blur(obter_imagem())))
    #salvar_imagem(aplicar_sobel_x_y(aplicar_filtro_median_blur(obter_imagem())))
    #salvar_imagem(binarizar_imagem(aplicar_sobel_x_y(obter_imagem())))
    #salvar_imagem(binarizar_imagem(aplicar_sobel_x(obter_imagem())))
    #salvar_imagem(binarizar_imagem(aplicar_sobel_y(obter_imagem())))
    #salvar_imagem(binarizar_imagem_adaptive_mean(obter_imagem()))


if __name__ == '__main__':
    main()
