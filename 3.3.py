from random import random

aux = 1  # variável do while
contador = 0  # variável de contagem
while aux >= 0.1:  # enquanto a variável for maior que 0.1 o código abaixo se repete
    aux = aux + 0.2 * (
        0.5 - random()
    )  # soma um número aleatório com valor entre -0.1 e 0.1 à variável do while (aux)
    contador = contador + 1  # conta quantas iterações ocorreram dentro do while
print(contador)  # mostra o numero total de iterações
