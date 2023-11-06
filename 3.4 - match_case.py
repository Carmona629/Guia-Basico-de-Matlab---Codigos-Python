from random import random

a = int(
    (360 * random()) / 90
)  # gera um ângulo entre 0 e 360° e arredonda o valor da divisão desse ângulo por 90

match a:
    case 0:
        print("'O ângulo pertence ao primeiro quadrante.")
    case 1:
        print("'O ângulo pertence ao segundo quadrante.")
    case 2:
        print("'O ângulo pertence ao terceiro quadrante.")
    case 3:
        print("'O ângulo pertence ao quarto quadrante.")
