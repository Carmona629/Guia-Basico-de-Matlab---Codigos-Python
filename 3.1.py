from random import random

a = random()  # atribui a variável “a” um numero aleatório entre 1 e 0;
if a <= 0.5:  # impõe a condição da variável ser menor ou igual a 1/2
    print(
        "A variável é menor ou igual a 1/2"
    )  # se a condição é satisfeita esta mensagem é exibida

else:  # senão
    print(
        "A variável é maior que 1/2"
    )  # se a condição não é satisfeita esta mensagem é exibida
